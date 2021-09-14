import requests
from bs4 import BeautifulSoup


def CallWeatherApi():

    uri = f'''
    https://search.naver.com/search.naver?where=nexearch&sm=top_sly.hst&fbm=1&acr=1&ie=utf8&query=%EB%82%A0%EC%94%A8
    '''
    response = requests.get(uri)

    soup = BeautifulSoup(response.text, 'html.parser')

    target = soup.select_one("#main_pack .todaytemp")

    weather = target.text
    weatherDict = {"temp": weather}

    return weatherDict
