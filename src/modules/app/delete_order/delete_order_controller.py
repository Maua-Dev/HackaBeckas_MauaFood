from .delete_order_usecase import DeleteOrderUseCase
from .delete_order_viewmodel import DeleteOrderViewModel
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound


class DeleteOrderController:
    def __init__(self, usecase: DeleteOrderUseCase):
        self.deleteOrderUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.body.get('id') is None:
                raise MissingParameters('id')

            if not request.body["id"].isdecimal():
                raise EntityError('id')

            order = self.deleteOrderUsecase(id=int(request.body.get("id")))
            viewmodel = DeleteOrderViewModel(order=order)
            return OK(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])