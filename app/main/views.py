from app import app
from flask import render_template
from app.requests import get_quotes

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    all_quotes = get_quotes()
    title = 'Personal Blog'
    return render_template('index.html', title = title,quote = all_quotes)