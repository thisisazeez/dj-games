from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def drawing(request):
    return render(request, 'index.html')

def catch(request):
    return render(request, 'catch.html')

def quiz(request):
    return render(request, 'quiz.html')
