from django.shortcuts import render

def principal(request):
    return render(request, 'index/index.html',{})
# Create your views here.
