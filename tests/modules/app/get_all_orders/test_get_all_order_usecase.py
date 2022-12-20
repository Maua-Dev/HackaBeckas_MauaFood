from src.modules.app.get_all_orders.get_all_order_usecase import GetAllOrderUsecase
from src.shared.infra.repositories.pizzaria_repository_mock import PizzariaRepositoryMock


class Test_GetAllOrderUsecase:
    def test_get_all_selfies(self):
        repo = PizzariaRepositoryMock()
        usecase = GetAllOrderUsecase(repo=repo)
       
        all_orders = usecase()
       
        assert all_orders == repo.orders