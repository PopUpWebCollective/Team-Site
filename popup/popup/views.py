from django.shortcuts import render

def index(request):
    return render(request, 'popup/index.html')

def contact(request):
    return render(request, 'popup/contact.html')

def work(request):
    return render(request, 'popup/work.html')