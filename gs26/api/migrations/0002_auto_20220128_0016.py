# Generated by Django 2.2.13 on 2022-01-27 18:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='passby',
            field=models.ForeignKey(on_delete='cascade', to=settings.AUTH_USER_MODEL),
        ),
    ]
