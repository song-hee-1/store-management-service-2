# Generated by Django 3.1 on 2022-10-23 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='주소')),
                ('receiver_name', models.CharField(max_length=40, verbose_name='수령자이름')),
                ('order_state', models.CharField(choices=[('결제취소', 0), ('결제완료', 1)], default=1, max_length=4, verbose_name='주문서 상태')),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name='주문 날짜')),
                ('total_price', models.PositiveIntegerField(null=True, verbose_name='주문서 총 가격')),
            ],
            options={
                'verbose_name': '주문',
                'verbose_name_plural': '주문 목록',
                'db_table': 'order',
            },
        ),
    ]
