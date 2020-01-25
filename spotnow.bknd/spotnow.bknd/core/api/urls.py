from django.urls import path
from .views import (ClientListView,OwnerListView,ClientAddView,OwnerAddView,GarageAddView,GarageListView,GarageListActiveView,
					SmartLockAddView,SmartLockListView,SmartLockTokenView,SmartLockTokenRefreshView,GarageUpdateView,GarageDeleteView,
					BookingAddView,BookingUpdateView,TransactionView,BookingListView,BookingListClientView,ComentarioAddView,
					ComentarioListView,SmartLockDeleteView,SmartLockUpdateView,BookingListOwnerView,TransactionListView,SmartLockCommandView,
					UserTypeView)


urlpatterns = [
	path('clients/',ClientListView.as_view(),name='client-list'),
	path('client-add/',ClientAddView.as_view(),name='client-add'),
	#client update(telephone)
	path('owners/',OwnerListView.as_view(),name='owner-list'),
	path('owner-add/',OwnerAddView.as_view(),name='owner-add'),
	#owner update(telephone)
	path('user-profile/',UserTypeView.as_view(),name='user-type'),
	path('garage-add/',GarageAddView.as_view(),name='garage-add'),
	path('garages/',GarageListView.as_view(),name='garage-list'),
	path('garages-active/',GarageListActiveView.as_view(),name='garage-active-list'),
	path('garage-update/<int:pk>/',GarageUpdateView.as_view(),name='garage-update'),
	path('garage-delete/<int:pk>/',GarageDeleteView.as_view(),name='garage-delete'),
	path('smartlocks/',SmartLockListView.as_view(),name='smartlock-list'),
	path('smartlock-add/',SmartLockAddView.as_view(),name='smartlock-add'),
	path('smartlock-update/<int:pk>/',SmartLockUpdateView.as_view(),name='smartlock-update'),
	path('smartlock-delete/<int:pk>/',SmartLockDeleteView.as_view(),name='smartlock-delete'),
	path('smartlock-token/<int:pk>/',SmartLockTokenView.as_view(),name='smartlock-token'),
	path('smartlock-token-refresh/<int:pk>/',SmartLockTokenRefreshView.as_view(),name='smartlock-token-refresh'),
	path('smartlock-command/',SmartLockCommandView.as_view(),name='smartlock-command'),
	path('booking-add/',BookingAddView.as_view(),name='booking-add'),
	path('booking-update/<int:pk>/',BookingUpdateView.as_view(),name='booking-update'),
	path('bookings/',BookingListView.as_view(),name='booking-list'),
	path('booking-client/<int:pk>/',BookingListClientView.as_view(),name='booking-client-list'),
	path('booking-owner/<int:pk>/',BookingListOwnerView.as_view(),name='booking-owner-list'),
	path('payment/',TransactionView.as_view(),name='payment'),
	path('payment-list/<int:pk>/',TransactionListView.as_view(),name='payment-list'),
	path('comment-add/',ComentarioAddView.as_view(),name='comment-add'),
	path('comments/<int:pk>/',ComentarioListView.as_view(),name='comment-list'),
]