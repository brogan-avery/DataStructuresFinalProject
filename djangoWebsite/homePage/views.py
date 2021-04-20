from django.shortcuts import render

def index(request):
    template = "homePage/index.html"
    return render(request,template)
