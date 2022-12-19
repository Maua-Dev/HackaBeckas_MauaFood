import pytest
from src.modules.app.update_order.update_order_usecase import UpdateOrderUsecase
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.enums.stuffed_edge_enum import STUFFED_EDGE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.pizzaria_repository_mock import PizzariaRepositoryMock


class Test_UpdateUsecase:
    def test_update_order_usecase(self):
        repo = PizzariaRepositoryMock()
        usecase = UpdateOrderUsecase(repo=repo)

        updatedOrder = (repo.orders[0])

        order = usecase(id=1, new_flavor=FLAVOR.BEEF, new_stuffed_edge=STUFFED_EDGE.RICOTTA)

        assert [order.id, order.pizza.flavor, order.pizza.stuffed_edge] == [updatedOrder.id, updatedOrder.pizza.flavor, updatedOrder.pizza.stuffed_edge]

    def test_update_order_usecase_not_found_id(self):
        repo = PizzariaRepositoryMock()
        usecase = UpdateOrderUsecase(repo=repo)

        with pytest.raises(NoItemsFound):
            usecase(
                id=666,
                new_flavor=FLAVOR.BACON,
                new_stuffed_edge=STUFFED_EDGE.CATUPIRY
            )

    def test_update_order_usecase_invalid_flavor(self):
        repo = PizzariaRepositoryMock()
        usecase = UpdateOrderUsecase(repo=repo)

        with pytest.raises(EntityError):
            usecase(
                id=2,
                new_flavor={},
                new_stuffed_edge=STUFFED_EDGE.CATUPIRY
            )

    def test_update_order_usecase_invalid_stuffed_edge(self):
        repo = PizzariaRepositoryMock()
        usecase = UpdateOrderUsecase(repo=repo)

        with pytest.raises(EntityError):
            usecase(
                id=4,
                new_flavor=FLAVOR.BACON,
                new_stuffed_edge="CATUPIRY"
            )