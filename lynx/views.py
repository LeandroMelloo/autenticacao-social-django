from django.shortcuts import render

def home(request):
    return render(request, 'lynx/index.html')


def dashboard(request):
    return render(request, 'lynx/dashboard.html')
