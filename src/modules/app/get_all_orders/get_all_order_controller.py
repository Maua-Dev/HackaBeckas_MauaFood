from src.modules.app.get_all_orders.get_all_order_usecase import GetAllOrderUsecase
from src.modules.app.get_all_orders.get_all_order_viewmodel import GetAllOrderViewmodel
from src.shared.helpers.http.http_models import OK, HttpRequest, HttpResponse


class GetAllOrderController:
    def __init__(self, usecase: GetAllOrderUsecase):
        self.getAllOrderUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:           
        all_orders = self.getAllOrderUsecase()
        viewmodel = GetAllOrderViewmodel(all_orders)
        return OK(viewmodel.to_dict())