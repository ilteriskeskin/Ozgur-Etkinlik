# Generated by Django 2.2.1 on 2019-05-15 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20190515_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='finish_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Bitiş Tarihi'),
        ),
        migrations.AlterField(
            model_name='event',
            name='starter_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Başlangıç tarihi'),
        ),
    ]
