import urllib.request, json
from .models import Quote
from config import Config
import requests

quote_url = Config.QUOTE_API_BASE_URL
    
def getQuotes():
    '''
    function that gets the json response  quotes to our url request
    '''
    quote=requests.get(quote_url)
    new_quote = quote.json()
    author = new_quote.get('author')
    quote = new_quote.get('quote')
    quote_result = Quote(author, quote)
        
    return quote_result     