# Generated by Django 3.1 on 2020-11-07 06:55

from django.db import migrations, models
import prime_date_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('prime_date_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='data',
            field=models.JSONField(default=prime_date_api.models.my_default),
        ),
    ]