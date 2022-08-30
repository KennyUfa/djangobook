from django.db import models


# Create your models here.
class DndSpell(models.Model):
    link = models.CharField(max_length=100, verbose_name='ссылка')
    name = models.CharField(max_length=100, verbose_name='название')
    lvl = models.CharField(max_length=15, verbose_name='уровень')
    school = models.CharField(max_length=60, verbose_name='школа')
    time_cast = models.CharField(max_length=200,
                                 verbose_name='время накладывания')
    distance = models.CharField(max_length=100, verbose_name='дистанция')
    components = models.CharField(max_length=400, verbose_name='компоненты')
    timing = models.CharField(max_length=100, verbose_name='Длительность')
    class_actor = models.CharField(max_length=150, verbose_name='Классы',
                                   blank=True, null=True)
    architype = models.CharField(max_length=200, verbose_name='Архетипы',
                                 blank=True, null=True)
    origin = models.CharField(blank=True, null=True, max_length=100,
                              verbose_name='источник')
    instruction = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Заклинания'
        verbose_name = 'Заклинание'

