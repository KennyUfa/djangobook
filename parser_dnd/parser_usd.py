from urllib.request import urlopen
from bs4 import BeautifulSoup


def usd_parser():
    url = 'https://quote.rbc.ru/ticker/59111'
    html = urlopen(url)
    bs0 = BeautifulSoup(html, 'html.parser', )
    usd = bs0.find('span', attrs={'class': "chart__info__sum"})
    return usd.text

