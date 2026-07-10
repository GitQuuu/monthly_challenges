from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

def monthly_challenge(request, month):
    challenge_month = None

    if month == "january":
        challenge_month = "Start learning python"
    elif month == "february":
        challenge_month = "And Django"
    elif month == "march":
        challenge_month = "Make webapi"
    elif month == "april":
        challenge_month = "Integrate frontend"
    else:
        return HttpResponseNotFound("Not supported yet")
    return HttpResponse(month)