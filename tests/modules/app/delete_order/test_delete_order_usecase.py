
from src.modules.app.delete_order.delete_order_usecase import DeleteOrderUseCase
from src.shared.domain.entities.order import Order
from src.shared.domain.entities.pizza import Pizza
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.enums.stuffed_edge_enum import STUFFED_EDGE
from src.shared.infra.repositories.pizzaria_repository_mock import PizzariaRepositoryMock


class Test_CreateOrderUsecase:
    def test_delete_order_usecase(self):
        repo = PizzariaRepositoryMock()
        usecase = DeleteOrderUseCase(repo=repo)
        
        lenBefore = len(repo.orders)

        deletedOrder = repo.orders[0]
        
        order = usecase(id=1)

        # deletedOrder = Order(
        #         id = 1,
        #         pizza = Pizza(flavor=FLAVOR.BACON, stuffed_edge=STUFFED_EDGE.CHEDDAR),
        #         table = 1
        #     )
        
        assert len(repo.orders) == lenBefore - 1
        assert [order.id, order.pizza, order.table] == [deletedOrder.id, deletedOrder.pizza, deletedOrder.table]

    def __repr__(self):
        return f'repo={PizzariaRepositoryMock}'