from pandas_datareader import data, wb
from datetime import datetime
import pandas as pd
import numpy as np


def finance():
    # CitiGroup
    BAC = data.DataReader('BAC', start='2006, 1, 1', end='2016, 1, 1', data_source='yahoo')
    C = data.DataReader('C', start='2006, 1, 1', end='2016, 1, 1', data_source='yahoo')
    GS = data.DataReader('GS', start='2006, 1, 1', end='2016, 1, 1', data_source='yahoo')
    JPM = data.DataReader('JPM', start='2006, 1, 1', end='2016, 1, 1', data_source='yahoo')
    MS = data.DataReader('MS', start='2006, 1, 1', end='2016, 1, 1', data_source='yahoo')
    WFC = data.DataReader('WFC', start='2006, 1, 1', end='2016, 1, 1', data_source='yahoo')
    #  Create a list of the ticker symbols (as strings) in alphabetical order. Call this list: tickers
    tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']
    # Use pd.concat to concatenate the bank dataframes together to a single data frame called bank_stocks.
    # Set the keys argument equal to the tickers list. Also pay attention to what axis you concatenate on.
    bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC], axis=1, keys=tickers)
    print(bank_stocks.head())
    # Set the column name levels (this is filled out for you):
    bank_stocks.columns.names = ['Bank Ticker', 'Stock Info']
    print(bank_stocks.head())
    # What is the max Close price for each bank's stock throughout the time period?
    print(bank_stocks.xs(key='Close', axis=1, level='Stock Info').max())







if __name__ == '__main__':
    finance()
