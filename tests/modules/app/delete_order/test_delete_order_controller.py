from src.modules.app.delete_order.delete_order_controller import DeleteOrderController
from src.modules.app.delete_order.delete_order_usecase import DeleteOrderUseCase
from src.shared.helpers.http.http_models import HttpRequest
from src.shared.infra.repositories.pizzaria_repository_mock import PizzariaRepositoryMock


class Test_DeleteOrderController:
    def test_delete_order_controller(self):
        repo = PizzariaRepositoryMock()
        usecase = DeleteOrderUseCase(repo=repo)
        controller = DeleteOrderController(usecase=usecase)
        request = HttpRequest(
            body = {
                "id": "1",
            }
        )

        response = controller(request=request)
        
        assert response.status_code == 200
        assert response.body["id"] == 1
        assert response.body["pizza"]["flavor"] == "BACON"
        assert response.body["pizza"]["stuffed_edge"] == "CHEDDAR"
        assert response.body["table"] == 1
        assert response.body["message"] == "the order has been deleted"
