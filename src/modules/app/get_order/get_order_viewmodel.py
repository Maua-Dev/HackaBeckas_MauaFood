from src.modules.app.create_order.create_order_viewmodel import PizzaViewModel
from src.shared.domain.entities.order import Order

class GetOrderViewmodel:
    order: Order

    def __init__(self, order: Order):
        self.order = order

    def to_dict(self) -> dict:
        return{
            "id": self.order.id,
            "table": self.order.table,
            "pizza": PizzaViewModel(self.order.pizza).to_dict(),
            "state": self.order.state.value,
            "price": self.order.pizza.price
        }
