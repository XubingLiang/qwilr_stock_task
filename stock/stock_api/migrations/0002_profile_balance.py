# Generated by Django 2.1.7 on 2019-02-22 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='balance',
            field=models.FloatField(default=0.0),
        ),
    ]