# Generated by Django 3.1 on 2022-10-27 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20221027_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]