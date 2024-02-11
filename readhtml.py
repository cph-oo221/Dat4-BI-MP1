from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
from urllib.parse import urlparse

# Method takes a webpage url,
# and returns an array of strings:
# [filetype, title, metadata, body, link0, link1, link2, link3]
# metadata is seperated in key/value by "="
# tag content and links are separated by space

def readhtml(url: str) -> [str]:
    
    try:
        print(f'Trying url: {url}')
        data = requests.get(url)
    except Exception as err:
        print(err)
        return None;
        
    html = BeautifulSoup(data.text, "html.parser")
    if html == None:
        return html;
    
    head = html.head != None
    title = ''
    metadata = ''
        
    domain = urlparse(url).netloc
        
    if head:
        title_tag = html.head.find('title')
        title = title_tag.string if title_tag != None else np.nan
        
        for meta in html.head.find_all('meta'):
            for key in meta.attrs.keys():
                metadata += f'{key}={meta[key]} '
    else:
        title = np.nan
        meta = np.nan
        
    links = []
    content = ''
    if html.body != None:
        for a_tag in html.body.find_all('a'):
            link = a_tag.get('href')
            if link is None:
                continue;
            if link.startswith('http://') or link.startswith('https://'):
                if (len(links) > 3):
                    break;
                links.append(link)
            
        for elem in html.body.stripped_strings:
            content += elem + ' '
    links.extend([np.nan] * (4 - len(links)))
    
    return 'html', domain, title, content, metadata, *links

# takes an array of start urls, and integer representing the depth of the search
# calls readhtml recursively and blacklists bad responses, and already visited pages
# returns a pandas dataframe, with ad added "level" attribute.

def readhtml_recursively(start_urls: [str], max_depth: int):
    
    df = pd.DataFrame(columns = ['filetype', 'domain', 'title', 'content', 'meta', 'link0', 'link1', 'link2', 'link3', 'level'])
    urls_to_read = start_urls
    black_list = []
    
    for iteration in range(max_depth):
        for url in urls_to_read:
            result = readhtml(url)
            if result != None:
                df.loc[len(df.index)] = [*result, iteration]
            else:
                black_list.append(url)
            

        links0 = df['link0'].to_list()
        links1 = df['link1'].to_list()
        links2 = df['link2'].to_list()
        links3 = df['link3'].to_list()

        links_total = [*links0, *links1, *links2, *links3]
        
        urls_to_read.clear()
        for link in links_total:
            if isinstance(link, str) and link not in black_list:
                urls_to_read.append(link)
                black_list.append(link)
    
    return df;
