
import pandas as pd
from meta import getMeta

def read_txt(filename):
    with open(filename, 'r') as file:
        raw_txt = file.read()

    txt = getDfTxt(raw_txt)
    
    mymeta = getMeta(filename)
    
    return mymeta, txt

def getDfTxt(raw_txt):

    # Splitting raw_txt into lines and removing any leading/trailing whitespaces
    lines = [line.strip() for line in raw_txt.split('\n')]

    # Extracting column names from the first line (assuming it contains headers)
    columns = [column.strip() for column in lines[0].split(',')]

    # Extracting data from subsequent lines
    data = [line.split(',') for line in lines[1:]]

    # Make DataFrame
    df = pd.DataFrame(data, columns=columns)
    return df
