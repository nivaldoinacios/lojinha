from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

load_dotenv()

CLOUD_ID = os.getenv('CLOUD_ID')
PASSWORD = os.getenv('PASSWORD')


# TODO: make use to internal interface
def connect_elastic():
    """
    Connect to Elasticsearch
    """
    es = Elasticsearch(cloud_id=CLOUD_ID,
                       basic_auth=('rooststore', PASSWORD))
    return es


# TODO: make user to api.
def Engine():
    """
    Connect to Elasticsearch
    """
    es = Elasticsearch(cloud_id=CLOUD_ID,
                       basic_auth=('rooststore', PASSWORD))
    return es


if __name__ == '__main__':
    client = connect_elastic()
    print(client.info())
