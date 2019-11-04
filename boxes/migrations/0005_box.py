# Generated by Django 2.2.5 on 2019-10-31 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxes', '0004_auto_20191029_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(blank=True, upload_to='media/image', verbose_name='Картинка 1')),
                ('image_2', models.ImageField(blank=True, upload_to='media/image', verbose_name='Картинка 2')),
                ('image_3', models.ImageField(blank=True, upload_to='media/image', verbose_name='Картинка 3')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('size', models.CharField(max_length=25, verbose_name='Габариты')),
                ('price_2', models.CharField(max_length=25, verbose_name='Цена от 11 до 50')),
                ('price_1', models.CharField(max_length=25, verbose_name='Цена от 101')),
            ],
            options={
                'verbose_name': 'коробку',
                'verbose_name_plural': 'Коробки',
            },
        ),
    ]