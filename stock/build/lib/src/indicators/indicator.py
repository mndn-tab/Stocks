import pandas as pd
import numpy as np

# abstract class
# can not instantiate an abstract class
from abc import ABC, abstractmethod

class Indicator(ABC):

    def __init__(self, symbol, start_date, end_date, price):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.price = pd.Series(price)

    @abstractmethod
    def calculate_indicator(self):
        pass

    @abstractmethod
    def show_indicator(self):
        pass




