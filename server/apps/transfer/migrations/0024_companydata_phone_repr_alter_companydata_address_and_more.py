# Generated by Django 4.2.2 on 2023-06-30 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0023_transfer_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydata',
            name='phone_repr',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='İş adresi'),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='address_link',
            field=models.TextField(blank=True, null=True, verbose_name='İş adresi linki'),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Kurumsal E-posta'),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='phone_whatsapp',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
