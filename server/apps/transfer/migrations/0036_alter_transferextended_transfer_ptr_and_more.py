# Generated by Django 4.2.2 on 2023-07-13 11:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0035_alter_transferextended_iata_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transferextended',
            name='transfer_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='transfer.transfer'),
        ),
        migrations.AlterField(
            model_name='transferextended',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]