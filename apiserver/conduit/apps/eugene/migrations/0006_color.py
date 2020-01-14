# Generated by Django 2.2.8 on 2020-01-13 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eugene', '0005_auto_20200113_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('value', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
    ]