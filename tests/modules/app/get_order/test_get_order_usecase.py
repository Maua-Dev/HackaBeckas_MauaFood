from src.modules.app.get_order.get_order_usecase import GetOrderUsecase
from src.shared.infra.repositories.pizzaria_repository_mock import PizzariaRepositoryMock


class Test_GetOrderUsecase:
    def test_get_order_usecase(self):
        repo = PizzariaRepositoryMock()
        usecase = GetOrderUsecase(repo=repo)

        getOrder = repo.orders[0]

        order = usecase(id=1)

        assert [order.id, order.pizza, order.table, order.pizza.price, order.state] == [getOrder.id, getOrder.pizza, getOrder.table, getOrder.pizza.price, getOrder.state]