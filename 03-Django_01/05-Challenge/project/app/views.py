from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = dict(
        insert_me='Hello I am from views.py'
    )

    return render(request, 'app/index.html', context=my_dict)

def help(request):
    helpdict = dict(
        help_insert='HELP PAGE'
    )
    return render(request, 'app/help.html', context=helpdict)
