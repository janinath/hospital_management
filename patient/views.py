from django.shortcuts import render,redirect
from random import randint
from django.core.mail import send_mail
from . models import *
from doctor.models import *
from django.conf import settings
# Create your views here.
def Home(request):
    return render(request,'patient/home.html')
def Booking(request):
    doctors=Doctor.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        date=request.POST['date']
        time=request.POST['time']
        message=request.POST['message']
        doctor_id=request.POST['doctor']
        doctor=Doctor.objects.get(id=doctor_id)
        appointment=Appointment(name=name,date=date,time=time,email=email,doctor=doctor,message=message,status='waiting')
        appointment.save()
        return render(request,'patient/booking.html',{'msg':'Your Appointment updation will be added in APPOINTMENT LIST'})
    return render(request,'patient/booking.html',{'doctors':doctors})
def List(request):
    patients=Appointment.objects.filter(status='confirmed')
    return render(request,'patient/list.html',{'patients':patients})
def Login(request):
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']
        patient_exist = Patient.objects.filter(email=email,password=password).exists()
        if patient_exist :
            patient = Patient.objects.get(email=email,password=password)
            request.session['patientid']=patient.id
            if patient.status == 'toverify':
                otp = randint(1000,9999)
                send_mail(
            'please verify your otp',
                str(otp),
                settings.EMAIL_HOST_USER,
                [patient.email]
                )
                patient.otp=otp
                patient.save()
                return redirect('patient:otp')
            else :
                return redirect('patient:booking')
        else :
                return render(request, 'patient/login.html', {'msg':'invalid email or password'})
    
    return render(request,'patient/login.html')
def Signup(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        patient_exist=Patient.objects.filter(email=email)
        if not patient_exist:
            otp= randint(1000,9999)
            send_mail(
                'please verify your otp',
                str(otp),
                settings.EMAIL_HOST_USER,
                [email]
                )
        patient=Patient(name=name,email=email,password=password,otp=otp,status='toverify')
        patient.save()
        request.session['patientid']=patient.id
        return redirect('patient:otp')
    return render(request,'patient/signup.html')
def otp(request):
    if request.method == 'POST' :
        otp = request.POST['otp']
        c_id = request.session['patientid']
        patient =Patient.objects.get(id=c_id)
        if otp==patient.otp :
            Patient.objects.filter(id=c_id).update(status='verified')
            return redirect('patient:booking')
        else :
            return render (request,'patient/otp.html' ,{'msg':'invalid otp'})
    return render(request, 'patient/otp.html')