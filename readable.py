
import os
from datetime import datetime
import pandas as pd

def read_txt(filename):
    with open(filename, 'r') as file:
        raw_txt = file.read()

    mymeta = getMetaTxt(filename)
    # df = getDfTxt(raw_txt)
    
    return mymeta, raw_txt # , df

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

def getMetaTxt(filename):
    metadata = {}

    time_pattern = '%Y-%m-%d %H:%M:%S'

    pt = os.path
    
    metadata['created'] = unixtime_to_datetime(pt.getctime(filename), time_pattern)
    metadata['modified'] = unixtime_to_datetime(pt.getmtime(filename), time_pattern)
    metadata['size'] = pt.getsize(filename)
    return metadata
    

def unixtime_to_datetime(unix, pattern):
    return datetime.fromtimestamp(unix).strftime(pattern)
