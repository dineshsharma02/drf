# Generated by Django 2.2.13 on 2022-01-19 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('roll', models.IntegerField()),
                ('city', models.CharField(max_length=40)),
            ],
        ),
    ]
