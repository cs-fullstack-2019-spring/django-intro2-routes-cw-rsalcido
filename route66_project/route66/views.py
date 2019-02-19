from django.http import HttpResponse


# default function
def index (request):
    return HttpResponse("Memphis All Day!")

# function for mycity
def mycity (request):
    return HttpResponse("Memphis All Day!")

# function for myeats
def myeats (request):
    return HttpResponse("Italian!")

# new function
def gogetthegood (request):
    return HttpResponse("Here you go! End of day!")

# new function #2
def happyhappyjoyjoy (request):
    return HttpResponse("A song title!")
