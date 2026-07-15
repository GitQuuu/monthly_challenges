from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


monthly_challenges = {
    "January": "Start learning python",
    "February": "And Django",
    "March": "Make webapi",
    "April": "Integrate frontend",
    "May": "Learn more about Django",
    "June": "for webapi",
    "July": "Make webapi",
    "August": "We miss .Net",
    "September": "And Angular",
    "October": "But we can do it",
    "November": "Python has a bit og resembling to the vsa pattern",
    "December": "Make webapi",
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
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": month,
            "value": challenge_text
        })
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