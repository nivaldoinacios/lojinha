""" Load .env file """
from dotenv import load_dotenv
import requests
import os

load_dotenv()

# API access Token and headers for the request
token = os.getenv('FEEDZ_TOKEN')
headers = {
    'Authorization': 'Bearer ' + token,
    'accept': 'application/json'
}

basicUrl = 'https://sandbox.feedz.com.br/v2/integracao'


# request for update or add data to user
def put(url, data):
    """
    :param url: url called
    :param data: data to be sent
    :return: response from the server
    """
    return requests.request("PUT", basicUrl + url, headers=headers, data=data).json()


# request for get data from API
def get(url, params=None):
    """
    :param url: url called
    :param params: params to be sent
    :return: response from the server
    """

    if params is None:
        params = {}
    return requests.get(basicUrl + url, headers=headers, params=params).json()


# request for get user's data from API
def request_user(user_cpf=None):
    """
    :param user_cpf: cpf of the user
    :return: response from the server
    """
    if user_cpf is None:
        response = get('/employees')
        return response
    else:
        user_cpf = str(user_cpf)
        response = get('/employees', {'cpf': user_cpf})
        return response


# request for get user wallet (user id, cpf, email and balance) from api
def get_user(cpf):
    array = request_user(cpf)['data']
    obj = array[0]
    del obj['description'], obj['remuneration'], obj['admission_at'], obj['birth_at'], obj['situation'], obj['manager'], obj['race'], obj['gender'], obj['status'], obj['company'], obj['company_data'], obj['branch'], obj['department_data'], obj['job_description'], obj['direct_manager'], obj['role']
    return obj


def request_user_wallet(employee_id):
    """
    :param employee_id: id of the user
    :return: response from the server
    """
    return get('/employees/' + str(employee_id) + '/feedzcoins')


def get_user_wallet(employee_id):
    if employee_id is None:
        return print('Error: employee_id is None\n'
                     'Please, inform the employee_id')
    else:
        wallet = request_user_wallet(employee_id)['data']
        return wallet
# request for update user balance from API


def get_wallet_balance(employee_id):
    if employee_id is None:
        return print('Error: employee_id is None\n'
                     'Please, inform the employee_id')
    else:
        wallet = get_user_wallet(employee_id)
        obj = wallet['feedzcoins']
        return obj


def update_coins(employee_id, user_cpf, user_email, roostcoins):
    """
    :param employee_id: id of the user
    :param user_cpf: cpf of the user
    :param user_email: email of the user
    :param roostcoins: amount of roostcoins to be deposited
    :return: response from the server
    """

    payload = {
        "cpf": str(user_cpf),
        "email": user_email,
        "feedzcoins": roostcoins,
    }

    return put('/employees/' + str(employee_id) + '/feedzcoins', payload)


if __name__ == '__main__':
    print(request_user())
    # print('\n')

# dados para teste; id do usuário e cpf
# 148741 / 148748
# 61003930930
