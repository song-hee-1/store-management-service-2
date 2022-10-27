# Generated by Django 3.1 on 2022-10-27 02:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='상품 이름')),
                ('description', models.TextField(verbose_name='상품 설명')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='상품 가격')),
                ('stock', models.PositiveIntegerField(verbose_name='재고')),
                ('create_at', models.DateTimeField(auto_now=True, verbose_name='상품 업로드 날짜')),
                ('order', models.ManyToManyField(blank=True, related_name='user_order', through='orders.Order', to=settings.AUTH_USER_MODEL, verbose_name='상품 주문내역')),
            ],
            options={
                'verbose_name': '상품',
                'verbose_name_plural': '상품 목록',
                'db_table': 'product',
            },
        ),
    ]
