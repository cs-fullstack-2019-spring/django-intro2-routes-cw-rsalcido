from django.http import HttpResponse



def index (request):
    return HttpResponse("Memphis All Day!")

def mycity (request):
    return HttpResponse("Memphis All Day!")

def myeats (request):
    return HttpResponse("Italian!")

def gogetthegood (request):
    return HttpResponse("Here you go! End of day!")

def happyhappyjoyjoy (request):
    return HttpResponse("A song title!")
