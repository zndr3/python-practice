from django.shortcuts import render
from django.http import HttpResponse # type: ignore

def members(request):
    return HttpResponse("Hello world!")