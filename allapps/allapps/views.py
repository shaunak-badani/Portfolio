from django.http import HttpResponse

def home(request):
    return HttpResponse("There's no place like home :)")

