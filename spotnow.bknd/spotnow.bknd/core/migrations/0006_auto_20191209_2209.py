# Generated by Django 2.2.4 on 2019-12-09 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20191209_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garage',
            name='isinactive',
            field=models.BooleanField(blank=True, db_column='isInactive', null=True),
        ),
    ]