from django.shortcuts import render,HttpResponse


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    context = {
        'message':''
    }
    return render(request,'about.html')

def contact(request):
    context = {
        'Mobile_no':9421346789,
        'Email':'nirmswami67@gmail.com',
        'Address':'B wing, benchmark,Nirmal Bazar',
        'office_Location':'Suite 02, Level 12, Sahera Tropical Center'
        

    }
    return render(request,'contact_us.html',context)    
    