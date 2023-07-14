# Generated by Django 4.2.2 on 2023-06-22 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0003_alter_place_options_transfer_date_transfer_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='paid',
            field=models.BooleanField(default=False, verbose_name='Ödeme statüsü'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Fiyat (USD)'),
        ),
    ]