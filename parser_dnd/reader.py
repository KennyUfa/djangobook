import csv

# with open('spells.csv', newline='') as csvfile:
#
#     reader = csv.reader(csvfile)
#     mydict = dict(reader)
x = {'link': '/spells/1-hellish_rebuke/', 'name': 'Адское возмездие [Hellish rebuke]', 'lvl': '1 уровень', 'school': 'воплощение', 'Время накладывания': '1 реакция, совершаемая вами вы получаете урон от существа, находящегося в пределах 60 футов от вас и видимого вами', 'Дистанция': '60 футов', 'Компоненты': 'В, С', 'Длительность': 'Мгновенная', 'Классы': 'колдун', 'Архетипы': 'клятвопреступник (паладин)', 'Источник': "«Player's handbook»", 'Описание': 'Вы указываете пальцем, и существо, причинившее вам урон, мгновенно окружается пламенем. Существо должно совершить спасбросок Ловкости. Оно получает урон огнём 2к10 при провале, или половину этого урона при успехе.На больших уровнях. Если вы накладываете это заклинание, используя ячейку 2-го уровня или выше, урон увеличивается на 1к10 за каждый уровень ячейки выше первого.'}

y = {}
y.setdefault('name',x.get('name'))
print(x.keys())