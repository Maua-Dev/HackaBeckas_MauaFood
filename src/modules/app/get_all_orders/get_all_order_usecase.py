from typing import Dict, List
from src.shared.domain.entities.order import Order
from src.shared.domain.repositories.pizzaria_repository_interface import IPizzariaRepository


class GetAllOrderUsecase:
    def __init__(self, repo: IPizzariaRepository):
        self.repo = repo

    def __call__(self) -> List[Order]:
        return self.repo.get_all_orders()
