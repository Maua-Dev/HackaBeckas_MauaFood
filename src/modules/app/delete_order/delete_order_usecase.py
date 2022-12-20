from src.shared.domain.entities.order import Order
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.enums.stuffed_edge_enum import STUFFED_EDGE
from src.shared.domain.repositories.pizzaria_repository_interface import IPizzariaRepository


class DeleteOrderUseCase:
    def __init__(self, repo: IPizzariaRepository):
        self.repo = repo

    def __call__(self, id: int) -> Order:
        return self.repo.delete_order(id=id)