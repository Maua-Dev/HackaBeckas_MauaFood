from src.shared.domain.entities.order import Order
from src.shared.domain.repositories.pizzaria_repository_interface import IPizzariaRepository
from src.shared.helpers.errors.domain_errors import EntityError


class GetOrderUsecase:
    def __init__(self, repo:IPizzariaRepository):
        self.repo = repo

    def __call__(self, id: int) -> Order:
        if(id == None and type(id) != int and id <= 0):
            raise EntityError('id')

        return self.repo.get_order(id=id)