from __future__ import (absolute_import, division, print_function, unicode_literals)
import shutil
import os

import backtrader as bt
#from TiingoFeed import TiingoDirectData
from TiingoFeed import GenerateTiingoDataFeed

from tiingo import TiingoClient
from configuration.config import Config

cleanup = True #if True, will clean up data directory when done using it.

class TestStrategy(bt.Strategy):
    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.dataclose = self.datas[0].close

    def next(self):
        # Log closing price
        self.log('Close, %.2f' % self.dataclose[0])

def cleanUp():
    datapath = os.path.join(os.getcwd(), "data")
    shutil.rmtree(datapath)
    os.mkdir(datapath)

if __name__ == '__main__':
    cerebro = bt.Cerebro()

    cerebro.addstrategy(TestStrategy)

    cerebro.broker.setcash(100000.0)

    datapath = os.path.abspath("../msft.csv")
    print(datapath)


    msftdata = GenerateTiingoDataFeed("MSFT", frequency="daily", startDate="2018-08-21", endDate="2018-08-31")

    cerebro.adddata(msftdata)


    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    if(cleanup):
        cleanUp()