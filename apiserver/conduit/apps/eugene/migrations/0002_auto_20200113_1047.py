# Generated by Django 2.2.8 on 2020-01-13 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eugene', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='alpha3code',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='country',
            name='phoneCode',
            field=models.CharField(max_length=5),
        ),
    ]