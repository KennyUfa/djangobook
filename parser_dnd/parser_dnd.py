from urllib.request import urlopen
from bs4 import BeautifulSoup

filtered = []
hrefval = []


def dnd_spell_parser():
    """

    :param day: день в формате '2020-12-25'
    :return: парсит сайт return {'date': '2020-12-10', 'am_temp': '-21˚', 'pm_temp': '-13˚', 'weather_day': 'Snow'
    """
    mysityurl = f'https://dnd.su/spells/'
    html = urlopen(mysityurl)
    bs0 = BeautifulSoup(html, 'html.parser', )
    spells = bs0.findAll('li', attrs={'class': "for_filter"})
    for data in spells:
        # < a href = "/spells/66-shocking_grasp/" title = "Электрошок [Shocking grasp]" > Электрошок < / a >
        x = data.find('a')

        # ['/spells/1-hellish_rebuke/ - Адское возмездие [Hellish rebuke]',
        # '/spells/2-antipathy_sympathy/ - Антипатия/симпатия [Antipathy/sympathy]',...]
        y = hrefval.append(x.get('href') + ' - ' + x.get('title'))

    for i in hrefval:
        print(i)


dnd_spell_parser()
