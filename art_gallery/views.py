from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'art_gallery/home.html')