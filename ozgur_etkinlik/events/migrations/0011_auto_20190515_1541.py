# Generated by Django 2.2.1 on 2019-05-15 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_event_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar'),
        ),
    ]
