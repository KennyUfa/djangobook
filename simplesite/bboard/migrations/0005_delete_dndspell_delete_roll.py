# Generated by Django 4.0.3 on 2022-05-19 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0004_roll'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DndSpell',
        ),
        migrations.DeleteModel(
            name='Roll',
        ),
    ]