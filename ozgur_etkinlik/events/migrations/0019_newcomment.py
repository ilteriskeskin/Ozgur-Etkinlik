# Generated by Django 2.2.1 on 2019-05-19 23:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0018_remove_event_finish_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_parent', models.BooleanField(default=False)),
                ('object_id', models.PositiveIntegerField()),
                ('icerik', models.TextField(max_length=1000, null=True, verbose_name='Yorum')),
                ('comment_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('content_type', models.ForeignKey(null=True, on_delete=True, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(default=1, null=True, on_delete=True, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'İç içe yorum sistemi',
            },
        ),
    ]
