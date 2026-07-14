from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

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

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{month.capitalize()}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge(request, month):
    # try:
        challenge_text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    # except:
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