from src.modules.app.create_order.create_order_viewmodel import PizzaViewModel
from src.shared.domain.entities.order import Order


class DeleteOrderViewModel:
    order: Order

    def __init__(self, order:Order):
        self.order = order

    def to_dict(self) -> dict:
        return{
            "id": self.order.id,
            "table": self.order.table,
            "pizza": PizzaViewModel(self.order.pizza).to_dict(),
            "state": self.order.state.value,
            "message": "the order has been deleted"
        }
