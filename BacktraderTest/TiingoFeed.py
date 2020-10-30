#### Standard Imports
from __future__ import (absolute_import, division, print_function, unicode_literals)

import os
import time


#### Imports from open-source projects
from backtrader.utils.py3 import filter, string_types, integer_types
from backtrader import date2num
from tiingo import TiingoClient

import backtrader.feeds as feed

#### Imports from my own module
from configuration.config import Config


class TiingoDirectData(feed.GenericCSVData):
    '''
    Parses the Tiingo historical prices csv file.


    '''

    params = (

        ('dtformat', '%Y-%m-%d'), #2017-08-01

        ('close', 1),
        ('high', 2),
        ('low', 3),
        ('open', 4),
        ('volume', 5),
        ('openinterest', -1)
    )


def TiingoPullToFile(ticker: str, frequency: str = "daily", startDate : str = None, endDate:str = None):
    client = TiingoClient(Config['Tiingo'])

    if (frequency is None):
        frequency = "daily"
    if (startDate is None or endDate is None):
        historical_prices = client.get_ticker_price(ticker, fmt='csv', frequency=frequency)
    else:
        historical_prices = client.get_ticker_price(ticker, fmt='csv', frequency=frequency, startDate=startDate, endDate=endDate)

    fileName = os.path.join(os.getcwd(),
                            "data/" + str(time.time()) +
                            str(ticker) + str(startDate) +
                            str(endDate) + str(frequency) + ".csv")

    csvwrite = open(fileName, 'w')
    csvwrite.write(historical_prices)
    csvwrite.close()

    return fileName


def GenerateTiingoDataFeed(ticker: str, frequency: str = "daily", startDate: str =None, endDate:str =None):
    fileName = TiingoPullToFile(ticker, frequency=frequency, startDate=startDate, endDate=endDate)
    dataFeed = TiingoDirectData(dataname=fileName)
    return dataFeed