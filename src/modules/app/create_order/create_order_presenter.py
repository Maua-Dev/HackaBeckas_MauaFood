from src.shared.helpers.http.http_lambda_requests import LambdaHttpResponse, LambdaHttpRequest
from .create_order_controller import CreateOrderController
from .create_order_usecase import CreateOrderUsecase
from src.shared.infra.repositories.pizzaria_repository_mock import PizzariaRepositoryMock

def lambda_handler(event, context):
    repo = PizzariaRepositoryMock()
    usecase = CreateOrderUsecase(repo)
    controller = CreateOrderController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.body)
    
    
    return httpResponse.toDict()
