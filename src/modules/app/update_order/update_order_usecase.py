from src.shared.domain.entities.order import Order
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.enums.stuffed_edge_enum import STUFFED_EDGE
from src.shared.domain.repositories.pizzaria_repository_interface import IPizzariaRepository
from src.shared.helpers.errors.domain_errors import EntityError


class UpdateOrderUsecase:
    def __init__(self, repo: IPizzariaRepository):
        self.repo = repo

    def __call__(self, id: int, new_flavor: FLAVOR, new_stuffed_edge: STUFFED_EDGE, new_state: STATE) -> Order:
        if(new_flavor == None or type(new_flavor) != FLAVOR):
            raise EntityError('new_flavor')

        if(new_stuffed_edge == None or type(new_stuffed_edge) != STUFFED_EDGE):
            raise EntityError('new_stuffed_edge')

        if (new_state == None or type(new_state) != STATE):
            raise EntityError('new_state')
        
        return self.repo.update_order(id=id, new_flavor=new_flavor, new_stuffed_edge=new_stuffed_edge, new_state=new_state)