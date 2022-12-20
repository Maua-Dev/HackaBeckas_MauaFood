from abc import ABC, abstractmethod
from typing import List
from src.shared.domain.enums.flavor_enum import FLAVOR
# from src.shared.domain.enums.price_enum import PRICE
from src.shared.domain.entities.order import Order
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.enums.stuffed_edge_enum import STUFFED_EDGE


class IPizzariaRepository(ABC):

    @abstractmethod
    def create_order(self, id: int, table: int, flavor: FLAVOR, stuffed_edge: STUFFED_EDGE, state: STATE) -> Order:
        pass
    
    @abstractmethod
    def delete_order(self, id: int) -> Order:
        pass

    @abstractmethod
    def update_order(self, id: int, new_flavor: FLAVOR, new_stuffed_edge: STUFFED_EDGE, new_state: STATE) -> Order:
        pass

    @abstractmethod
    def get_order(self, id: int) -> Order:
        pass

    @abstractmethod
    def get_all_orders(self) -> List[Order]:
        pass