from urllib.request import urlopen
from bs4 import BeautifulSoup


def usd_parser():
    url = 'https://www.tinkoff.ru/invest/currencies/USDRUB/'
    html = urlopen(url)
    bs0 = BeautifulSoup(html, 'html.parser')
    usd = bs0.findAll('text',
                   attrs={'class': "RightPanel__svgInfoPanelContainer_wTVlj"})
    return usd


if __name__ == "__main__":
    print(usd_parser())
