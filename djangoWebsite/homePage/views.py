from django.shortcuts import render
from django.http import HttpResponse
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

def index(request):
    template = "homePage/index.html"
    return render(request,template)
