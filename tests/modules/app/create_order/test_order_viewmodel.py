import pytest
from src.modules.app.create_order.create_order_viewmodel import CreateOrderViewModel
from src.shared.infra.repositories.pizzaria_repository_mock import PizzariaRepositoryMock

class Test_CreateOrderViewModel:
    def test_create_order_viewmodel(self):
        repo = PizzariaRepositoryMock()

        createOrderViewModel = CreateOrderViewModel(order=repo.orders[4]).to_dict()

        assert createOrderViewModel == {'id': 5, 'pizza': {'flavor': 'OLIVES', 'stuffed_edge': 'CHEDDAR'}, 'table': 5, 'message': 'the order has been created'}