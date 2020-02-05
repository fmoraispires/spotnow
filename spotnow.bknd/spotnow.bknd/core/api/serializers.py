from rest_framework import serializers
from core.models import Client,Horario,Owner,Booking,Garage,Smartlock,Transaction,Comentario
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class User1Serializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username','password','email')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('__all__')


class ClientSerializer(serializers.ModelSerializer):
	user_obj = serializers.SerializerMethodField()

	class Meta:
		model = Client
		fields = ('user','user_obj','id','nif','createddate','telephone')

	def get_user_obj(self,obj):
		return UserSerializer(obj.user).data



class ClientAddSerializer(serializers.ModelSerializer):
	user = User1Serializer(required=True)


	class Meta:
		model = Client
		fields = ('user','id','nif','createddate','telephone')    


	def create(self,validated_data):
		print(validated_data);
		data = validated_data.pop('user')
		username = data['username']
		password = data['password']
		email = data['email']

		nif=validated_data.pop('nif')
		#createddate=validated_data.pop('createddate')
		#updateddate=validated_data.pop('updateddate')
		telephone=validated_data.pop('telephone')

		user = User.objects.create_user(username, email, password)
		token = Token.objects.create(user=user)
		client = Client.objects.create(user=user,nif=nif,telephone=telephone)

		return client


	#def get_user_obj(self,obj):
	#	return UserSerializer(obj.user).data


	def get_username(self,obj):
		return obj.user.username

	def get_password(self,obj):
		return obj.user.password

	def get_email(self,obj):
		return obj.user.email


class OwnerSerializer(serializers.ModelSerializer):
	user_obj = serializers.SerializerMethodField()

	class Meta:
		model = Owner
		fields = ('user','user_obj','id','nif','createddate','telephone')

	def get_user_obj(self,obj):
		return UserSerializer(obj.user).data

class OwnerAddSerializer(serializers.ModelSerializer):
	user = User1Serializer(required=True)


	class Meta:
		model = Owner
		fields = ('user','id','nif','createddate','telephone')    


	def create(self,validated_data):
		print(validated_data);
		data = validated_data.pop('user')
		username = data['username']
		password = data['password']
		email = data['email']
		nif=validated_data.pop('nif')
		#createddate=validated_data.pop('createddate')
		#updateddate=validated_data.pop('updateddate')
		telephone=validated_data.pop('telephone')


		user = User.objects.create_user(username, email, password)
		token = Token.objects.create(user=user)
		owner = Owner.objects.create(user=user,nif=nif,telephone=telephone)
		return owner


	#def get_user_obj(self,obj):
	#	return UserSerializer(obj.user).data


	def get_username(self,obj):
		return obj.user.username

	def get_password(self,obj):
		return obj.user.password

	def get_email(self,obj):
		return obj.user.email


class GarageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Garage
		fields = ('id','name','isinactive','state_garage','createddate','latitude','longitude','address','country','city','zipcode','owner','imagem')


class SmartlockSerializer(serializers.ModelSerializer):
	class Meta:
		model = Smartlock
		fields = ('__all__')


class SmartlockAddSerializer(serializers.ModelSerializer):
	class Meta:
		model = Smartlock
		fields = ('name','isinactive','createddate','garage')

class SmartlockUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Smartlock
		fields = ('isinactive',)


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ('__all__')

class BookingAddSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ('state','createddate','receipt','garage',)

class BookingUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ('state',)


class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		fields = ('__all__')

class HorarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Horario
		fields = ('__all__')

class ComentarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comentario
		fields = ('__all__')

