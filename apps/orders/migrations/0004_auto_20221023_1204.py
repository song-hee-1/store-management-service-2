# Generated by Django 3.1 on 2022-10-23 03:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20221023_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='receiver_phone_number',
            field=models.CharField(help_text='휴대폰 번호는 다음과 같은 형식을 따라야 합니다: 010-1234-5678', max_length=13, validators=[django.core.validators.RegexValidator(regex='^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')]),
        ),
    ]