# Generated by Django 3.1 on 2022-10-22 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='상품이름')),
                ('description', models.TextField(verbose_name='상품설명')),
                ('stock', models.PositiveIntegerField(verbose_name='재고')),
                ('create_at', models.DateTimeField(auto_now=True, verbose_name='상품 업로드 날짜')),
            ],
            options={
                'verbose_name': '상품',
                'verbose_name_plural': '상품 목록',
                'db_table': 'product',
            },
        ),
    ]
