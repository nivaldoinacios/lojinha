# import src.feedz as feedz
from enum import Enum
import feedz

# TODO: Criar modelos para validação de dados, talvez seja necessário
# renomear o arquivo models.py para schemas.py


class AccessType(str, Enum):
    """ Tipos de acesso do usuário. """
    admin = "admin"
    manager = "manager"
    user = "user"


class Objdict(dict):
    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)


# TODO: function to show history of spends and gains
# TODO: criar modelos para outros objetos do banco de dados elasticsearch
class WalletBase(Objdict):
    def get_balance(self):
        """ Get wallet balance. """
        balance = feedz.get_wallet_balance(self.id)
        return balance

    def update_balance(self, amount):
        feedz.update_coins(self.employeeId, self.cpf, self.email, amount)
        balance = feedz.get_wallet_balance(self.id)
        return balance

    # def __str__(self):
    #     return f"WalletBase({self.id}, {self.cpf}, {self.email}, {self.feedzcoins})"

    # def __repr__(self):
    #     return f"WalletBase({self.id}, {self.cpf}, {self.email}, {self.feedzcoins})"


class UserBase(Objdict):
    def __init__(self, feedz_body):
        super().__init__()
        self.employeeId = feedz_body['employeeId']
        self.feedz_id = self.employeeId
        self.name = feedz_body['name']
        self.email = feedz_body['email']
        self.cpf = feedz_body['cpf']
        self.department = feedz_body['department']
        self.access = AccessType('user')
        self.wallet = WalletBase(feedz.get_user_wallet(self.employeeId))

    def get_wallet(self):
        return self.wallet

    def get_balance(self):
        """ Get wallet balance. """
        balance = feedz.get_wallet_balance(self.employeeId)
        return balance

    def update_balance(self, amount):
        feedz.update_coins(self.employeeId, self.cpf, self.email, amount)
        balance = feedz.get_wallet_balance(self.employeeId)
        return balance

    def get_access(self):
        return self.access

    def get_department(self):
        return self.department

    def get_cpf(self):
        return self.cpf

    def get_email(self):
        return self.email

    def get_name(self):
        return self.name

    def get_id(self):
        return self.employeeId

    # def __str__(self):
        # return f"UserBase({self.feedz_id}, {self.name}, {self.email}, {self.cpf}, {self.department}, {self.access}, {self.wallet})"

    # def __repr__(self):
    #     return f"UserBase({self.feedz_id}, {self.name}, {self.email}, {self.cpf}, {self.department}, {self.access}, {self.wallet})"


class ProductBase(Objdict):
    def __init__(self, feedz_body):
        super().__init__()
        self.id = feedz_body['product_id']
        self.name = feedz_body['name']
        self.description = feedz_body['description']
        self.price = feedz_body['price']
        # self.image = feedz_body['image']

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    # def get_image(self):
    #     return self.image


# def __str__(self):
#     return f"ProductBase({self.id}, {self.name}, {self.description}, {self.price}, {self.category}, {self.image})"

# def __repr__(self):
#     return f"ProductBase({self.id}, {self.name}, {self.description}, {self.price}, {self.category}, {self.image})"

if __name__ == "__main__":

    x = feedz.get_user('44469900206')
    # print(x)
    y = Objdict(x)
    z = UserBase(y)
    print(x)
    print(y)
    print(z)
    # user = UserBase(x)
    # wallet = WalletBase(feedz.get_user_wallet('148742'))
    # print(user)
    # print(wallet)
