from src.modules.app.get_all_orders.get_all_order_controller import GetAllOrderController
from src.shared.helpers.http.http_models import HttpRequest
from src.shared.infra.repositories.pizzaria_repository_mock import PizzariaRepositoryMock
from src.modules.app.get_all_orders.get_all_order_usecase import GetAllOrderUsecase


class Test_GetAllOrderController:
    def test_get_all_order_controller(self):
        repo = PizzariaRepositoryMock()
        usecase = GetAllOrderUsecase(repo=repo)
        controller = GetAllOrderController(usecase=usecase)

        request = HttpRequest()

        response = controller(request=request)

        assert response.status_code == 200
        assert len(response.body['all_orders']) ==  len(repo.orders)
        assert response.body['all_orders'][0]['id'] == repo.orders[0].id
        assert response.body['all_orders'][0]['pizza']['flavor'] == repo.orders[0].pizza.flavor.value[0]
        assert response.body['all_orders'][0]['pizza']['stuffed_edge'] == repo.orders[0].pizza.stuffed_edge.value[0]
        assert response.body['all_orders'][0]['table'] == repo.orders[0].table
        assert response.body['all_orders'][0]['price'] == repo.orders[0].pizza.price
        assert response.body['message'] == 'all orders have been shown'