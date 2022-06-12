# Generated by Django 4.0.4 on 2022-06-09 23:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_closet_onepiece_url_closet_onepiece_closet_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='closet_outer',
            name='author',
        ),
        migrations.RemoveField(
            model_name='closet_pants',
            name='author',
        ),
        migrations.RemoveField(
            model_name='closet_top',
            name='author',
        ),
        migrations.AddField(
            model_name='closet',
            name='closet_color',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='closet',
            name='closet_fall',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='closet',
            name='closet_fit',
            field=models.IntegerField(default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='closet',
            name='closet_spring',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='closet',
            name='closet_style',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='closet',
            name='closet_summer',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='closet',
            name='closet_winter',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='closet',
            name='onepiece',
            field=models.TextField(choices=[(1, 'onepiece'), (2, 'twopiece')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='closet',
            name='outer',
            field=models.TextField(choices=[(1, 'Coat'), (2, 'Jacket'), (3, 'Jumper'), (4, 'Padding'), (5, 'Best'), (6, 'Cardigan '), (7, 'Zip-Up')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='closet',
            name='pants',
            field=models.TextField(choices=[(1, 'Blue jeans'), (2, 'Pants'), (3, 'Skirt'), (4, 'Leggings'), (5, 'Jogger pants')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='closet',
            name='section',
            field=models.TextField(choices=[(1, 'Top'), (2, 'Pants'), (3, 'Outer'), (4, 'Onepiece')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='closet',
            name='top',
            field=models.TextField(choices=[(1, 'Blouse'), (2, 'T-shirt'), (3, 'Knit'), (4, 'Hoodie')], default='', max_length=20),
        ),
        migrations.DeleteModel(
            name='Closet_onepiece',
        ),
        migrations.DeleteModel(
            name='Closet_outer',
        ),
        migrations.DeleteModel(
            name='Closet_pants',
        ),
        migrations.DeleteModel(
            name='Closet_top',
        ),
    ]
