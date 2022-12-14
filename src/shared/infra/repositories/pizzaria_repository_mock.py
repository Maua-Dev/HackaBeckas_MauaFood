from typing import List
from src.shared.domain.enums.flavor_enum import FLAVOR
# from src.shared.domain.enums.price_enum import PRICE
from src.shared.domain.entities.pizza import Pizza
from src.shared.domain.entities.order import Order
from src.shared.domain.enums.stuffed_edge_enum import STUFFED_EDGE
from src.shared.domain.repositories.pizzaria_repository_interface import IPizzariaRepository

class PizzariaRepositoryMock(IPizzariaRepository):
    orders: List[Order]

    def __init__(self):
        self.orders = [
            Order(
                pizza = Pizza(flavor = FLAVOR.BACON, stuffed_edge = STUFFED_EDGE.CHEDDAR),
                table = 1
            ),
            Order(
                pizza = Pizza(flavor = FLAVOR.MUSSARELA, stuffed_edge = STUFFED_EDGE.CATUPIRY),
                table = 2
            ),
            Order(
                pizza = Pizza(flavor = FLAVOR.BEEF, stuffed_edge = STUFFED_EDGE.RICOTTA),
                table = 3
            ),
            Order(
                pizza = Pizza(flavor = FLAVOR.VEGGIE, stuffed_edge = STUFFED_EDGE.CLASSIC),
                table = 4
            ),
            Order(
                pizza = Pizza(flavor = FLAVOR.OLIVES, stuffed_edge = STUFFED_EDGE.CHEDDAR),
                table = 5
            )
        ]

    def create_order(self, table: int, flavor: FLAVOR, stuffed_edge: STUFFED_EDGE) -> Order:
        order = Order(table = table, pizza = Pizza(flavor = flavor, stuffed_edge = stuffed_edge))
        self.orders.append(order)   
        return order