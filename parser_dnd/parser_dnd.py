from urllib.request import urlopen
from bs4 import BeautifulSoup

component = []
name = []
link = ['/spells/1-hellish_rebuke/']

def dnd_spell_parser():
    mysityurl = 'https://dnd.su/spells/'
    html = urlopen(mysityurl)
    bs0 = BeautifulSoup(html, 'html.parser', )
    spells = bs0.findAll('li', attrs={'class': "for_filter"})
    for data in spells:
        components = data.findAll('span', attrs={"class": "end_icon_component"})
        for comp in components:
            component.append(comp.get('title'))
        name_and_link = data.find('a')
        link.append(name_and_link.get('href'))
        name.append(name_and_link.get('title'))
        print(link)
        print(name)
        print(component)
        return

def next_link(link):
    url='https://dnd.su'+link[0]
    html = urlopen(url)
    bs0 = BeautifulSoup(html, 'html.parser')
    info = bs0.find('ul', attrs={'class': "params"})
    for li in info.find_all("li"):
        print(li.text, end="\n")

# dnd_spell_parser()
next_link(link)




