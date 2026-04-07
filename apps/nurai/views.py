from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    html_content = """
    <h1>Моя страница</h1>
    <p>Привет, это моё фото:</p>
    <img src="/media/photos/me.jpg" alt="Моё фото" width="400">
    """
    return HttpResponse(html_content)

# Create your views here.
