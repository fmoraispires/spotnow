# Generated by Django 2.2.4 on 2019-12-09 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191130_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='isinactive',
            field=models.BooleanField(blank=True, db_column='isInactive', null=True),
        ),
    ]
