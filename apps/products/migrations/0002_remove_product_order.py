# Generated by Django 3.1 on 2022-10-27 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='order',
        ),
    ]