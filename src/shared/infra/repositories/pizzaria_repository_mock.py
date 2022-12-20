from typing import List
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.entities.pizza import Pizza
from src.shared.domain.entities.order import Order
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.enums.stuffed_edge_enum import STUFFED_EDGE
from src.shared.domain.repositories.pizzaria_repository_interface import IPizzariaRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound

class PizzariaRepositoryMock(IPizzariaRepository):
    orders: List[Order]

    def __init__(self):
        self.orders = [
            Order(
                id = 1,
                pizza = Pizza(flavor = FLAVOR.BACON, stuffed_edge = STUFFED_EDGE.CHEDDAR),
                table = 1,
                state = STATE.DONE
            ),
            Order(
                id = 2,
                pizza = Pizza(flavor = FLAVOR.MUSSARELA, stuffed_edge = STUFFED_EDGE.CATUPIRY),
                table = 2,
                state = STATE.DONE
            ),
            Order(
                id = 3,
                pizza = Pizza(flavor = FLAVOR.BEEF, stuffed_edge = STUFFED_EDGE.RICOTTA),
                table = 3,
                state = STATE.WAITING_PAYMENT
            ),
            Order(
                id = 4,
                pizza = Pizza(flavor = FLAVOR.VEGGIE, stuffed_edge = STUFFED_EDGE.CLASSIC),
                table = 4,
                state = STATE.DECLINED
            ),
            Order(
                id = 5,
                pizza = Pizza(flavor = FLAVOR.OLIVES, stuffed_edge = STUFFED_EDGE.CHEDDAR),
                table = 5,
                state = STATE.DELIVERING
            )
        ]

    def create_order(self, id: int, table: int, flavor: FLAVOR, stuffed_edge: STUFFED_EDGE, state: STATE) -> Order:
        order = Order(id = id, table = table, pizza = Pizza(flavor = flavor, stuffed_edge = stuffed_edge), state = state)
        self.orders.append(order)
        return order

    def delete_order(self, id: int) -> Order:
        for ids in range(len(self.orders)):
            if (self.orders[ids].id == id):
                order = self.orders.pop(ids)
                return order
        raise NoItemsFound("id")

    def update_order(self, id: int, new_flavor: FLAVOR=None, new_stuffed_edge: STUFFED_EDGE=None, new_state: STATE=None) -> Order:
        idsOrder = -1

        for ids, possible_order in enumerate(self.orders):
            if (possible_order.id == id):
                order = possible_order
                idsOrder = ids
                break

        if idsOrder == -1:
            raise NoItemsFound("id")

        if new_flavor != None:
            order.pizza.flavor = new_flavor

        if new_stuffed_edge != None:
            order.pizza.stuffed_edge = new_stuffed_edge

        if new_state != None:
            order.state = new_state

        self.orders[idsOrder] = order

        return self.orders[idsOrder]

    def get_order(self, id: int) -> Order:
        for order in self.orders:
            if (order.id == id):
                return order
        return None

    def get_all_orders(self) -> List[Order]:
        return self.orders