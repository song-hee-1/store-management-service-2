# Generated by Django 3.1 on 2022-10-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='상품가격'),
        ),
    ]
