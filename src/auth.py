from polygon import RESTClient
from dotenv import load_dotenv
from os import getenv

def auth():
    load_dotenv()
    api_key = getenv('POLYGON_API_KEY')
    return RESTClient(api_key=api_key)