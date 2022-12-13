import abc

from src.shared.domain.enums.flavor_enum import FLAVOR

from src.shared.helpers.errors.domain_errors import EntityError

class Pizza(abc.ABC):
    flavor : FLAVOR
    price : int

    def __init__(self, flavor: FLAVOR):
        if(flavor == None or type(flavor) != FLAVOR):
            raise EntityError('flavor')
            
        self.flavor = flavor
        
        self.price = flavor.value[1]

    def __repr__(self):
        return f'Pizza(flavor={self.flavor.value[0]}, price={self.price})'