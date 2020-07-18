from django.shortcuts import render
from .models import *
# Create your views here.
def makeentry(request):
    if request.method == "GET":
        return render(request, "makeentry.html")
    else:
        if request.method == "POST":
            fname1=request.POST.get('fname')
            lname1=request.POST.get('lname')
            email1=request.POST.get('email')
            mobile1=request.POST.get('mobile')
            company1=request.POST.get('company')
            loc1=request.POST.get('loc')

            data = customer(
                fname=fname1,
                lname=lname1,
                email=email1,
                mobile=mobile1,
                company=company1,
                loc=loc1
            )

            data.save()
        return render (request, 'customer.html')
def index(request):
    customers =customer.objects.all()
    return render(request, "customer.html",{"customer":customers})
def details(request,pk):
    details=customer.objects.get(id=pk)
    return render(request,"details.html",{"details":details})