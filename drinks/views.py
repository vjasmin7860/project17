from django.shortcuts import render

# Create your views here.
def mazza(request):
    return render(request,'mazza.html')
def sprit(request):
    return render(request,'sprit.html')