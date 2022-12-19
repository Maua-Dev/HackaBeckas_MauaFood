import abc

from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.enums.stuffed_edge_enum import STUFFED_EDGE
from src.shared.helpers.errors.domain_errors import EntityError

class Pizza(abc.ABC):
    flavor : FLAVOR
    stuffed_edge: STUFFED_EDGE
    price : int

    def __init__(self, flavor: FLAVOR, stuffed_edge: STUFFED_EDGE):
        if(flavor == None or type(flavor) != FLAVOR):
            raise EntityError('flavor')

        if(stuffed_edge == None or type(stuffed_edge) != STUFFED_EDGE):
            raise EntityError('stuffed_edge')
            
        self.flavor = flavor
        self.stuffed_edge = stuffed_edge
        self.price = flavor.value[1] + stuffed_edge.value[1]

    def __repr__(self):
        return f'Pizza(flavor={self.flavor.value[0]}, stuffed_edge={self.stuffed_edge.value[0]}, price={self.price})'