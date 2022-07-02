from django.shortcuts import render
from appointments.models import Clinic, Form, Review, login
from appointments.forms import ReviewForm, AppointmentForm, loginReport, ContactUs, Date_Clinic
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def virtual_tour(request):
    return render(request, 'virtual_tour.mp4')

def Appointment(request):
    return render(request, 'Appointment.html')

def id(request):
    form = Form.objects.all().last()
    print(form)
    print(form.Id)
    print(form.name)
    print(form.clinic)
    return render(request, 'id.html', {'form':form})

def form(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointments = form.save()
            return render(request, 'form.html', {"form": form})

    form = AppointmentForm()
    return render(request, 'form.html', {"form": form})

def report(request):
    from datetime import date

    date = date.today()
    # date = date(2022, 6, 17)
    data = {'clinics':[]}
    
    clinics = Clinic.objects.filter().distinct()

    # clinics = Clinic.objects.filter(appointments__date=date).distinct()
    # clinics = Clinic.objects.all()

    for clinic in clinics:
        # count = Form.objects.filter(clinic=clinic, date=date).count()
        count = Form.objects.filter(clinic=clinic).count()
        clinic_detail = {'clinic_name':clinic.name, 'clinic_id':clinic.id, 'count':count}
        data['clinics'].append(clinic_detail)
    
    return render(request, 'report_index.html', {'clinics': data})

def report_daily(request, date):
    
    from datetime import date

    # date = date.todays()
    date = date(2022, 6, 17)
    data = {'clinics':[]}
    
    # clinics = Clinic.objects.filter().distinct()

    clinics = Clinic.objects.filter(appointments__date=date).distinct()
    print(clinics)
    # clinics = Clinic.objects.all()

    for clinic in clinics:
        # count = Form.objects.filter(clinic=clinic, date=date).count()
        count = Form.objects.filter(clinic=clinic, date=date).count()
        clinic_detail = {'clinic_name':clinic.name, 'clinic_id':clinic.id, 'count':count}
        data['clinics'].append(clinic_detail)
    
    return render(request, 'report_daily.html', {'clinics': data})

def dateClinic(request):
    Date = Date_Clinic()
    if request.method == "POST":
        form = DateClinic(request.POST)
        if form.is_valid():
            DateClinic = form.save()
            DateClinic = (2022, 6, 17)
            print('noor')
            print(DateClinic)
            report_daily(DateClinic)

    print('manar')
    return render(request, 'report_daily.html', {'Date':Date})


def ReviewView(request):
    if request.method == "POST":
        print("in poost")
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            print(review.review_detail)
            return render(request, 'Review.html', {"form": form})

    form = ReviewForm()
    return render(request, 'Review.html', {"form": form})


def ApppintmentReviews(request):
    reviews =  Review.objects.all()

    return render(request, 'ApppintmentReviews.html', {'reviews': reviews})

# def reportindex(request):
#     return render(request, 'report_index.html')

def login_report(request):
    from datetime import date
    date = date.today()

    # data = {'clinics':[]}
    # clinics = Clinic.objects.filter(appointments__date=date).distinct()
    # for clinic in clinics:
    #     count = Form.objects.filter(clinic=clinic, date=date).count()
    #     clinic_detail = {'clinic_name':clinic.name, 'clinic_id':clinic.id, 'count':count}
    #     data['clinics'].append(clinic_detail)

    data = {'clinics':[]}
    
    clinics = Clinic.objects.filter().distinct()

    form = loginReport()
    users = login.objects.all()
    if request.method=="POST":
        form = loginReport(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for i in range(login.objects.all().count()):
                if (cd['username'] == str(users[i].username)) and (cd['password'] == str(users[i].password)) :
                    for clinic in clinics:
                        # count = Form.objects.filter(clinic=clinic, date=date).count()
                        count = Form.objects.filter(clinic=clinic).count()
                        clinic_detail = {'clinic_name':clinic.name, 'clinic_id':clinic.id, 'count':count}
                        data['clinics'].append(clinic_detail)
                    
                    return render(request, 'report_index.html', {'clinics': data})

    return render(request, 'login_report.html', {'form':form})


    # if request.method == "POST":
    #     form = login_report(request.POST)
    #     if form.is_valid():
    #         login = form.save()
    #         # print(appointments.appointment_form)
    #         return render(request, 'login_report.html', {"form": form})

    # form = login_report()
    # return render(request, 'login_report.html', {"form": form})

def Emergency(request):
    return render(request, 'Emergency.html')

def Login(request):
    return render(request, 'Login.html')

def contact(request):
    if request.method == "POST":
        form = ContactUs(request.POST)
        if form.is_valid():
            contact = form.save()
            # print(appointments.appointment_form)
            return render(request, 'contact.html', {"form": form})

    form = ContactUs()
    return render(request, 'contact.html', {"form": form})


import os

classes = {"NORMAL" : "Normal" ,
         "PNEUMONIA" : "Pneumonia"}


def preprocessing(path):
    img = cv2.imread(path)
    img = cv2.resize(img,(224,224))
    img = np.reshape(img,[1,224,224,3])

# import tensorflow

def predict(img):
    model = load_model('/chest.h5')
    clf = classes = model.predict(img)
    return clf

def clf(img):
    if (img==1):
        return 'Normal'
    else :
        return 'Normal'

def home(request):
    if request.method == "POST":
        # name = request.POST["name"]
        # age  = request.POST["date"]
        file_path = request.POST["file"]
        print(file_path)
        # data = preprocessing(file_path)
        # cls  = predict(data)
        # print(cls)
        # desease = classes[str(cls)]
        desease = clf(file_path)
        return render(request , "predict.html" , {"submitted" : True , "desease" : desease})
    else:
        return render(request , "ChestX-Ray.html" , {"submitted" : False , "desease" : 'Normal'})

