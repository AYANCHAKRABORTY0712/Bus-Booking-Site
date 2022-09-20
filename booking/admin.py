from django.contrib import admin
from booking.models import USER,BUS,Booking,Contact

# Register your models here.

admin.site.register(USER)
admin.site.register(BUS)
admin.site.register(Booking)
admin.site.register(Contact)