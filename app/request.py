
import urllib.request,json
from .models import Quotes

# base_url = 'http://quotes.stormconsultancy.co.uk/random.json'

def quote_fetch():
    quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(quote_url) as url:
        quote_data = url.read()
        quote_response = json.loads(quote_data)

        if quote_response:
            author = quote_response.get('author')
            quote = quote_response.get('quote')

            quote_item = Quotes(author, quote)
    return quote_item
