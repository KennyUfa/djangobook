# Generated by Django 4.0.3 on 2022-05-17 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_dndspell'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_amount', models.IntegerField()),
                ('d_type', models.IntegerField()),
                ('attack_bonus', models.IntegerField()),
                ('dmg_bonus', models.IntegerField()),
                ('advatage_bonus', models.BooleanField(blank=True)),
                ('critic_bonus', models.BooleanField(blank=True)),
                ('attack_result', models.IntegerField()),
                ('dmg_result', models.IntegerField()),
            ],
        ),
    ]
