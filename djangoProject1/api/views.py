from django.http import HttpResponse
from django.shortcuts import redirect

def home(request):
    return HttpResponse("Welcome to the home page!")


def redirect_to_api(request):
    return redirect('/api/note/')
