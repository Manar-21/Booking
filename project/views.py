from django.shortcuts import render
from appointments.models import *
from appointments.forms import *
from itertools import chain
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def Appointment(request):
    return render(request, 'Appointment.html')

def ApppintmentReviews(request):
    reviews =  Review.objects.all()
    return render(request, 'ApppintmentReviews.html', {'reviews': reviews})

def Login(request):
    return render(request, 'Login.html')

def ReviewView(request):
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            print(review.review_detail)
            return render(request, 'Review.html', {"form": form})

    return render(request, 'Review.html', {"form": form})

def contact(request):
    form = ContactUs()
    if request.method == "POST":
        form = ContactUs(request.POST)
        if form.is_valid():
            contact = form.save()
            return render(request, 'contact.html', {"form": form})

    return render(request, 'contact.html', {"form": form})

def idSaturday(request):
    data = {'clinics':[]}
    count = 0
    person = saturday.objects.filter().last()

    for cl in saturday.objects.all():
        if cl.clinic==person.clinic:
            count = count+1
    
    return render(request, 'idSat.html', {'person': person, 'count':count})

def idSunday(request):
    data = {'clinics':[]}
    count = 0
    person = sunday.objects.filter().last()

    for cl in sunday.objects.all():
        if cl.clinic==person.clinic:
            count = count+1
    
    return render(request, 'idSun.html', {'person': person, 'count':count})

def idMonday(request):
    data = {'clinics':[]}
    count = 0
    person = monday.objects.filter().last()

    for cl in monday.objects.all():
        if cl.clinic==person.clinic:
            count = count+1
    
    return render(request, 'idMon.html', {'person': person, 'count':count})

def idTuesday(request):
    data = {'clinics':[]}
    count = 0
    person = Tuesday.objects.filter().last()

    for cl in Tuesday.objects.all():
        if cl.clinic==person.clinic:
            count = count+1
    
    return render(request, 'idTue.html', {'person': person, 'count':count})

def idThursday(request):
    data = {'clinics':[]}
    count = 0
    person = thursday.objects.filter().last()

    for cl in thursday.objects.all():
        if cl.clinic==person.clinic:
            count = count+1
    
    return render(request, 'idThu.html', {'person': person, 'count':count})

def idWednesdayy(request):
    data = {'clinics':[]}
    count = 0
    person = wednesday.objects.filter().last()

    for cl in wednesday.objects.all():
        if cl.clinic==person.clinic:
            count = count+1
    
    return render(request, 'idWed.html', {'person': person, 'count':count})


def Saturday(request):
    form = AppointmentFormSatrday()
    if request.method == "POST":
        form = AppointmentFormSatrday(request.POST)
        if form.is_valid():
            appointments = form.save()
            return render(request, 'Saturday.html', {"form": form})

    return render(request, 'Saturday.html', {"form": form})

def Sunday(request):
    form = AppointmentFormSunday()
    if request.method == "POST":
        form = AppointmentFormSunday(request.POST)
        if form.is_valid():
            appointments = form.save()
            return render(request, 'Sunday.html', {"form": form})

    return render(request, 'Sunday.html', {"form": form})

def Monday(request):
    form = AppointmentFormMonday()
    if request.method == "POST":
        form = AppointmentFormMonday(request.POST)
        if form.is_valid():
            appointments = form.save()
            return render(request, 'Monday.html', {"form": form})

    return render(request, 'Monday.html', {"form": form})

def Tuesday(request):
    form = AppointmentFormTuesday()
    if request.method == "POST":
        form = AppointmentFormTuesday(request.POST)
        if form.is_valid():
            appointments = form.save()
            return render(request, 'Tuesday.html', {"form": form})

    return render(request, 'Tuesday.html', {"form": form})

def Thursday(request):
    form = AppointmentFormThursday()
    if request.method == "POST":
        form = AppointmentFormThursday(request.POST)
        if form.is_valid():
            appointments = form.save()
            return render(request, 'Thursday.html', {"form": form})

    return render(request, 'Thursday.html', {"form": form})

def Wednesday(request):
    form = AppointmentFormWednesday()
    if request.method == "POST":
        form = AppointmentFormWednesday(request.POST)
        if form.is_valid():
            appointments = form.save()
            return render(request, 'Wednesday.html', {"form": form})

    return render(request, 'Wednesday.html', {"form": form})

def login_report(request):
    form = loginReport()
    users = login.objects.all()
    if request.method=="POST":
        form = loginReport(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for i in range(login.objects.all().count()):
                if (cd['username'] == str(users[i].username)) and (cd['password'] == str(users[i].password)) :                    
                    return render(request, 'report_index.html')

    return render(request, 'login_report.html', {'form':form})

def report(request, date):
    return render(request, 'report_index.html')

def report_weekly(request):
    from datetime import date
    date = date.today()
    data = {'clinics':[]}    
    clinic = Clinic_a.objects.filter().distinct()
    clinic1 = Clinic_bSatrday.objects.filter().distinct()
    clinic2 = Clinic_cSunday.objects.filter().distinct()
    clinics = list(chain(clinic1,clinic2))
    day1 = saturday
    day2 = sunday
    day3 = monday
    day4 = tuesday
    day5 = wednesday
    day6 = thursday
    days = list((day1, day2, day3, day4, day5, day6))

    # for cl in clinic: 
    #     # print(cl)
    #     count = 0
    #     for d in days:
    #         print('norhan\n')
    #         print(cl, "  ",d, "  ", count,'\n')
    #         print('manar  ' ,clinic, '\n')
    #         count = d.objects.filter(clinic=cl).count() 
    #         # except :
    #         #     print("manar ", cl , "  ",d, '\n')
    #     print(count, '\n')
    #     clinic_detail = {'clinic_name':cl.name, 'clinic_id':cl.id, 'count':count}
    #     data['clinics'].append(clinic_detail)
    #     # print(data)

    # return render(request, 'report_weekly.html', {'clinics': data})

    # print('\n', saturday, '\n')
    # print('\n', days)

    # print(Clinic_Satrday)
    # print(Clinic_a)
    # print(clinic)
    for cl in clinic:
        # print(cl)
        # print(cl.id)
        # print(cl.name)
        # count = 0
        # for d in days:
        # print(saturday)
            # print(d)
        count = saturday.objects.filter(clinic=cl.id).count()
            # print(count)
            # print(cl.name)
        # print(count)
        # print('clinic_name',cl.name, 'clinic_id',cl.id, 'count',count)
        clinic_detail = {'clinic_name':cl.name, 'clinic_id':cl.id, 'count':count}
        data['clinics'].append(clinic_detail)
    # print(data)
    # return JsonResponse(data, status=200)
    return render(request, 'report_weekly.html', {'clinics': data})

    # for cl in clinic:
    #     # print('\n\n')
    #     # print(clinic)
    #     # print('\n\n')
    #     # print(cl)
    # count = 0
    # mon = Clinic_Monday.objects.filter().distinct()

    # for cl in mon:
    #         # print(cl)
    #         # for cl in 
    #     for d in days:
    #             # print('\n\n')
    #             # print(days)

    #             # print('\n\n')
    #             # print(d)
    #             #  print(cl.objects.filter().distinct())
    #         try:
    #                 # print(cl[j])
    #                 # print(d)
    #             count = d.objects.filter(clinic=cl).count() + count
    #                 # clinic_detail = {'clinic_name':cl[j].name, 'clinic_id':cl[j].id, 'count':count}
    #                 # data['clinics'].append(clinic_detail)

    #                 # print(cl[j].name)
    #         except :
    #             continue
    #     print('clinic_name',cl.name, 'clinic_id',cl.id, 'count',count)
    #     clinic_detail = {'clinic_name':cl.name, 'clinic_id':cl.id, 'count':count}
    #     data['clinics'].append(clinic_detail)

    # print(data)

    # return render(request, 'report_weekly.html', {'clinics': data})


    # for cl in clinic:
    #     # print('\n\n')
    #     # print(clinic)
    #     # print('\n\n')
    #     # print(cl)
    #     count = 0
    #     for j in range(cl.count()):
    #         # print(cl)
    #         # for cl in 
    #         for d in days:
    #             # print('\n\n')
    #             # print(days)

    #             # print('\n\n')
    #             # print(d)
    #             #  print(cl.objects.filter().distinct())
    #             try:
    #                 # print(cl[j])
    #                 # print(d)
    #                 count = d.objects.filter(clinic=cl[j]).count() + count
    #                 # clinic_detail = {'clinic_name':cl[j].name, 'clinic_id':cl[j].id, 'count':count}
    #                 # data['clinics'].append(clinic_detail)

    #                 # print(cl[j].name)
    #             except :
    #                 continue
    #         # print('clinic_name',cl[j].name, 'clinic_id',cl[j].id, 'count',count)
    #         clinic_detail = {'clinic_name':cl[j].name, 'clinic_id':cl[j].id, 'count':count}
    #         data['clinics'].append(clinic_detail)

def report_daily(request):
    from datetime import date
    date = date.today()
    data = {'clinics':[]}
    clinics = Clinic_Sunday.objects.filter().distinct()
    print(clinics)
    print('\n', Form)

    for clinic in clinics:
        count = Form.objects.filter(clinic=clinic).count()
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

