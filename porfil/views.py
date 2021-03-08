from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(req):
    return render(req, 'index.html')
    # return HttpResponse("Home")

def analyzeText(req):
    textt = req.POST.get('text', 'default')
    rempunc = req.POST.get('Remove Punctuation', 'off')
    # cap = req.POST.get('Start with capital', 'off')
    capitalize = req.POST.get('capitalize', 'off')
    # lower = req.POST.get('lower', 'off')
    extraspaceremover = req.POST.get('extraspaceremover', 'off')

    analyzed = ""
    if rempunc == "on":
        punctuations = '''~`!@#$%^&*()_+-={}[]|\:';"<>?,./'''
        for c in textt:
            if c not in punctuations:
                analyzed += c
    else:
        analyzed = textt
    # if cap == "on":
    #     analyzed=analyzed.capitalize()
    if capitalize=="on":
        cap="off"
        lower="off"
        analyzed=analyzed.upper()
    # if lower=="on":
    #     analyzed=analyzed.lower()
    if extraspaceremover=="on":
        analyzed2=""
        for i in range(len(analyzed)):
            if not (analyzed[i]==' ' and analyzed[i+1]==' '):
                analyzed2+=analyzed[i]
        analyzed=analyzed2

    params = {"analyzed_text": analyzed,"count":len(analyzed)}
    return render(req, "analyze.html", params)
