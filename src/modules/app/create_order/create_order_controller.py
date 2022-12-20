from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.enums.stuffed_edge_enum import STUFFED_EDGE
from .create_order_usecase import CreateOrderUsecase
from .create_order_viewmodel import CreateOrderViewModel
from src.shared.helpers.http.http_models import BadRequest, Created, HttpRequest, HttpResponse, InternalServerError
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.domain.enums.flavor_enum import FLAVOR
# from src.shared.domain.enums.price_enum import PRICE



class CreateOrderController:
    def __init__(self, usecase: CreateOrderUsecase):
        self.createOrderUsecase = usecase
    
    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.body.get("table") is None:
                raise MissingParameters('table')
            
            if request.body.get("flavor") is None:
                raise MissingParameters('flavor')

            if request.body.get("stuffed_edge") is None:
                raise MissingParameters('stuffed_edge')

            if not request.body["table"].isdecimal():
                raise EntityError('table')

            if request.body["id"] is None:
                raise EntityError('id')
            
            if not request.body["id"].isdecimal():
                raise EntityError('id')

            if request.body["state"] is None:
                raise EntityError('state')
            
            # if not request.body["price"].isdecimal():
            #     raise EntityError("price")
            
            flavors = list()
            for item in FLAVOR:
                flavors.append(item.value[0])

            edges = list()
            for item in STUFFED_EDGE:
                edges.append(item.value[0])

            states = list()
            for item in STATE:
                states.append(item.value)

            # prices = list()
            # for item in FLAVOR.value[1]:
            #     prices.append(item.value())

            if request.body["flavor"] not in flavors:
                raise EntityError("flavor")

            if request.body["stuffed_edge"] not in edges:
                raise EntityError("stuffed_edge")

            if request.body["state"] not in states:
                raise EntityError("state")
            
            # if request.body["price"] not in prices:
            #     raise EntityError("price")

            order = self.createOrderUsecase(id=int(request.body["id"]), table=int(request.body["table"]),flavor=FLAVOR[request.body["flavor"]],stuffed_edge=STUFFED_EDGE[request.body["stuffed_edge"]], state=STATE[request.body["state"]])
            viewmodel = CreateOrderViewModel(order=order)
            return Created(viewmodel.to_dict())
            
        except EntityError as err:
            return BadRequest(body=err.message)
            
        except MissingParameters as err:
            return BadRequest(body=err.message)    
            
        except Exception as err:
            return InternalServerError(body=err.args[0])