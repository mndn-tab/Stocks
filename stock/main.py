

#from src.stock import set_stock_price 
from src.stock.general import *

# NOTE 1: because __init__.py(indicators) already has "from .sma import SMA", 
# so we dont have to write the full path "from src.indicators.sma import SMA"
# NOTE 2: IMPORTANT: need to import class SMA not module sma
from src.indicators import SMA


# Example 1: create sma object
prices = pd.Series([10, 12, 14, 13, 15, 16, 18])
sma1 = SMA("Z", 1, 7, prices, 3)
sma1.calculate_indicator()
sma1.show_indicator()


# Example 2: create stock object and add SMA indicator
prices = pd.Series([10, 12, 14, 13, 15, 16, 18])
s1 = Stock("F", 1, 7, prices)

indicator_name = s1.prompt_indicator_name()
s1.set_indicator(indicator_name)
s1.indicators_dict['SMA'].calculate_indicator()
s1.indicators_dict['SMA'].show_indicator()


