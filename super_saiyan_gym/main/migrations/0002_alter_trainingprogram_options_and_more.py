# Generated by Django 4.1 on 2022-08-24 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trainingprogram',
            options={'ordering': ['prise'], 'verbose_name': 'Тренировочная программа', 'verbose_name_plural': 'Программы тренировок'},
        ),
        migrations.AddField(
            model_name='trainingprogram',
            name='training_count',
            field=models.IntegerField(default=8, verbose_name='Количество занятий'),
        ),
    ]
