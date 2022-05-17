from urllib.request import urlopen
from bs4 import BeautifulSoup


def usd_parser():
    url = 'https://www.tinkoff.ru/invest/currencies/USDRUB/'
    html = urlopen(url)
    bs0 = BeautifulSoup(html, 'html.parser')
    usd = bs0.find('span',
                   attrs={'class': "SecurityInvitingScreen__priceValue_c1Ah9"})
    return usd.get_text()


if __name__ == "__main__":
    usd_parser()
