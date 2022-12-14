from abc import ABC, abstractmethod
from src.shared.domain.enums.flavor_enum import FLAVOR
# from src.shared.domain.enums.price_enum import PRICE
from src.shared.domain.entities.order import Order
from src.shared.domain.enums.stuffed_edge_enum import STUFFED_EDGE


class IPizzariaRepository(ABC):

    @abstractmethod
    def create_order(self, table: int, flavor: FLAVOR, stuffed_edge: STUFFED_EDGE) -> Order:
        pass