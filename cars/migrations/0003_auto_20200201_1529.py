# Generated by Django 3.0.2 on 2020-02-01 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20200201_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]
