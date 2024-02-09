
from datetime import datetime
import os

def getMeta(filename):
    metadata = {}
    pt = os.path

    time_pattern = '%Y-%m-%d %H:%M:%S'
    
    metadata['created'] = unixtime_to_datetime(pt.getctime(filename), time_pattern)
    metadata['modified'] = unixtime_to_datetime(pt.getmtime(filename), time_pattern)
    metadata['size'] = pt.getsize(filename)
    return metadata

def unixtime_to_datetime(unix, pattern):
    return datetime.fromtimestamp(unix).strftime(pattern)
