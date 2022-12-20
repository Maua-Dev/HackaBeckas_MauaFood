from src.modules.app.delete_order.delete_order_usecase import DeleteOrderUseCase
from src.modules.app.update_order.update_order_controller import UpdateOrderController
from src.modules.app.update_order.update_order_usecase import UpdateOrderUsecase
from src.shared.helpers.http.http_models import HttpRequest
from src.shared.infra.repositories.pizzaria_repository_mock import PizzariaRepositoryMock


class Test_UpdateOrderController:
    def test_update_order_controller(self):
        repo = PizzariaRepositoryMock()
        usecase = UpdateOrderUsecase(repo=repo)
        controller = UpdateOrderController(usecase=usecase)
        request = HttpRequest(
            body = {
                "id": "1",
                "new_flavor": "BEEF",
                "new_stuffed_edge": "RICOTTA",
                "new_state": "DELIVERING"
            }
        )

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body["id"] == 1
        assert response.body["pizza"]["flavor"] == "BEEF"
        assert response.body["pizza"]["stuffed_edge"] == "RICOTTA"
        assert response.body["state"] == "DELIVERING"
        assert response.body["message"] == "The order has been updated!"