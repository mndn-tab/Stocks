import pandas as pd
import numpy as np

from .indicator import Indicator


class SMA(Indicator):

    def __init__(self, symbol, start_date, end_date, price, period):
        super().__init__(symbol, start_date, end_date, price)
        self.period = period
        self.sma = pd.Series()

    #TODO: check if range covers the start_date and end_date boundries of the series
    def calculate_indicator(self):
        for i in range (self.end_date - self.start_date - self.period + 1):
            self.sma.loc[i] = self.price[i : i + self.period].mean()

    def show_indicator(self):
        print(self.sma)

      


