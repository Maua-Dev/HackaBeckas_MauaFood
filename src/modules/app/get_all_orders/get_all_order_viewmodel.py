from typing import List
from src.modules.app.get_order.get_order_viewmodel import GetOrderViewmodel
from src.shared.domain.entities.order import Order


class GetAllOrderViewmodel:
    all_orders: List[GetOrderViewmodel]

    def __init__(self, all_orders: List[Order]):
        self.orders = [order for order in all_orders]

    def to_dict(self) -> dict:
        return {
            "all_orders": [GetOrderViewmodel(order).to_dict() for order in self.orders],
            "message": "all orders have been shown"
        }