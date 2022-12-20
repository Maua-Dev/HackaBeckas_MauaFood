from src.modules.app.update_order.update_order_usecase import UpdateOrderUsecase
from src.modules.app.update_order.update_order_viewmodel import UpdateOrderViewmodel
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.enums.stuffed_edge_enum import STUFFED_EDGE
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound
from src.shared.helpers.http.http_models import OK, BadRequest, Conflict, HttpRequest, HttpResponse, InternalServerError, NotFound



class UpdateOrderController:
    def __init__(self, usecase: UpdateOrderUsecase):
        self.updateOrderUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.body.get("id") is None:
                raise MissingParameters('id')

            if request.body.get("new_flavor") is None:
                raise MissingParameters('new_flavor')

            if request.body.get("new_stuffed_edge") is None:
                raise MissingParameters('new_stuffed_edge')

            if request.body.get("new_state") is None:
                raise MissingParameters('new_state')

            if not request.body["id"].isdecimal():
                raise EntityError('id')
            
            order = self.updateOrderUsecase(id=int(request.body.get("id")),new_flavor=FLAVOR[request.body["new_flavor"]],new_stuffed_edge=STUFFED_EDGE[request.body["new_stuffed_edge"]], new_state=STATE[request.body["new_state"]])
            viewmodel = UpdateOrderViewmodel(order)
            return OK(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except DuplicatedItem as err:
            return Conflict(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
