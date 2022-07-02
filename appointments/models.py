
from django.db import models

        
class login(models.Model):
    username = models.TextField()
    password = models.TextField()

    def __str__(self) -> str:
        return self.username 

class Review(models.Model):
    review_detail = models.TextField()
       
    def __str__(self) -> str:
        return self.review_detail

class Contact(models.Model):
    name = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    message = models.TextField()

    def __str__(self) -> str:
        return self.name

class Clinic_a(models.Model):
    name = models.TextField()

    def __str__(self) -> str:
        return self.name

class Clinic_bSatrday(models.Model):
    name = models.TextField()

    def __str__(self) -> str:
        return self.name

class Clinic_cSunday(models.Model):
    name = models.TextField()

    def __str__(self) -> str:
        return self.name

class Clinic_dMonday(models.Model):
    name = models.TextField()

    def __str__(self) -> str:
        return self.name

class Clinic_eTuesday(models.Model):
    name = models.TextField()

    def __str__(self) -> str:
        return self.name

class Clinic_fThursday(models.Model):
    name = models.TextField()

    def __str__(self) -> str:
        return self.name

class Clinic_gWednesday(models.Model):
    name = models.TextField()

    def __str__(self) -> str:
        return self.name

class saturday(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    clinic = models.ForeignKey(Clinic_bSatrday, on_delete=models.CASCADE)
    address = models.TextField()
    notes = models.TextField()
    Id = models.IntegerField(primary_key=True)

    def __str__(self) -> str:
        return self.name+' '+str(self.Id)

class sunday(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    clinic = models.ForeignKey(Clinic_cSunday, on_delete=models.CASCADE)
    address = models.TextField()
    notes = models.TextField()
    Id = models.IntegerField(primary_key=True)

    def __str__(self) -> str:
        return self.name+' '+str(self.Id)

class monday(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    clinic = models.ForeignKey(Clinic_dMonday, on_delete=models.CASCADE)
    address = models.TextField()
    notes = models.TextField()
    Id = models.IntegerField(primary_key=True)

    def __str__(self) -> str:
        return self.name+' '+str(self.Id)

class tuesday(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    clinic = models.ForeignKey(Clinic_eTuesday, on_delete=models.CASCADE)
    address = models.TextField()
    notes = models.TextField()
    Id = models.IntegerField(primary_key=True)

    def __str__(self) -> str:
        return self.name+' '+str(self.Id)


class thursday(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    clinic = models.ForeignKey(Clinic_fThursday, on_delete=models.CASCADE)
    address = models.TextField()
    notes = models.TextField()
    Id = models.IntegerField(primary_key=True)

    def __str__(self) -> str:
        return self.name+' '+str(self.Id)

class wednesday(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    clinic = models.ForeignKey(Clinic_gWednesday, on_delete=models.CASCADE)
    # date = models.DateField(auto_now=True)
    address = models.TextField()
    notes = models.TextField()
    Id = models.IntegerField(primary_key=True)

    def __str__(self) -> str:
        return self.name+' '+str(self.Id)


