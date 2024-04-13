from django.shortcuts import render

# Create your views here.
def biryani(request):
    return render(request,'biryani.html')
def parota(request):
    return render(request,'parota.html')