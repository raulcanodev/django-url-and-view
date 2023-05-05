from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    'december': None,
}
# Create your views here.


def index(request): # view in /challenges
    months = list(monthly_challenges.keys())
    
    return render(request, 'challenges/index.html', {
        'months': months,
    })


def monthly_challenge_by_number(request, month):
    # as the dictionary is sorted in python, we get the keys into a list
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Not btween 1 and 12')

    # then the month for the given int:month index in the previus sorted list
    redirect_month = months[month - 1] # deduct one from the month input therefore 1 = 0 = January
    redirect_path = reverse('month-challenges', args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)
    # HttpResponseRedirect: You can visit it but actually is not the final real 
    # url, you should be, here is that real url

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        
        return render(request, 'challenges/challenge.html', {
            'text' : challenge_text,
            'month' : month.capitalize(),
        })
    except:
        return HttpResponseNotFound('Month not found')
    
    
