import pytest
from src.modules.create_order.create_order_viewmodel import CreateOrderViewModel
from src.shared.infra.repositories.pizzaria_repository_mock import PizzariaRepositoryMock

class Test_CreateOrderViewModel:
    def test_create_order_viewmodel(self):
        repo = PizzariaRepositoryMock()

        orderViewModel = CreateOrderViewModel(order=repo.orders[0]).to_dict()

        assert orderViewModel == {'pizza': {'flavor': 'BACON','price': 'BACON'}, 'table': 1, 'message': 'the order has been created'}