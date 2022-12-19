from src.modules.app.get_order.get_order_viewmodel import GetOrderViewmodel
from src.shared.infra.repositories.pizzaria_repository_mock import PizzariaRepositoryMock


class Test_GetOrderViewmodel:
    def test_get_order_viewmodel(self):
        repo = PizzariaRepositoryMock()

        updateOrderViewModel = GetOrderViewmodel(order=repo.orders[0]).to_dict()

        assert updateOrderViewModel == {"id": 1, "table": 1, "pizza": {"flavor": "BACON", "stuffed_edge": "CHEDDAR"}, "price": 35}