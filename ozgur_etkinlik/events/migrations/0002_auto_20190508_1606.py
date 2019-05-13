# Generated by Django 2.2.1 on 2019-05-08 13:06

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('content', ckeditor.fields.RichTextField()),
                ('subscriber', models.IntegerField(verbose_name='Katılımcı Sayısı')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('finished_date', models.CharField(default='', max_length=10, verbose_name='Bitirilmesi Gereken Tarih')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar')),
            ],
        ),
        migrations.DeleteModel(
            name='OmeFile',
        ),
    ]
