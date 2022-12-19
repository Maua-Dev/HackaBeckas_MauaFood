from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.enums.stuffed_edge_enum import STUFFED_EDGE
from src.shared.domain.repositories.pizzaria_repository_interface import IPizzariaRepository
from src.shared.domain.enums.flavor_enum import FLAVOR
# from src.shared.domain.enums.price_enum import PRICE
from src.shared.domain.entities.order import Order

class CreateOrderUsecase:
    def __init__(self, repo: IPizzariaRepository):
        self.repo = repo
    
    def __call__(self, id:int, table:int, flavor: FLAVOR, stuffed_edge: STUFFED_EDGE, state: STATE) -> Order:
        return self.repo.create_order(id=id, table=table, flavor=flavor, stuffed_edge=stuffed_edge, state=state)