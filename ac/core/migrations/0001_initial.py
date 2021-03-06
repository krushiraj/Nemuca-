# Generated by Django 2.0.2 on 2018-03-08 06:39

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_choice', models.CharField(choices=[('R', 'Running'), ('P', 'Played'), ('W', 'Waiting')], max_length=8)),
                ('gId', models.CharField(max_length=5)),
                ('QId', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5), size=None)),
                ('Total', models.IntegerField(default=0)),
                ('date_time', models.DateTimeField(auto_now=True, verbose_name='Date Published')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eId', models.CharField(default='NULL', max_length=3)),
                ('eName', models.CharField(max_length=50)),
                ('eCount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Hits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mediaType', models.CharField(max_length=20)),
                ('link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QId', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationsAndParticipations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5), size=None)),
                ('registered', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5), size=None)),
                ('participated', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5), size=None)),
                ('QId', models.OneToOneField(max_length=5, on_delete='CASCADE', to='core.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='details',
            name='eId',
            field=models.OneToOneField(max_length=5, on_delete='CASCADE', to='core.Event'),
        ),
    ]
