# Generated by Django 2.2.4 on 2019-11-30 22:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='email',
        ),
        migrations.RemoveField(
            model_name='client',
            name='isinactive',
        ),
        migrations.RemoveField(
            model_name='client',
            name='name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='passwordhash',
        ),
        migrations.RemoveField(
            model_name='client',
            name='passwordsalt',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='email',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='isinactive',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='passwordhash',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='passwordsalt',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='role_id',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='username',
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='owner',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
