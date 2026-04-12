from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request, 'index1.html')

def quiz_page(request):
    return render(request, 'quiz.html')

def about_page(request):
    return render(request, 'about.html')

# Create your views here.
