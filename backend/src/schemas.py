from pydantic import BaseModel
from enum import Enum
from typing import Optional, List, Dict

# import feedz
# import models


class AccessType(str, Enum):
    """ Tipos de acesso do usuário. """
    admin = 'admin'
    manager = 'manager'
    user = 'user'


class UserBase(BaseModel):
    """ Modelo de usuário. """
    employeeId: Optional[int]
    # employeeId: int
    name: str
    email: str
    cpf: str or int
    department: Optional[str]
    access_type: Optional[List[AccessType]]
    wallet: Optional[Dict]


if __name__ == '__main__':
    # ordem da chamada de construção do objeto
    x = feedz.get_user(44469900206)
    print(x)
    f = UserBase(**x)
    print(f.dict())
    y = models.Objdict(f)
    print(y)
    z = models.UserCreate(y)
    print(z)

    # user = UserBase(**y)
    # print(user)


#
# class TypeTransaction(str, Enum):
#     """ Tipos de transação. """
#     credit = "credit" == 1
#     debit = "debit" == 2
#
#
# class Transaction(BaseModel):
#     """ Modelo de transação. """
#     id: Optional[UUID] = uuid4()
#     order_by: int
#     approved_by: Optional[int]
#     amount: int
#     type: TypeTransaction
#     date: datetime
#
#     class Config:
#         orm_mode = True
#
#
# class StatusCredit(str, Enum):
#     """ Status do crédito. """
#     pending = "pending"
#     approved = "approved"
#     rejected = "rejected"
#
#
# class Credit(BaseModel):
#     """ Modelo de crédito. """
#     id: Optional[UUID] = uuid4()
#     mineration_tasks_id: int
#     payed_to_id: int
#     amount: int
#     created_date: datetime
#     status: StatusCredit
#     approved_date: datetime
#
#     class Config:
#         orm_mode = True
#
#
# class MinerationTasks(BaseModel):
#     """ Modelo de tarefa de mineração. """
#     id: Optional[UUID] = uuid4()
#     name: str
#     description: str
#     amount: int
#     type: str
#
#     class Config:
#         orm_mode = True
#
#
# class StatusOrder(str, Enum):
#     """ Status do pedido. """
#     pending = "pending"
#     approved = "approved"
#     rejected = "rejected"
#     canceled = "canceled"
#
#
# class Order(BaseModel):
#     """ Modelo de pedido. """
#     id: Optional[UUID] = uuid4()
#     user_id: int
#     order_date: datetime
#     updated_at: datetime
#     status: StatusOrder
#
#     class Config:
#         orm_mode = True
#
#
# class ItemOrder(BaseModel):
#     """ Modelo de itens do pedido. """
#     id: Optional[UUID] = uuid4()
#     order_id: int
#     item_id: int
#     quantity: int
#
#
# class Product(BaseModel):
#     """ Modelo de produto. """
#     id: Optional[UUID] = uuid4()
#     name: str
#     price: int
#     description: str
#     quantity: int
#
#     class Config:
#         orm_mode = True
