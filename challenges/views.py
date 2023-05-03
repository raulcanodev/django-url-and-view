from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


# def january(request):
#     return HttpResponse('January')

# def february(request):
#     return HttpResponse('February')

# def march(request):
#     return HttpResponse('March')

def monthly_challenges(request, month):
    text = None
    if month == 'january':
        text = 'January text'
    elif month == 'february':
        text = 'February text'
    elif month == 'march':
        text = 'March text'
    else:
        return HttpResponseNotFound('Month not supported')
    return HttpResponse(text)
