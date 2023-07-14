# Generated by Django 4.2.2 on 2023-07-11 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0025_media_companydata_video_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companydata',
            name='video_link',
        ),
        migrations.AddField(
            model_name='tour',
            name='video_link',
            field=models.URLField(blank=True, null=True, verbose_name='Video linki'),
        ),
    ]
