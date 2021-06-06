import urllib.request
import pandas as pd
import numpy as np


def saveData():
    url = 'https://thingspeak.com/channels/1408499/feed.csv'
    urllib.request.urlretrieve(url, './1.csv')


def splitData(df):
    temperature = np.array(df.tail(1)['field2'])
    time = np.array(df.tail(1)['created_at'])
    return temperature, time
