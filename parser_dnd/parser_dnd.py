from urllib.request import urlopen
from bs4 import BeautifulSoup
import pprint
import re
from time import sleep


def dnd_spell_parser():
    start = 0
    spell_id = {}
    total = {}
    mysityurl = 'https://dnd.su/spells/'
    html = urlopen(mysityurl)
    bs0 = BeautifulSoup(html, 'html.parser', )
    spells = bs0.findAll('li', attrs={'class': "for_filter"})
    for data in spells:
        name_and_link = data.find('a')
        spell_id.update({'link': name_and_link.get('href')})
        l = name_and_link.get('href')
        spell_id.update({'name': name_and_link.get('title')})
        next_link(l, spell_id)
        total.update({start: spell_id})
        spell_id = {}
        start += 1
        pprint.pprint(total)
        sleep(5)
    return


def next_link(link, spell_id):
    url = 'https://dnd.su' + link
    html = urlopen(url)
    bs0 = BeautifulSoup(html, 'html.parser')
    info = bs0.find('ul', attrs={'class': "params"})
    all_li = info.find_all("li")
    for l in all_li:
        bufer = l.getText().split(':')
        if bufer[0][:1].isdigit():
            i = bufer[0].split(',')
            spell_id.update({'lvl': i[0].strip()})
            spell_id.update({'school': i[1].strip()})
        if bufer[0] == 'Время накладывания':
            spell_id.update({bufer[0]: bufer[1].strip()})
        if bufer[0] == 'Дистанция':
            spell_id.update({bufer[0]: bufer[1].strip()})
        if bufer[0] == 'Компоненты':
            spell_id.update({bufer[0]: bufer[1].strip()})
        if bufer[0] == 'Длительность':
            spell_id.update({bufer[0]: bufer[1].strip()})
        if bufer[0] == 'Классы':
            spell_id.update({bufer[0]: bufer[1].strip()})
        if bufer[0] == 'Архетипы':
            spell_id.update({bufer[0]: bufer[1].strip()})
        if bufer[0] == 'Источник':
            spell_id.update({bufer[0]: bufer[1].strip()})
        else:
            spell_id.update({'Описание': re.sub('[\t\r\n]', '', str(bufer[0]))})

    return spell_id


dnd_spell_parser()
