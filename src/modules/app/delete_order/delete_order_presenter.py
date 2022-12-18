from src.shared.helpers.http.http_lambda_requests import LambdaHttpResponse, LambdaHttpRequest
from .delete_order_controller import DeleteOrderController
from .delete_order_usecase import DeleteOrderUseCase
from src.shared.infra.repositories.pizzaria_repository_mock import PizzariaRepositoryMock

def lambda_handler(event, context):
    repo = PizzariaRepositoryMock()
    usecase = DeleteOrderUseCase(repo)
    controller = DeleteOrderController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.body)
    
    
    return httpResponse.toDict()
