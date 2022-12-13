import pytest
from src.shared.domain.repositories.pizzaria_repository_interface import IPizzariaRepository
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.enums.price_enum import PRICE
from src.shared.domain.entities.order import Order
from src.modules.create_order.create_order_usecase import CreateOrderUsecase
from src.shared.infra.repositories.pizzaria_repository_mock import PizzariaRepositoryMock

class Test_CreateOrderUsecase:
    def test_create_order_usecase(self):
        repo = PizzariaRepositoryMock()
        usecase = CreateOrderUsecase(repo=repo)
        
        lenBefore = len(repo.orders)
        
        order = usecase(table=4, flavor=FLAVOR.BACON, price = PRICE.BACON)
        
        assert len(repo.orders) == lenBefore + 1
        assert order.table == 4
        assert order.pizza.flavor == FLAVOR.BACON
        assert order.pizza.price == PRICE.BACON

#Erro de testes