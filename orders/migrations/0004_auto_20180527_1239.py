# Generated by Django 2.0.5 on 2018-05-27 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20180526_1708'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'Товар в заказе', 'verbose_name_plural': 'Товары в заказе'},
        ),
    ]
