import abc

from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.enums.price_enum import PRICE
from src.shared.helpers.errors.domain_errors import EntityError

class Pizza(abc.ABC):
    flavor : FLAVOR
    price : PRICE

    def __init__(self, flavor: FLAVOR, price: PRICE):
        if(flavor == None or type(flavor) != FLAVOR):
            raise EntityError('flavor')
        self.flavor = flavor
        
        if(price == None or type(price) != PRICE):
            raise EntityError('price')
        self.price = price