# Generated by Django 2.2.4 on 2020-01-15 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20191218_0101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='createddate',
        ),
    ]
