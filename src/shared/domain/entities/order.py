import abc
from src.shared.helpers.errors.domain_errors import EntityError

from src.shared.domain.entities.pizza import Pizza

class Order(abc.ABC):
    pizza: Pizza
    table: int

    def __init__(self, pizza: Pizza, table: int):
        if(pizza == None and type(pizza) != Pizza):
            raise EntityError('pizza')
        self.pizza = pizza

        if(table == None and type(table) != int):
            raise EntityError('table')
        self.table = table