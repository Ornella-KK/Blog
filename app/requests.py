from app import app

# Getting the movie base url
base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTES_API_BASE_URL']

def get_quotes():
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = base_url

    with urllib.request.urlopen(get_quotes_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        quote_results = None
        quote_results_list = get_quotes_response['results']
        quote_results = process_results(quote_results_list)


    return quote_results

def process_results(quote_list):
    '''
    Function  that processes the quote result and transform them to a list of Objects

    Args:
        quote_list: A list of dictionaries that contain quote details

    Returns :
        quote_results: A list of quote objects
    '''
    quote_results = []
    for quote_item in quote_list:
        author = quote_item.get('author')
        quote = quote_item.get('quote')

        if author:
            quote_object = Quote(author,quote)
            quote_results.append(quote_object)

    return quote_results
