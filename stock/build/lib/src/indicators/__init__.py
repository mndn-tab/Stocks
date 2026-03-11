# relative import: "." says that we are in the current package (indicators)
from .indicator import Indicator
from .sma import SMA
print("imported indicators")

INDICATORS = ["SMA", "RSI"]
