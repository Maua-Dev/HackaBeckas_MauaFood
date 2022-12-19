import pytest
from src.modules.app.create_order.create_order_usecase import CreateOrderUsecase
from src.shared.infra.repositories.pizzaria_repository_mock import PizzariaRepositoryMock
from src.modules.app.create_order.create_order_controller import CreateOrderController
from src.shared.helpers.http.http_models import HttpRequest

class Test_CreateOrderController():
    def test_create_order_controller(self):
        repo = PizzariaRepositoryMock()
        usecase = CreateOrderUsecase(repo=repo)
        controller = CreateOrderController(usecase=usecase)
        request = HttpRequest(
            body = {
                "id": "6",
                "table": "6",
                "flavor": "BACON",
                "stuffed_edge": "CLASSIC"
            }
        )

        response = controller(request=request)

        assert response.status_code == 201
        assert response.body["id"] == 6
        assert response.body["pizza"]["flavor"] == "BACON"
        assert response.body["pizza"]["stuffed_edge"] == "CLASSIC"
        assert response.body["table"] == 6
        assert response.body["message"] == "the order has been created"