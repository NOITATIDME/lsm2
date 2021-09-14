import requests
from bs4 import BeautifulSoup


def CallMovieApi(page=1):

    list = []

    url = f'''
    https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number={page}&limit=20
    '''
    response = requests.get(url)
    responseDict = response.json()
    movies = responseDict["data"]["movies"]

    return movies
