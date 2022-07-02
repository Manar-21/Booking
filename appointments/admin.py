from django.contrib import admin
from .models import Review, Clinic, Form, Contact, login
# from .models import Report
# from .models import Form_bones
# from .models import Form_children

class FormAdmin(admin.ModelAdmin):
    fields =  ("name", "address", "phone", "clinic", "notes", 'date', "Id")

# Register your models here.
admin.site.register(Review)
# admin.site.register(Report)
admin.site.register(Form)
admin.site.register(Clinic)
# admin.site.register(Form_bones)
# admin.site.register(Form_children)
admin.site.register(Contact)
admin.site.register(login)

