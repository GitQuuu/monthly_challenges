from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

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
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")



def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())

        if month > len(months):
            return HttpResponseNotFound("This month is not supported")

        redirect_month = months[month - 1]
        return HttpResponseRedirect("/challenges/" + redirect_month)
    except:
        return HttpResponseNotFound("This month is not supported")