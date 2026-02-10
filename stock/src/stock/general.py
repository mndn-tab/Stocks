
import pandas as pd
import numpy as np

# absolute import: write the full path of directory
from src.indicators import *
# relative import: ".." goes one directory up to reach the "indicators" directory
# from ..indicators.indicator import Indicator

class Stock:

    # TODO: make it series
    #symbol = "MSFT"
    #start_date = 1
    #end_date = 1
    #price = 1

    # TODO: change start_date and end_date to DATE type (instead of char)
    def __init__(self, symbol, start_date, end_date, price):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.price = pd.Series(price)
        # composition: adding a dict of indicator objects, as class attribute 
        self.indicators_dict = {}
        self.init_indicators_dict()

    #TODO: instead of None add an indictor object
    def init_indicators_dict(self):
        for key in INDICATORS:
            self.indicators_dict[key] = None

    # add an indicator to the indicators_dict
    def set_indicator(self, indicator_name):
        # add sma 
        if indicator_name == "SMA":
            period = int(input("Enter period for SMA: "))
            indicator = SMA(self.symbol, self.start_date, self.end_date, self.price, period)

        self.indicators_dict[indicator_name] = indicator

    # get indicator_name from user
    def prompt_indicator_name(self):

        indicator_name = input("Enter indicator name: ")
        indicator_name = indicator_name.upper().strip()
        if indicator_name in self.indicators_dict.keys():
            return indicator_name
        else:
            raise ValueError("unknown indicator")

        

#prices = pd.Series([10, 12, 14, 13, 15, 16, 18])
#s1 = Stock("F", 2, 2, prices)
#print(s1.symbol)

        