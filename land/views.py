from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')


def faq(request):
    return render(request,'faq.html')


def contact_us(request):
    return render(request,'contactus.html')


def form_job(request):
    return render(request,'formjob.html')


def form_freelance(request):
    return render(request,'formfreelance.html')