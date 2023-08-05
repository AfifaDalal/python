from django.shortcuts import render
from django.http import HttpResponse
from .models import pm

# Create your views here.
def home(request):
	return render(request,'form.html')

def saveData(request):
	p1=pm()
	p1.fname=request.GET.get('fname')
	p1.lname=request.GET.get('lname')
	p1.email=request.GET.get('email')
	p1.contactno=request.GET.get('contactno')
	p1.save()
	return HttpResponse('<h1>Data Saved</h1>')

def getData(request):
	data=pm.objects.all()

	dic={'fname':'Afifa', 'lname':'Dalal'}	
	return render(request,'display.html',{'Data': data})
		
		# p1=pm(fname=fname, lname=lname, email=email, contactno=contactno)
		# p.save()