
import os
from datetime import datetime
import pandas as pd

def read_txt(filename):
    with open(filename, 'r') as file:
        raw_txt = file.read()

    mymeta = getMetaTxt(filename)
    
    return mymeta, raw_txt


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
