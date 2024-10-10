# models/__init__.py
from .houses import House, HouseCreate
from .wolves import Wolf, WolfCreate
from .pigs import Pig, PigCreate

__all__ = ['House', 'HouseCreate', 'Wolf', 'WolfCreate', 'Pig', 'PigCreate']