from django.shortcuts import render


def index(request):
    context_dict = {'Danny': '/danny', 'Saph': '/saph', 'Fenix': '/fenix', 'Faolin':'/faolin', 'Rhanoct':'/rhanoct'}

    return render(request, 'index.html', {'data':context_dict.items})

def saph(request):
    context_dict = {}

    return render(request, 'saph.html', {'data':context_dict.items})

def danny(request):
    context_dict = {}

    return render(request, 'danny.html', {'data':context_dict.items})

def faolin(request):
    context_dict = {}

    return render(request, 'faolin.html', {'data':context_dict.items})

def fenix(request):
    context_dict = {}
    return render(request, 'fenix.html', {'data':context_dict.items})

def rhanoct(request):
    context_dict = {}
    return render(request, 'rhanoct.html', {'data':context_dict.items})

