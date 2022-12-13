from src.shared.domain.entities.order import Order
from src.shared.domain.entities.pizza import Pizza
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.enums.price_enum import PRICE


class PizzaViewModel:
    pizza: Pizza

    def __init__(self, pizza:Pizza):
        self.pizza = pizza

    def to_dict(self) -> dict:
        return {
            "flavor": self.pizza.flavor.value,
            "price": self.pizza.flavor.value
        }

class CreateOrderViewModel:
    order:Order

    def __init__(self, order:Order):
        self.order = order

    def to_dict(self) -> dict:
        return{
            "table": self.order.table,
            "pizza": PizzaViewModel(self.order.pizza).to_dict(),
            "message": "the order has been created"
        }

