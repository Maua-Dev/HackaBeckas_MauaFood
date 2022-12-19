from src.modules.app.get_order.get_order_controller import GetOrderController
from src.modules.app.get_order.get_order_usecase import GetOrderUsecase
from src.shared.helpers.http.http_lambda_requests import LambdaHttpResponse, LambdaHttpRequest
from src.shared.infra.repositories.pizzaria_repository_mock import PizzariaRepositoryMock

def lambda_handler(event, context):
    repo = PizzariaRepositoryMock()
    usecase = GetOrderUsecase(repo)
    controller = GetOrderController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.body)
    
    
    return httpResponse.toDict()
