# Generated by Django 4.2.2 on 2023-06-29 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0021_transfer_uuid_alter_transfer_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='uuid',
        ),
    ]