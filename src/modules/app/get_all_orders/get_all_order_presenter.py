from .get_all_order_controller import GetAllOrderController
from src.shared.helpers.http.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.shared.infra.repositories.pizzaria_repository_mock import PizzariaRepositoryMock
from .get_all_order_usecase import GetAllOrderUsecase


def lambda_handler(event, context):
    repo = PizzariaRepositoryMock()
    usecase = GetAllOrderUsecase(repo)
    controller = GetAllOrderController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.body)
    
    
    return httpResponse.toDict()