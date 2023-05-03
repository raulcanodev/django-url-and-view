from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
    'january':'January connected',
    'february': 'February connected',
    'march': 'March connected',
    'april': 'April connected',
    'may': 'May connected',
    'june': 'June connected',
    'july': 'July connected',
    'august': 'August connected',
    'september': 'September connected',
    'october' : 'October connected',
    'november': 'November connected',
    'december': 'December connected',
}
# Create your views here.

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    challenge_text = monthly_challenges[month]
    return HttpResponse(challenge_text)
    
    
