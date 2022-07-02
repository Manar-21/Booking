
from django.db import models

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

class Clinic(models.Model):
    name = models.TextField()

    def __str__(self) -> str:
        return self.name

class Form(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField(auto_now=True)
    address = models.TextField()
    notes = models.TextField()
    Id = models.IntegerField(primary_key=True)

    def __str__(self) -> str:
        return self.name+' '+str(self.Id)

class login(models.Model):
    username = models.TextField()
    password = models.TextField()

    def __str__(self) -> str:
        return self.username 

