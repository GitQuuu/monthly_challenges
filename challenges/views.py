from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
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
    "august": "We miss .Net",
    "september": "And Angular",
    "october": "But we can do it",
    "november": "Python has a bit og resembling to the vsa pattern",
    "december": None,
}


# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month": month,
            "challenge": challenge_text
        })
    except:
        raise Http404()


def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())

        if month > len(months):
            return HttpResponseNotFound("This month is not supported")

        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        raise Http404()
