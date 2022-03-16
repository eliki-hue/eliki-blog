
import urllib.request,json
from .models import Quotes

# base_url = 'http://quotes.stormconsultancy.co.uk/random.json'

def get_quotes():
    quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(quote_url) as url:
        quote_data = url.read()
        quote_data_response = json.loads(quote_data)

        if quote_data_response:
            author = quote_data_response.get('author')
            quote = quote_data_response.get('quote')

            quote_object = Quotes(author, quote)
    return quote_object
