# Generated by Django 4.2.2 on 2023-07-11 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0026_remove_companydata_video_link_tour_video_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeekDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Hafta günü',
                'verbose_name_plural': 'Hafta günleri',
            },
        ),
        migrations.AddField(
            model_name='tour',
            name='time_end',
            field=models.TimeField(blank=True, null=True, verbose_name='Bitiş saati'),
        ),
        migrations.AddField(
            model_name='tour',
            name='time_start',
            field=models.TimeField(blank=True, null=True, verbose_name='Başlangıç saati'),
        ),
        migrations.AddField(
            model_name='tour',
            name='weekdays',
            field=models.ManyToManyField(to='transfer.weekday', verbose_name='Hafta günleri'),
        ),
    ]
