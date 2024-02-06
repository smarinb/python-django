from django.http import HttpResponse
def hello(request):
    return HttpResponse("Hello World")

def bie(request):
    return HttpResponse("Good Bie")

def adult(request, age):
    if(age>=18):
        return HttpResponse("You are upper 18")
    else:
        return HttpResponse("You are not upper 18")