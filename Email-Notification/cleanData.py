import pandas as pd
import datetime as dt
import turicreate as tc


def getCleanData(sf):
    sf['time'] = sf['created_at'].str_to_datetime(format='%Y-%m-%dT%H:%M:%S%ZP')
    st = sf['time'][0]
    sf['difference'] = (sf['time'] - st)
    df = sf.to_dataframe()
    return df
