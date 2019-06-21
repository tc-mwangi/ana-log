from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def log(request):
    return render(request, 'log.html')

def requestAjax(request):
    data = {
        'is_valid': False,
    }

    if request.is_ajax():
        message = request.Post.get('message')

        if message == 'I want an AJAX response':
            data.update(is_valid=True)

            data.update(response='This is the response you wanted')

    return JsonResponse(data)