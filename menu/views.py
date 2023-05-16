from django.shortcuts import render

# Create your views here.
def uno(request):
    return render(request,'menu/uno.html')