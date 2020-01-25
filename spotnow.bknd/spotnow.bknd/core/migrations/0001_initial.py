# Generated by Django 2.2.4 on 2019-11-30 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id_admin', models.AutoField(db_column='id_Admin', primary_key=True, serialize=False)),
                ('name_admin', models.CharField(db_column='Name_Admin', max_length=255)),
                ('email_admin', models.CharField(db_column='Email_Admin', max_length=255)),
                ('passwordhash', models.CharField(db_column='PasswordHash', max_length=64)),
                ('passwordsalt', models.CharField(db_column='passwordSalt', max_length=128)),
            ],
            options={
                'db_table': 'Admin',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.TextField(blank=True, null=True)),
                ('valueclosed', models.FloatField(blank=True, db_column='valueClosed', null=True)),
                ('borkermargin', models.FloatField(blank=True, db_column='borkerMargin', null=True)),
                ('profit', models.FloatField(blank=True, null=True)),
                ('createdby', models.IntegerField(blank=True, db_column='createdBy', null=True)),
                ('createddate', models.DateTimeField(blank=True, db_column='createdDate', null=True)),
                ('updatedby', models.IntegerField(blank=True, db_column='updatedBy', null=True)),
                ('updateddate', models.DateTimeField(blank=True, db_column='updatedDate', null=True)),
                ('isinactive', models.IntegerField(blank=True, db_column='isInactive', null=True)),
                ('token', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'booking',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('nif', models.CharField(max_length=255)),
                ('passwordhash', models.CharField(db_column='passwordHash', max_length=64)),
                ('passwordsalt', models.CharField(db_column='passwordSalt', max_length=128)),
                ('createddate', models.DateTimeField(db_column='createdDate')),
                ('updateddate', models.DateTimeField(db_column='updatedDate')),
                ('isinactive', models.TextField(db_column='isInactive')),
                ('telephone', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'Client',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Garage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('isinactive', models.TextField(blank=True, db_column='isInactive', null=True)),
                ('createddate', models.DateTimeField(blank=True, db_column='createdDate', null=True)),
                ('updatedby', models.IntegerField(blank=True, db_column='updatedBy', null=True)),
                ('updateddate', models.DateTimeField(blank=True, db_column='updatedDate', null=True)),
                ('latitude', models.CharField(blank=True, max_length=45, null=True)),
                ('longitude', models.CharField(blank=True, max_length=45, null=True)),
                ('address', models.CharField(blank=True, max_length=45, null=True)),
                ('country', models.CharField(blank=True, max_length=45, null=True)),
                ('city', models.CharField(blank=True, max_length=45, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'garage',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, db_column='userName', max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('nif', models.IntegerField(blank=True, null=True)),
                ('passwordhash', models.CharField(blank=True, db_column='passwordHash', max_length=64, null=True)),
                ('passwordsalt', models.CharField(blank=True, db_column='passwordSalt', max_length=128, null=True)),
                ('createddate', models.DateTimeField(blank=True, db_column='createdDate', null=True)),
                ('updateddate', models.DateTimeField(blank=True, db_column='updatedDate', null=True)),
                ('isinactive', models.TextField(blank=True, db_column='isInactive', null=True)),
                ('role_id', models.IntegerField(blank=True, null=True)),
                ('telephone', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'Owner',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('createdby', models.IntegerField(blank=True, db_column='createdBy', null=True)),
                ('createddate', models.DateTimeField(blank=True, db_column='createdDate', null=True)),
                ('updatedby', models.IntegerField(blank=True, db_column='updatedBy', null=True)),
                ('updateddate', models.DateTimeField(blank=True, db_column='updatedDate', null=True)),
                ('isinactive', models.TextField(blank=True, db_column='isInactive', null=True)),
                ('transactiontype_id', models.IntegerField()),
                ('tipo_transaçao', models.CharField(max_length=45)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Booking')),
            ],
            options={
                'db_table': 'transaction',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Smartlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('isinactive', models.TextField(blank=True, db_column='IsInactive', null=True)),
                ('createdby', models.IntegerField(blank=True, db_column='createdBy', null=True)),
                ('createddate', models.DateTimeField(blank=True, db_column='createdDate', null=True)),
                ('updatedby', models.IntegerField(blank=True, db_column='updatedBy', null=True)),
                ('updateddate', models.DateTimeField(blank=True, db_column='updatedDate', null=True)),
                ('tokenprimarykey', models.CharField(blank=True, max_length=255, null=True)),
                ('garage', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Garage')),
            ],
            options={
                'db_table': 'smartlock',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('idhorario', models.AutoField(db_column='idHorario', primary_key=True, serialize=False)),
                ('dia_semana', models.CharField(blank=True, db_column='Dia_Semana', max_length=255, null=True)),
                ('hora_inicio', models.CharField(db_column='Hora_Inicio', max_length=255)),
                ('hora_final', models.CharField(blank=True, db_column='Hora_Final', max_length=255, null=True)),
                ('preço', models.CharField(db_column='Preço', max_length=255)),
                ('tipo_mensalidade', models.CharField(blank=True, max_length=255, null=True)),
                ('garage', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Garage')),
            ],
            options={
                'db_table': 'Horario',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='garage',
            name='owner',
            field=models.ForeignKey(db_column='Owner_id', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Owner'),
        ),
        migrations.AddField(
            model_name='booking',
            name='garage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Garage'),
        ),
        migrations.AddField(
            model_name='booking',
            name='receipt',
            field=models.ForeignKey(db_column='Receipt_id', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Client'),
        ),
    ]
