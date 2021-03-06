# Generated by Django 3.1.3 on 2022-03-20 16:03

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('status', models.CharField(default='A', max_length=1)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('short_description', models.TextField(max_length=512)),
                ('long_description', models.TextField(max_length=2048)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'topics',
            },
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('status', models.CharField(default='A', max_length=1)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('topic', models.ManyToManyField(to='api.Topic')),
            ],
            options={
                'db_table': 'folders',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(unique=True, upload_to=api.models.PathAndRename('uploads'))),
                ('status', models.CharField(default='A', max_length=1)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('limit_access', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('folder', models.ManyToManyField(to='api.Folder')),
            ],
            options={
                'db_table': 'documents',
            },
        ),
    ]
