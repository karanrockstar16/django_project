# Generated by Django 3.1 on 2020-11-07 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prime_date_api', '0002_auto_20201107_0655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mymodel',
            old_name='data',
            new_name='json_data',
        ),
    ]
