from src.shared.helpers.http.http_lambda_requests import LambdaHttpResponse, LambdaHttpRequest
from src.modules.app.update_order.update_order_controller import UpdateOrderController
from src.modules.app.update_order.update_order_usecase import UpdateOrderUsecase
from src.shared.infra.repositories.pizzaria_repository_mock import PizzariaRepositoryMock


def lambda_handler(event, context):
    repo = PizzariaRepositoryMock()
    usecase = UpdateOrderUsecase(repo)
    controller = UpdateOrderController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.body)
    
    
    return httpResponse.toDict()