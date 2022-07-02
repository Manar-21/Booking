from django import forms
from .models import Review, Form, Clinic, login
# from .models import Form_bones
# from .models import Form_children
from .models import Contact
import datetime

class Date_Clinic(forms.Form):
    date_clinic = forms.DateTimeField(initial=datetime.date.today)

class ReviewForm(forms.ModelForm):
    review_detail = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder":"Your Review *",
                "class": "form-control",
                "style": "width: 100%; height: 150px;"
            }
        ),
        label="",
    )

    class Meta:
        model = Review
        fields = ("review_detail", )

class loginReport(forms.ModelForm):
    username = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "class": "form-control",
                "style": "width: 100%; height: 40px;"
            }
        ),
        label="",
    )

    password = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "class": "form-control",
                "style": "width: 100%; height: 40px;"
            }
        ),
        label="",
    )

    class Meta:
        model = login
        fields = '__all__'

class ContactUs(forms.ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder":"Your Name *",
                "class": "contactus",
            }
        ),
        label="",
    )

    phone = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder":"Your Phone *",
                "class": "contactus",
          }
        ),
        label="",
    )

    email = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder":"Your Address *",
                "class": "contactus",
           }
        ),
        label="",
    )
    message = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder":"Your Message *",
                "class": "textarea",
          }
        ),
        label="",
    )
    
    class Meta:
        model = Contact
        fields = ("name", "phone", "email", "message", )


class AppointmentForm(forms.ModelForm):
    name = forms.CharField(
            required=True,
            widget=forms.widgets.Textarea(
                attrs={
                    "placeholder":"Your Name *",
                    "class": "form-control",
                    "style": "width: 100%; height: 40px;"
                }
            ),
            label="",
        )

    address = forms.CharField(
            required=True,
            widget=forms.widgets.Textarea(
                attrs={
                    "placeholder":"Your Address *",
                    "class": "form-control",
                    "style": "width: 100%; height: 40px;"
            }
            ),
            label="",
        )

    phone = forms.CharField(
            required=True,
            widget=forms.widgets.Textarea(
                attrs={
                    "placeholder":"Your Phone *",
                    "class": "form-control",
                    "style": "width: 100%; height: 40px;"
            }
            ),
            label="",
        )
        
    notes = forms.CharField(
            widget=forms.widgets.Textarea(
                attrs={
                    "placeholder":"Your Notes *",
                    "class": "form-control",
                    "style": "width: 100%; height: 40px;"
                }
            ),
        label="",
    )
    class Meta:
        model = Form
        exclude = ('date','Id')

        

