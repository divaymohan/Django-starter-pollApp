#from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, World. You are at the polls index.")

# Create your views here.


def details(request, question_id):
    return HttpResponse("You'are looking at questtion %s." % question_id)


def result(request, question_id):
    response = "You are looking at the result of Question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("you are voting on question %s." % question_id)
