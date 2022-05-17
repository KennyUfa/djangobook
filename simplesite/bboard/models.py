from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']


class DndSpell(models.Model):
    # ['link', 'name', 'lvl', 'school', 'Время накладывания', 'Дистанция', 'Компоненты', 'Длительность',
    # 'Классы', 'Архетипы', 'Источник', 'Описание']
    link = models.CharField(max_length=50, verbose_name='ссылка')
    name = models.CharField(max_length=50, verbose_name='название')
    lvl = models.IntegerField(verbose_name='уровень')
    school = models.CharField(max_length=50, verbose_name='школа')
    time_cast = models.CharField(max_length=100, verbose_name='время накладывания')
    distance = models.CharField(max_length=50, verbose_name='дистанция')
    components = models.CharField(max_length=100, verbose_name='компоненты')
    timing = models.CharField(max_length=100, verbose_name='Длительность')
    class_actor = models.CharField(max_length=100, verbose_name='Классы')
    arhitype = models.CharField(max_length=100, verbose_name='Архетипы')
    origin = models.CharField(max_length=100, verbose_name='источник')
    instruction = models.CharField(max_length=100, verbose_name='описание')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Заклинания'
        verbose_name = 'Заклинание'


class Roll(models.Model):
    d_amount = models.IntegerField()
    d_type = models.IntegerField()
    dmg_result = models.IntegerField()
