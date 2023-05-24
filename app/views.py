from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1 style="color:blue">This is my first string response</h1>')
def second(request):
    return HttpResponse('<h1 style="color:red">This is my second string response</h1>')
def first_html(request):
    return render(request,'html1.html')
def second_html(request):
    return render(request,'html2.html')