from .create_order_usecase import CreateOrderUsecase
from .create_order_viewmodel import CreateOrderViewModel
from src.shared.helpers.http.http_models import BadRequest, Created, HttpRequest, HttpResponse, InternalServerError
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.enums.price_enum import PRICE



class CreateOrderController:
    def __init__(self, usecase: CreateOrderUsecase):
        self.createOrderUsecase = usecase
    
    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.body.get("table") is None:
                raise MissingParameters('table')
            
            if request.body.get('flavor') is None:
                raise MissingParameters('flavor')

            if request.body.get('price') is None:
                raise MissingParameters('price')

            if not request.body["table"].isdecimal():
                raise EntityError("table")
            
            # if not request.body["price"].isdecimal():
            #     raise EntityError("price")
            
            flavors = list()
            for item in FLAVOR:
                flavors.append(item.value)

            prices = list()
            for item in PRICE:
                prices.append(item.value)

            if request.body["flavor"] not in flavors:
                raise EntityError("flavor")
            
            if request.body["price"] not in prices:
                raise EntityError("price")

            order = self.createOrderUsecase(table=int(request.body["table"]),flavor=FLAVOR[request.body["flavor"]],price=PRICE[request.body["price"]])
            viewmodel = CreateOrderViewModel(order=order)

            return Created(viewmodel.to_dict())
            
        except EntityError as err:
            return BadRequest(body=err.message)
            
        except MissingParameters as err:
            return BadRequest(body=err.message)    
            
        except Exception as err:
            return InternalServerError(body=err.args[0])