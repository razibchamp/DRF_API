# Generated by Django 2.1 on 2018-08-15 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0004_auto_20180815_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
