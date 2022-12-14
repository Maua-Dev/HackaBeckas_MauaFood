import pytest
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.enums.stuffed_edge_enum import STUFFED_EDGE
from src.shared.domain.repositories.pizzaria_repository_interface import IPizzariaRepository
from src.shared.domain.enums.flavor_enum import FLAVOR
# from src.shared.domain.enums.price_enum import PRICE
from src.shared.domain.entities.order import Order
from src.modules.app.create_order.create_order_usecase import CreateOrderUsecase
from src.shared.infra.repositories.pizzaria_repository_mock import PizzariaRepositoryMock

class Test_CreateOrderUsecase:
    def test_create_order_usecase(self):
        repo = PizzariaRepositoryMock()
        usecase = CreateOrderUsecase(repo=repo)
        
        lenBefore = len(repo.orders)
        
        order = usecase(id=6, table=6, flavor=FLAVOR.BACON, stuffed_edge=STUFFED_EDGE.CLASSIC, state=STATE.WAITING_PAYMENT)
        
        assert len(repo.orders) == lenBefore + 1
        assert order.id == 6
        assert order.table == 6
        assert order.pizza.flavor == FLAVOR.BACON
        assert order.pizza.stuffed_edge == STUFFED_EDGE.CLASSIC
        assert order.state == STATE.WAITING_PAYMENT
        assert order.pizza.price == FLAVOR.BACON.value[1] + STUFFED_EDGE.CLASSIC.value[1]

    def __repr__(self):
        return f'repo={PizzariaRepositoryMock}'

