from django.contrib import admin
from .models import *
# from .models import Report
# from .models import Form_bones
# from .models import Form_children

class FormAdmin(admin.ModelAdmin):
    fields =  ("name", "address", "phone", "clinic", "notes", 'date', "Id")

admin.site.register(Review)
admin.site.register(saturday)
admin.site.register(sunday)
admin.site.register(monday)
admin.site.register(tuesday)
admin.site.register(thursday)
admin.site.register(wednesday)
admin.site.register(Clinic_a)
admin.site.register(Clinic_bSatrday)
admin.site.register(Clinic_cSunday)
admin.site.register(Clinic_dMonday)
admin.site.register(Clinic_eTuesday)
admin.site.register(Clinic_fThursday)
admin.site.register(Clinic_gWednesday)
admin.site.register(Contact)
admin.site.register(login)

