import hashlib,uuid
import datetime
from rest_framework.generics import ListAPIView, RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework import mixins
from rest_framework import viewsets

from kubemq.events.lowlevel.event import Event
from kubemq.events.lowlevel.sender import Sender

from django.contrib.auth.models import User
from core.models import Client,Horario,Owner,Booking,Garage,Smartlock,Transaction,Comentario
from .serializers import (ClientSerializer,HorarioSerializer,OwnerSerializer,BookingSerializer,
						  GarageSerializer,SmartlockSerializer,ClientAddSerializer,TransactionSerializer,
						  OwnerAddSerializer,SmartlockAddSerializer,BookingAddSerializer,BookingUpdateSerializer,
						  ComentarioSerializer,SmartlockUpdateSerializer)


class ClientAddView(CreateAPIView):
	permissions_classes = (AllowAny,)
	serializer_class = ClientAddSerializer
	queryset = Client.objects.all()

class ClientListView(ListAPIView):
	permissions_classes = (AllowAny)
	serializer_class = ClientSerializer
	queryset = Client.objects.all()


class OwnerListView(ListAPIView):
	permissions_classes = (AllowAny)
	serializer_class = OwnerSerializer
	queryset = Owner.objects.all()

class OwnerAddView(CreateAPIView):
	permissions_classes = (AllowAny,)
	serializer_class = OwnerAddSerializer
	queryset = Owner.objects.all()


class GarageAddView(CreateAPIView):
	permissions_classes = (IsAuthenticated,)
	serializer_class = GarageSerializer
	queryset = Garage.objects.all()


class GarageListView(ListAPIView):
	permissions_classes = (AllowAny,)
	serializer_class = GarageSerializer
	queryset = Garage.objects.all()


class GarageListActiveView(ListAPIView):
	permissions_classes = (AllowAny,)
	serializer_class = GarageSerializer
	
	def get_queryset(self):
		return Garage.objects.filter(isinactive=True)

class GarageUpdateView(UpdateAPIView):
	permissions_classes = (IsAuthenticated,)
	serializer_class = GarageSerializer
	queryset = Garage.objects.all()

class GarageDeleteView(DestroyAPIView):
	permissions_classes = (IsAuthenticated,)
	queryset = Garage.objects.all()


class SmartLockListView(ListAPIView):
	permissions_classes = (AllowAny,)
	serializer_class = SmartlockSerializer
	queryset = Smartlock.objects.all()

class SmartLockAddView(CreateAPIView):
	permissions_classes = (IsAuthenticated,)
	serializer_class = SmartlockAddSerializer

	def post(self,request,*args,**kwargs):
		print(request.data)
		name = request.data.get('name',None)
		isinactive = request.data.get('isinactive',False)
		if(isinactive == 'true'):
			isinactive = True
		#createdby = request.data.get('createdby',None)
		createddate = request.data.get('createddate',None)
		#updatedby = request.data.get('updatedby',None)
		#updateddate = request.data.get('updateddate',None)
		garage_id = request.data.get('garage',None)
		garage = Garage.objects.get(id=garage_id)

		salt = uuid.uuid4().hex
		hasher = hashlib.sha512(salt.encode('utf-8'))
		token = hasher.hexdigest()[:24]
		
		lock = Smartlock.objects.create(name=name,isinactive=isinactive,createddate=createddate,
										garage=garage,tokenprimarykey=token)

		l = SmartlockSerializer(lock).data
		
		return Response({"lock":l},status=HTTP_200_OK)

class SmartLockTokenView(APIView):
	permissions_classes = (IsAuthenticated,)

	def get(self,request,*args,**kwargs):
		smartlock_id = self.kwargs['pk']
		lock = Smartlock.objects.get(id=smartlock_id)
		return Response({"token":lock.tokenprimarykey},status=HTTP_200_OK)


class SmartLockTokenRefreshView(APIView):
	permissions_classes = (IsAuthenticated,)

	def post(self,request,*args,**kwargs):
		smartlock_id = self.kwargs['pk']
		lock = Smartlock.objects.get(id=smartlock_id)

		salt = uuid.uuid4().hex
		hasher = hashlib.sha512(salt.encode('utf-8'))
		token = hasher.hexdigest()[:24]
		
		lock.tokenprimarykey = token
		lock.save()

		return Response({"token":token},status=HTTP_200_OK)

class SmartLockDeleteView(DestroyAPIView):
	permissions_classes = (IsAuthenticated,)
	queryset = Smartlock.objects.all()


class SmartLockUpdateView(UpdateAPIView):
	permissions_classes = (IsAuthenticated,)
	serializer_class = SmartlockUpdateSerializer
	queryset = Smartlock.objects.all()


class SmartLockCommandView(APIView):
	permissions_classes = (IsAuthenticated,)

	def post(self,request,*args,**kwargs):
		cmd = request.data.get('cmd',None)
		publisher  = Sender("51.105.156.152:50000")
		event = Event(metadata="EventMetaData",body=("hello kubemq - sending single event").encode('UTF-8'),
					  store=False,channel="testing_event_channel",client_id="hello-world-subscriber")
		try:
			res = publisher.send_event(event)
			print(res)
		except Exception as err:
			print("'error sending:'%s'" % (err))
			return Response(status=HTTP_400_BAD_REQUEST)

		return Response(status=HTTP_200_OK)


class BookingAddView(CreateAPIView):
	permissions_classes = (IsAuthenticated,)
	serializer_class = BookingAddSerializer

	def post(self,request,*args,**kwargs):
		#print (request.data)
		state = request.data.get('state',None)
		date = request.data.get('createddate',None)
		receipt = request.data.get('receipt',None)
		garage_id = request.data.get('garage',None)

		lock = Smartlock.objects.filter(garage=garage_id)
		token = lock[0].tokenprimarykey
		client = Client.objects.get(id=receipt)
		garage = Garage.objects.get(id=garage_id)

		booking = Booking.objects.create(state=state,createddate=date,token=token,
										 receipt=client,garage=garage,profit=0.05)
		b = BookingSerializer(booking).data
		return Response({"booking":b},status=HTTP_200_OK)

class BookingUpdateView(UpdateAPIView):
	permissions_classes = (IsAuthenticated,)
	serializer_class = BookingUpdateSerializer
	queryset = Booking.objects.all()

class BookingListView(ListAPIView):
	permissions_classes = (AllowAny)
	serializer_class = BookingSerializer
	queryset = Booking.objects.all()

class BookingListClientView(ListAPIView):
	permissions_classes = (IsAuthenticated,)
	serializer_class = BookingSerializer
	
	def get_queryset(self):
		user_id = self.kwargs['pk']
		return Booking.objects.filter(receipt=user_id)


class BookingListOwnerView(ListAPIView):
	permissions_classes = (IsAuthenticated,)
	serializer_class = BookingSerializer
	
	def get_queryset(self):
		owner_id = self.kwargs['pk']
		garages = Garage.objects.filter(owner=owner_id)
		print(garages)
		bookings = []
		for g in garages:
			bookings+= Booking.objects.filter(garage=g)
			print (bookings)
		return bookings


class TransactionView(CreateAPIView):
	permissions_classes = (IsAuthenticated,)
	serializer_class = TransactionSerializer
	queryset = Transaction.objects.all()

class TransactionListView(ListAPIView):
	permissions_classes = (IsAuthenticated,)
	serializer_class = TransactionSerializer

	def get_queryset(self):
		booking_id = self.kwargs['pk']
		return Transaction.objects.filter(booking=booking_id)


class ComentarioAddView(CreateAPIView):
	permissions_classes = (IsAuthenticated,)
	serializer_class = ComentarioSerializer
	queryset = Comentario.objects.all()

class ComentarioListView(ListAPIView):
	permissions_classes = (AllowAny,)
	serializer_class = ComentarioSerializer
	
	def get_queryset(self):
		garage_id = self.kwargs['pk']
		bookings = Booking.objects.filter(garage=garage_id)
		comments = []
		for b in bookings:
			comments += Comentario.objects.filter(booking=b)
		return comments


class UserTypeView(APIView):
	permissions_classes = (IsAuthenticated,)

	def get(self,request,*args,**kwargs):
		print(request.user)
		try:		
			client = Client.objects.get(user=request.user)
			print (client)
			return Response({"Client":ClientSerializer(client).data},status=HTTP_200_OK)
		except:
			owner = Owner.objects.get(user=request.user)
			return Response({"Owner":OwnerSerializer(owner).data},status=HTTP_200_OK)
		return Response(status=HTTP_400_BAD_REQUEST)
