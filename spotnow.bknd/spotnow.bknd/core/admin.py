from django.contrib import admin
from .models import Client,Horario,Owner,Booking,Garage,Smartlock,Transaction,Comentario

# Register your models here.

admin.site.register(Client)
admin.site.register(Horario)
admin.site.register(Owner)
admin.site.register(Booking)
admin.site.register(Garage)
admin.site.register(Smartlock)
admin.site.register(Transaction)
admin.site.register(Comentario)



