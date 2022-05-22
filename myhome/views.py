import re
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'pages/home.html')
    # response = HttpResponse()
    # response.writelines('<h1>Xin chao</h1>')
    # response.write('Day la app home')
    # return response
