from typing import List
from src.shared.domain.enums.flavor_enum import FLAVOR
# from src.shared.domain.enums.price_enum import PRICE
from src.shared.domain.entities.pizza import Pizza
from src.shared.domain.entities.order import Order
from src.shared.domain.repositories.pizzaria_repository_interface import IPizzariaRepository

class PizzariaRepositoryMock(IPizzariaRepository):
    orders: List[Order]

    def __init__(self):
        self.orders = [
            Order(
                pizza = Pizza(flavor = FLAVOR.BACON),
                table = 1
            ),
            Order(
                pizza = Pizza(flavor = FLAVOR.MUSSARELA),
                table = 2
            ),
            Order(
                pizza = Pizza(flavor = FLAVOR.BEEF),
                table = 3
            ),
            Order(
                pizza = Pizza(flavor = FLAVOR.VEGGIE),
                table = 4
            ),
            Order(
                pizza = Pizza(flavor = FLAVOR.OLIVES),
                table = 5
            )
        ]

    def create_order(self, table: int, flavor: FLAVOR) -> Order:
        order = Order(table = table, pizza = Pizza(flavor = flavor))
        self.orders.append(order)
        
        return order