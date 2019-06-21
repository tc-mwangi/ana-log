from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, render_to_response, HttpResponseRedirect
from django.contrib.auth import authenticate, login
import json
from django.http import JsonResponse
import random


def mygetview(request):
    if request.method == 'GET':

        print("**get**") 
        data = request.GET['mydata']
        astr = "<html><b> you sent a get request </b> <br> returned data: %s</html>" % data
        return HttpResponse(astr)
    return render(request)


def mypostview(request):
    if request.method == 'POST':

        print("**post**") 
        data = request.POST['mydata']
        astr = "<html><b> you sent a post request </b> <br> returned data: %s</html>" % data
        return HttpResponse(astr)
    return render(request)

def myajaxview(request):
    if request.method == 'POST':
        if request.is_ajax():
            print("**ajax post**")
            data = request.POST['mydata']
            astr = "<html><b> you sent an ajax post request </b> <br> returned data: %s</html>" % data
            return HttpResponse(astr)
    return render(request)


def myajaxformview(request):
    if request.method == 'POST':
        if request.is_ajax():
            import json

            print("**ajax form post**")
            for k, v in request.POST.items(): 
                print(k, v)

            print("field1 data: %s" % request.POST['field1'])
            print("field2 data: %s" % request.POST['field2'])

            mydata = [{'foo':1, 'baz':2}]
            return HttpResponse(json.dumps(mydata), mimetype="application/json")
    
    return render(request)


def foo(request,template='ajx/foo.html'):
    return render(request,template)















def index(request):  
    return render(request, 'index.html')


    # for N in range(1):
    #     N = random.randint(10,20)
    #     message = 'Start ' + 'N ' + 'servers'
    #     print(message)
    # return message 




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