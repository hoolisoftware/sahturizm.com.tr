# Generated by Django 4.2.2 on 2023-06-29 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0019_alter_transferextended_date_back'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='done',
            field=models.BooleanField(default=False, verbose_name='Tamamlandı'),
        ),
    ]