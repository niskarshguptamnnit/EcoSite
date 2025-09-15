from django.shortcuts import render , HttpResponse

# Create your views here.
"""def index(request):
    return HttpResponse("this is home page")
    """

def home(request):
    return render(request,'home.html')

def quiz(request):
    return render(request,'quiz.html')

def contest(request):
    return render(request,'contest.html')

def sustain(request):
    return render(request,'sustain.html')

def effects(request):
    return render(request,'effects.html')

def disaster(request):
    return render(request,'disaster.html')

def issues(request):
    return render(request,'issues.html')

def shop(request):
    return render(request,'shop.html')
def form(request):
    return render(request,'form.html')

