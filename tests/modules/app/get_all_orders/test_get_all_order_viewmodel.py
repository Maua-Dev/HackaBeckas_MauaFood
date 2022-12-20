from src.modules.app.get_all_orders.get_all_order_viewmodel import GetAllOrderViewmodel
from src.shared.infra.repositories.pizzaria_repository_mock import PizzariaRepositoryMock


class Test_GetAllOrderViewmodel:
    def test_get_all_order_viewmodel(self):
        repo = PizzariaRepositoryMock()
        all_orders = repo.orders

        result = {'all_orders': 
        [
        {'id': 1, 'table': 1, 'pizza': {'flavor': 'BACON', 'stuffed_edge': 'CHEDDAR'}, 'state': 'DONE', 'price': 35},
        {'id': 2, 'table': 2, 'pizza': {'flavor': 'MUSSARELA', 'stuffed_edge': 'CATUPIRY'}, 'state': 'DONE', 'price': 35},
        {'id': 3, 'table': 3, 'pizza': {'flavor': 'BEEF', 'stuffed_edge': 'RICOTTA'}, 'state': 'WAITING_PAYMENT', 'price': 38}, 
        {'id': 4, 'table': 4, 'pizza': {'flavor': 'VEGGIE', 'stuffed_edge': 'CLASSIC'}, 'state': 'DECLINED', 'price': 28}, 
        {'id': 5, 'table': 5, 'pizza': {'flavor': 'OLIVES', 'stuffed_edge': 'CHEDDAR'}, 'state': 'DELIVERING', 'price': 36}
        ], 
        'message': 'all orders have been shown'}

        allOrderViewModel = GetAllOrderViewmodel(all_orders).to_dict()
        
        assert allOrderViewModel == result