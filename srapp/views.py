from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import SalesData
from django.contrib import messages

# Create your views here.

def index(request):
    # Founction for showing total amount of sales started here
    byte = SalesData.objects.all().count()
    bts = {'byte':byte}

    # Functions to sumbit software value in data base 

    if request.method == 'POST':
        sno = request.POST['sno']
        Date = request.POST['Date']
        Costumer_Id = request.POST['Costumer_Id']
        Costumer_Name = request.POST['Costumer_Name']
        email = request.POST['email']
        Alt_email = request.POST['Alt_email']
        phone = request.POST['phone']
        Alt_phone = request.POST['Alt_phone']
        Address = request.POST['Address']
        Service = request.POST['Service']
        Price = request.POST['Price'] 

         # cheacks to all valuse in costumer data 

        if len(Costumer_Name)<2:
            messages.error(request,'User name not blank and less than 2 charcters. please try again')
            return render(request,'index.html')

        if SalesData.objects.filter(Costumer_Id=Costumer_Id).exists():
            messages.error(request,'Costumer id alredy exits please try again deffrent costumer id')
            return render(request,'index.html')

        if len(phone)<10:
            messages.error(request,'phone no. not accepted less than 10, please enter the valid phone number')
            return render(request,'index.html')    

        if SalesData.objects.filter(sno=sno).exists():
            messages.error(request,'Sno. alredy exists please try agin deffrent Sno.')
            return render(request,'index.html')  

        if email == "":
            messages.error(request,'email not blank please fill again')
            return render(request,'index.html')   

        if Address == "":
            messages.error(request, "you can't live blank address please try again")
            return render(render,'index.html')   

        if Service == "":
            messages.error(request,"you can't live blank service please try again")
            return render(request,'index,html')

        if Price == "":
            messages.error(request,"you can't live blank price please try again")
            return render(request,'index,html')        

        savedata = SalesData(sno=sno, Date=Date, Alt_email=Alt_email ,Alt_phone=Alt_phone, Costumer_Id=Costumer_Id,Costumer_Name=Costumer_Name,email=email,phone=phone,Address=Address,Service=Service,Price=Price)
        savedata.save()
        messages.success(request,'you data add successfily. Thank you for use our software.')


    return render(request,'index.html',bts)


# costumer data start hare 

def CostumerData(request):
    byte = SalesData.objects.all().count()
    Sales = SalesData.objects.all()
    # print(Sales)
    Context = {'Sales':Sales,'byte':byte}
    return render(request,"CostumerData.html",Context)



# heandl Search here 

def Search(request):
    byte = SalesData.objects.all().count()
    quary = request.GET['quary']
    if quary == "":
        messages.warning(request,"You can't search black value. please try again later.")
        return render(request,"index.html")
    Sales = SalesData.objects.filter(Costumer_Id__icontains=quary) 
    Context = {'Sales':Sales,'byte':byte}
    return render(request,'Search.html',Context)
    
    