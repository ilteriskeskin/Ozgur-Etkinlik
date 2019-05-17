# Generated by Django 2.2.1 on 2019-05-15 13:52

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20190515_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True, verbose_name='slug'),
        ),
    ]