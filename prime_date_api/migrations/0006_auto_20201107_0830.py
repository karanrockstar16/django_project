# Generated by Django 3.1 on 2020-11-07 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime_date_api', '0005_auto_20201107_0825'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='name',
            field=models.CharField(default='karan', max_length=200),
        ),
        migrations.AlterModelTable(
            name='mymodel',
            table=None,
        ),
    ]
