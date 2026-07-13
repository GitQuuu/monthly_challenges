from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
    "january": "Start learning python",
    "february": "And Django",
    "march": "Make webapi",
    "april": "Integrate frontend",
    "may": "Learn more about Django",
    "june": "for webapi",
    "july": "Make webapi",
    "august": "Make webapi",
    "september": "forwebapi",
    "october": "Make webapi",
    "november": "Make webapi",
    "december": "Make webapi",
}

# Create your views here.

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")



def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())

        if month > len(months):
            return HttpResponseNotFound("This month is not supported")

        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("This month is not supported")