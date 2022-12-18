from src.modules.app.delete_order.delete_order_viewmodel import DeleteOrderViewModel
from src.shared.infra.repositories.pizzaria_repository_mock import PizzariaRepositoryMock


class Test_DeleteOrderViewModel:
    def test_delete_order_viewmodel(self):
        repo = PizzariaRepositoryMock()

        deleteOrderViewModel = DeleteOrderViewModel(order = repo.orders[0]).to_dict()

        assert deleteOrderViewModel == {'id': 1, 'table': 1, 'pizza': {'flavor': 'BACON', 'stuffed_edge': 'CHEDDAR'}, "message": "the order has been deleted"}