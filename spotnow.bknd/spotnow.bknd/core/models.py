# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator



'''
class Admin(models.Model):
    id_admin = models.AutoField(db_column='id_Admin', primary_key=True)  # Field name made lowercase.
    name_admin = models.CharField(db_column='Name_Admin', max_length=255)  # Field name made lowercase.
    email_admin = models.CharField(db_column='Email_Admin', max_length=255)  # Field name made lowercase.
    passwordhash = models.CharField(db_column='PasswordHash', max_length=64)  # Field name made lowercase.
    passwordsalt = models.CharField(db_column='passwordSalt', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Admin'
'''

class Client(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase
    #name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    #email = models.CharField(max_length=255)
    nif = models.CharField(max_length=255)
    #passwordhash = models.CharField(db_column='passwordHash', max_length=64)  # Field name made lowercase.
    #passwordsalt = models.CharField(db_column='passwordSalt', max_length=128)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate',auto_now_add=True)  # Field name made lowercase.
    #updateddate = models.DateTimeField(db_column='updatedDate')  # Field name made lowercase.
    #isinactive = models.TextField(db_column='isInactive')  # Field name made lowercase. This field type is a guess.
    telephone = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'Client'

    def __str__(self):
        return self.user.username

class Horario(models.Model):
    idhorario = models.AutoField(db_column='idHorario', primary_key=True)  # Field name made lowercase.
    dia_semana = models.CharField(db_column='Dia_Semana', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hora_inicio = models.CharField(db_column='Hora_Inicio', max_length=255)  # Field name made lowercase.
    hora_final = models.CharField(db_column='Hora_Final', max_length=255, blank=True, null=True)  # Field name made lowercase.
    preço = models.CharField(db_column='Preço', max_length=255)  # Field name made lowercase.
    garage = models.ForeignKey('Garage', models.DO_NOTHING)
    tipo_mensalidade = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Horario'


class Owner(models.Model):
    user = models.OneToOneField(User,models.CASCADE)
    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase
    #username = models.CharField(db_column='userName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    #email = models.CharField(max_length=255, blank=True, null=True)
    nif = models.IntegerField(blank=True, null=True)
    #passwordhash = models.CharField(db_column='passwordHash', max_length=64, blank=True, null=True)  # Field name made lowercase.
    #passwordsalt = models.CharField(db_column='passwordSalt', max_length=128, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate',auto_now_add=True)  # Field name made lowercase.
    #updateddate = models.DateTimeField(db_column='updatedDate', blank=True, null=True)  # Field name made lowercase.
    #isinactive = models.TextField(db_column='isInactive', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    #role_id = models.IntegerField(blank=True, null=True)
    telephone = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Owner'

    def __str__(self):
        return self.user.username



class Booking(models.Model):
    state = models.TextField(blank=True, null=True)  # This field type is a guess.
    #valueclosed = models.FloatField(db_column='valueClosed', blank=True, null=True)  # Field name made lowercase.
    #borkermargin = models.FloatField(db_column='borkerMargin', blank=True, null=True)  # Field name made lowercase.
    profit = models.FloatField(blank=True, null=True)
    #createdby = models.IntegerField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate',auto_now_add=True)  # Field name made lowercase.
    enddate = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    #updatedby = models.IntegerField(db_column='updatedBy', blank=True, null=True)  # Field name made lowercase.
    #updateddate = models.DateTimeField(db_column='updatedDate', blank=True, null=True)  # Field name made lowercase.
    #isinactive = models.BooleanField(db_column='isInactive', blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(max_length=255)
    receipt = models.ForeignKey(Client, models.DO_NOTHING, db_column='Receipt_id')  # Field name made lowercase.
    garage = models.ForeignKey('Garage', models.DO_NOTHING)
    #final_price = models.FloatField(blank=True, null=True)
    #comentarios=models.ForeignKey(Comentario, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'booking'

class Comentario(models.Model):
    booking = models.ForeignKey(Booking,on_delete=models.DO_NOTHING)
    comentario=models.CharField(max_length=255)
    rating=models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    
    class Meta:
        managed = True
        db_table = 'comentario'


class Garage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    isinactive = models.BooleanField(db_column='isInactive', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createddate = models.DateTimeField(db_column='createdDate',auto_now_add=True)  # Field name made lowercase.
    #updatedby = models.IntegerField(db_column='updatedBy', blank=True, null=True)  # Field name made lowercase.
    #updateddate = models.DateTimeField(db_column='updatedDate', blank=True, null=True)  # Field name made lowercase.
    #latitude = models.CharField(max_length=45, blank=True, null=True)
    #longitude = models.CharField(max_length=45, blank=True, null=True)
    state_garage=models.BooleanField(db_column='state_garage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    latitude = models.CharField(max_length=45, blank=True, null=True)
    longitude = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    zipcode = models.CharField(max_length=45, blank=True, null=True)
    owner = models.ForeignKey(Owner, models.DO_NOTHING, db_column='Owner_id')  # Field name made lowercase.
    preco = models.CharField(db_column='Preco', max_length=255)
    imagem = models.ImageField(blank=True,null=True)

    class Meta:
        managed = True
        db_table = 'garage'

    def __str__(self):
        return self.name


class Smartlock(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    isinactive = models.BooleanField(db_column='IsInactive', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    #createdby = models.IntegerField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate',auto_now_add=True)  # Field name made lowercase.
    #updatedby = models.IntegerField(db_column='updatedBy', blank=True, null=True)  # Field name made lowercase.
    #updateddate = models.DateTimeField(db_column='updatedDate', blank=True, null=True)  # Field name made lowercase.
    tokenprimarykey = models.CharField(max_length=255, blank=True, null=True)
    garage = models.ForeignKey(Garage, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'smartlock'


    def __str__(self):
        return self.name


class Transaction(models.Model):
    amount = models.FloatField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    #createdby = models.IntegerField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate',auto_now_add=True)  # Field name made lowercase.
    #updatedby = models.IntegerField(db_column='updatedBy', blank=True, null=True)  # Field name made lowercase.
    #updateddate = models.DateTimeField(db_column='updatedDate', blank=True, null=True)  # Field name made lowercase.
    #isinactive = models.TextField(db_column='isInactive', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    #transactiontype_id = models.IntegerField()
    booking = models.ForeignKey(Booking, models.DO_NOTHING)
    tipo_transaçao = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'transaction'
