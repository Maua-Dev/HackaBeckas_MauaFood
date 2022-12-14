from src.shared.domain.enums.stuffed_edge_enum import STUFFED_EDGE
from src.shared.domain.repositories.pizzaria_repository_interface import IPizzariaRepository
from src.shared.domain.enums.flavor_enum import FLAVOR
# from src.shared.domain.enums.price_enum import PRICE
from src.shared.domain.entities.order import Order

class CreateOrderUsecase:
    def __init__(self, repo: IPizzariaRepository):
        self.repo = repo
    
    def __call__(self, table:int, flavor: FLAVOR, stuffed_edge: STUFFED_EDGE) -> Order:
        return self.repo.create_order(table=table, flavor=flavor, stuffed_edge=stuffed_edge)