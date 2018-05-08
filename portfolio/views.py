from django.shortcuts import render
from django.http import HttpResponse

def Index(request):
    return render(request, 'index.html', context=None)

def CollegeCareerReadiness(request):
    return render(request, 'collegeCareerReadiness.html', context=None)

def CommunityConnections(request):
    return render(request, 'communityConnections.html', context=None)

def InterdisciplinaryConnections(request):
    return render(request, 'interdisciplinaryConnections.html', context=None)

def RigorousThinking(request):
    return render(request, 'rigorousThinking.html', context=None)
