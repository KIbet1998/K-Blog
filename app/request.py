from app import app
import urllib.request,json
from .models import Quotes
base_url = None
def configure_request(app):
    global base_url
    base_url = app.config["QUOTES_API_BASE_URL"]
def get_quotes():
    '''
    Function that gets the json response to our url request
    '''
    quotes_list=[]
    get_quotes_url=base_url.format()
    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response=json.loads(get_quotes_data)
        id= str(get_quotes_response['id'])
        quote=str(get_quotes_response['quote'])
        author=str(get_quotes_response['author'])
        new_list=[id,quote,author]
        quotes_list.append(new_list)
    return quotes_list[0]