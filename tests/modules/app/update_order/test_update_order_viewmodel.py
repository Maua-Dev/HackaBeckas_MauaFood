from src.modules.app.update_order.update_order_viewmodel import UpdateOrderViewmodel
from src.shared.domain.entities.order import Order
from src.shared.domain.entities.pizza import Pizza
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.enums.stuffed_edge_enum import STUFFED_EDGE
from src.shared.infra.repositories.pizzaria_repository_mock import PizzariaRepositoryMock


class Test_UpdateOrderViewmodel:
    def test_update_order_viewmodel(self):

        order = Order(id=1,pizza=Pizza(flavor=FLAVOR.BEEF,stuffed_edge=STUFFED_EDGE.RICOTTA), state=STATE.DELIVERING, table=1)

        updateOrderViewmodel = UpdateOrderViewmodel(order = order).to_dict()

        assert updateOrderViewmodel == {"id": 1, "pizza":{"flavor":"BEEF","stuffed_edge":"RICOTTA"}, "state": "DELIVERING", "message":"The order has been updated!"}