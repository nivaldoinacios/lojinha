# Cria e mapeia os indexes do banco de dados
from backend.src import database, feedz, models

# connect to elasticsearch
client = database.Engine()


def mapping_user():
    """
    Create index
    """
    # index users
    try:
        client.indices.create(
            index='sandbox-users',
            mappings={
                "properties": {
                    "feedz_id": {
                        "type": "long"
                    },
                    "name": {
                        "type": "keyword"
                    },
                    "email": {
                        "type": "text"
                    },
                    "cpf": {
                        "type": "long"
                    },
                    "department": {
                        "type": "keyword"
                    },
                    "access_type": {
                        "type": "keyword"
                    },
                    "orders": {
                        "type": "nested"
                    },
                    "transactions": {
                        "type": "nested"
                    },
                }
            })
    except Exception:
        print(repr(Exception))

    res_users = client.search(
        index='sandbox-users',
        query={"match_all": {}})

    return print(f'{res_users}')


def mapping_product():
    """
    Create index
    """
    # index products
    try:
        client.indices.create(
            index='sandbox-products',
            mappings={
                "properties": {
                    "product_id": {
                        "type": "long"
                    },
                    "name": {
                        "type": "text"
                    },
                    "description": {
                        "type": "text"
                    },
                    "main_picture": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword"
                            }
                        }
                    },
                    "price": {
                        "type": "long"
                    },
                    "quantity": {
                        "type": "long"
                    },
                    "last_update": {
                        "type": "date"
                    },
                }
            }, )
    except Exception:
        print(repr(Exception))

    res_products = client.search(index='sandbox-products',
                                 query={"match_all": {}})

    return print(f'{res_products}')


def mapping_order():
    """
    Create index
    """
    # index orders
    try:
        client.indices.create(
            index='sandbox-orders',
            mappings={
                "properties": {
                    "order_id": {
                        "type": "long"
                    },
                    "user_id": {
                        "type": "long"
                    },
                    "total": {
                        "type": "long"
                    },
                    "details": {
                        "type": "nested"
                    },
                    "created_at": {
                        "type": "date"
                    },
                    "status": {
                        "type": "keyword"
                    },
                    "verified_by": {
                        "type": "long"
                    },
                    "last_update": {
                        "type": "date"
                    },
                }
            }, )
    except Exception:
        print(repr(Exception))

    res_orders = client.search(index='sandbox-orders',
                               query={"match_all": {}})

    return print(f'{res_orders}')


def mapping_transaction():
    """
    Create index
    """
    # index transactions
    try:
        client.indices.create(
            index='sandbox-transactions',
            mappings={
                "properties": {
                    "transaction_id": {
                        "type": "long"
                    },
                    "transaction_type": {
                        "type": "long"
                    },
                    "user_id": {
                        "type": "long"
                    },
                    "created_at": {
                        "type": "date"
                    },
                    "status": {
                        "type": "keyword"
                    },
                    "verified_by": {
                        "type": "long"
                    },
                    "last_update": {
                        "type": "date"
                    },
                    "description": {
                        "type": "nested"
                    },
                }
            }, )

    except Exception:
        print(repr(Exception))

    res_transactions = client.search(index='sandbox-transactions',
                                     query={"match_all": {}})
    return print(f'{res_transactions}')


def mapping_task():
    """
    Create index
    """
    # index tasks
    try:
        client.indices.create(
            index='sandbox-tasks',
            mappings={
                "properties": {
                    "task_id": {
                        "type": "long"
                    },
                    "name": {
                        "type": "text"
                    },
                    "description": {
                        "type": "text"
                    },
                    "type": {
                        "type": "keyword"
                    },
                    "value": {
                        "type": "long"
                    },
                    "time": {
                        "type": "long"
                    },
                    "prof": {
                        "type": "text"
                    },
                }
            }, )
    except Exception:
        print(repr(Exception))

    res_tasks = client.search(index='sandbox-tasks',
                              query={"match_all": {}})
    return print(f'{res_tasks}')


# TODO: add attributes to mapping like: created_at, last_update, access_type, etc
def ingest_users():
    # users data from feedz
    feedz_body = feedz.get_user_list()['data']

    # ingest users data to elasticsearch
    for obj in feedz_body:

        feedz_objdict = models.UserBase(**obj)

        user = {'feedz_id': feedz_objdict.employeeId,
                'employeeId': feedz_objdict.employeeId,
                'name': feedz_objdict.name,
                'email': feedz_objdict.email,
                'cpf': feedz_objdict.cpf,
                'department': feedz_objdict.department,
                }

        if user['cpf'] is None:
            pass
        else:
            user['cpf'] = int(user['cpf'])
            client.index(index='sandbox-users', id=user['feedz_id'], document=user)

    # Search data
    res = client.search(index='sandbox-users', query={"match_all": {}})

    # print(res)

    return print(res['hits']['hits'])


if __name__ == '__main__':
    mapping_user()
    mapping_product()
    mapping_order()
    mapping_transaction()
    mapping_task()
    ingest_users()
    print('Done')
