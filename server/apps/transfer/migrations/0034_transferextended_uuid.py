# Generated by Django 4.2.2 on 2023-07-13 10:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0033_remove_transfer_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='transferextended',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]