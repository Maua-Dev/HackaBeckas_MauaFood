from src.modules.app.get_order.get_order_usecase import GetOrderUsecase
from src.modules.app.get_order.get_order_viewmodel import GetOrderViewmodel
from src.shared.domain.entities.order import Order
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound


class GetOrderController:
    def __init__(self, usecase: GetOrderUsecase):
        self.getOrderUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.query_params.get('id') is None:
                raise MissingParameters('id')

            if not request.query_params["id"].isdecimal():
                raise EntityError('id')

            order = self.getOrderUsecase(id=int(request.query_params.get("id")))
            viewmodel = GetOrderViewmodel(order)
            return OK(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])