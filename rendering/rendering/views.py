# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': 'Yogesh Seralia', 'place': 'Alwar'}
    return render(request, 'index.html', params)
    # return HttpResponse("")
