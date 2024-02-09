
import pandas as pd
from meta import getMeta

def read_json(filename):
    with open(filename, "r") as json:
        tmp_json = json.read()

    data = getDf(tmp_json)
    mymeta = getMeta(filename)
    return mymeta, data

def getDf(data):
    json_data = eval(data)
    df = pd.DataFrame(json_data)
    return df
