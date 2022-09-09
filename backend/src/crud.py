# CRUD do banco de dados da API
# TODO: revisar funções e desmenbrar em funções menores
from src import database, feedz, schemas
from datetime import datetime

# connect to elasticsearch
client = database.Engine()
# timestamp
timestamp = datetime.now()


def create_user(cpf):
    feedz_obj = feedz.get_user(cpf)

    feedz_objdict = models.UserBase(feedz_obj)

    user = {'feedz_id': feedz_objdict.employeeId,
            'employeeId': feedz_objdict.employeeId,
            'name': feedz_objdict.name,
            'email': feedz_objdict.email,
            'cpf': feedz_objdict.cpf,
            'department': feedz_objdict.department,
            }
    try:
        res = client.index(index='sandbox-users', id=user['feedz_id'], document=user)
    except Exception as e:
        print(e)
        return e
    return res


# create or update user from Feedz through CPF
def get_user(user_id):
    """
    Get specific user data
    """
    try:
        res = client.get(index='sandbox-users', id=user_id, refresh=True)['_source']
        return res
    except Exception as e:
        print(e)
        return e


# TODO: aplicar loop em todos as funções de get_ALL que armazenam seus dados em ['_source']
def get_users():
    """
    Get data from all users
    """
    res = client.search(index='sandbox-users', query={"match_all": {}}, filter_path="hits.hits._source")
    res = res['hits']['hits']
    lista = []
    for user in res:
        lista.append(user['_source'])
    # print(res)
    return lista


# def update_user(user_id, field, value):
#     """
#     Update user data
#     """
#
#     try:
#         res = client.update(index='sandbox-users', id=user_id, source_includes=field, doc=value)
#     except Exception as e:
#         print(e)
#         return e
#     return res


def delete_user(user_id):
    """
    Delete user data
    """
    try:
        res = client.delete(index='sandbox-users', id=user_id)
    except Exception as e:
        print(e)
        return e
    return res


def create_product(**product_data):
    """
    Create product data
    """
    product = {'product_id': product_data['product_id'],
               'name': product_data['name'],
               'description': product_data['description'],
               'price': product_data['price'],
               'quantity': product_data['quantity'],
               # 'main_picture': product_data['main_picture'],
               }
    try:
        res = client.index(index='sandbox-products', id=product['product_id'], document=product)
    except Exception as e:
        print(e)
        return e
    return res


def update_product(product_id, **product_data):
    """
    Update product data
    """
    product = {'product_id': product_id,
               'name': product_data['name'],
               'description': product_data['description'],
               'price': product_data['price'],
               'quantity': product_data['quantity'],
               # 'main_picture': product_data['main_picture'],
               'last_update': timestamp,
               }
    try:
        res = client.index(index='sandbox-products', body=product)
    except Exception as e:
        print(e)
        return e
    return res


def get_product(product_id):
    """
    Get specific product
    """
    try:
        res = client.get(index='sandbox-products', id=product_id)['_source']
        # print(res)
        return res
    except Exception as e:
        print(e)
        return e


def get_products():
    """
    Get all products
    """
    try:
        res = client.search(index='sandbox-products', query={"match_all": {}}, filter_path="hits.hits._source")
        res = res['hits']['hits']
        lista = []
        for item in res:
            lista.append(item['_source'])
        # print(res)
        return lista
        # print(res)
    except Exception as e:
        print(e)
        return e


def delete_product(product_id):
    """
    Delete product
    """
    try:
        res = client.delete(index='sandbox-products', id=product_id)
    except Exception as e:
        print(e)
        return e
    return res


def get_task(task_id):
    """
    Get task
    """
    try:
        res = client.get(index='sandbox-tasks', id=task_id)
        res = res['_source']
        # print(res)
    except Exception as e:
        print(e)
        return e
    return res


def get_tasks():
    """
    Get all tasks
    """
    try:
        res = client.search(index='sandbox-tasks', query={"match_all": {}}, filter_path="hits.hits._source")
        res = res['hits']['hits']
        lista = []
        for task in res:
            lista.append(task['_source'])
        # print(res)
        return lista
        # print(res)
    except Exception as e:
        print(e)
        return e


def create_task(**task_data):
    """
    Create task
    """
    task = {'task_id': task_data['task_id'],
            'name': task_data['name'],
            'description': task_data['description'],
            'type': task_data['type'],
            'value': task_data['value'],
            'time': task_data['time'],
            'prof': task_data['prof'],
            }
    try:
        res = client.index(index='sandbox-tasks', id=task['task_id'], document=task)
    except Exception as e:
        print(e)
        return e
    return res


def update_task(task_id, **task_data):
    """
    Update task
    """
    task = {'task_id': task_id,
            'name': task_data['name'],
            'description': task_data['description'],
            'type': task_data['type'],
            'value': task_data['value'],
            'time': task_data['time'],
            'prof': task_data['prof'],
            }
    try:
        res = client.index(index='sandbox-tasks', document=task)
    except Exception as e:
        print(e)
        return e
    return res


def delete_task(task_id):
    """
    Delete task
    """
    try:
        res = client.delete(index='sandbox-tasks', id=task_id)
    except Exception as e:
        print(e)
        return e
    return res


if __name__ == '__main__':
    # create_user('07119811169')
    # update_user(148748, ['balance'], 1000)
    # create_user(44469900206)
    # print(feedz.getUserBalance(148748))
    # print('get user')
    # print(get_user(148734))
    print(get_users())
    # print('user obj')
    # print(UserObject(148734))
# print('Hello World!')
#     print(get_product('99'))
# print(get_products())
# print(get_tasks())
# print(create_user(49498301808))
