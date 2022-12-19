import abc
from src.shared.helpers.errors.domain_errors import EntityError

from src.shared.domain.entities.pizza import Pizza

class Order(abc.ABC):
    id: int
    pizza: Pizza
    table: int

    def __init__(self, id: int, pizza: Pizza, table: int):
        if(id == None and type(id) != int and id <= 0):
            raise EntityError('id')
        self.id = id

        if(pizza == None and type(pizza) != Pizza):
            raise EntityError('pizza')
        self.pizza = pizza

        if(table == None and type(table) != int and table <= 0):
            raise EntityError('table')
        self.table = table