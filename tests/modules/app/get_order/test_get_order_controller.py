from src.modules.app.get_order.get_order_controller import GetOrderController
from src.modules.app.get_order.get_order_usecase import GetOrderUsecase
from src.shared.helpers.http.http_models import HttpRequest
from src.shared.infra.repositories.pizzaria_repository_mock import PizzariaRepositoryMock


class Test_GetOrderController:
    def test_get_order_controller(self):
        repo = PizzariaRepositoryMock()
        usecase = GetOrderUsecase(repo=repo)
        controller = GetOrderController(usecase=usecase)
        request = HttpRequest(
            query_params= {
                "id": "1"
            }
        )

        response = controller(request=request)
        assert response.status_code == 200
        assert response.body['id'] == repo.orders[0].id
        assert response.body['table'] == repo.orders[0].table
        assert response.body['pizza']['flavor'] == repo.orders[0].pizza.flavor.value[0]
        assert response.body['pizza']['stuffed_edge'] == repo.orders[0].pizza.stuffed_edge.value[0]
        assert response.body['price'] == repo.orders[0].pizza.flavor.value[1] + repo.orders[0].pizza.stuffed_edge.value[1]