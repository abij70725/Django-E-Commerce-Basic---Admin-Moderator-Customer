from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Customer)
admin.site.register(Contractor)
admin.site.register(Worker)
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Enquiry)

