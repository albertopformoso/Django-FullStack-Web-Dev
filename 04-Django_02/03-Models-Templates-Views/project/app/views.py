from django.shortcuts import render
from django.http import HttpResponse
from app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = dict(
        access_records=webpages_list
    )

    return render(request, 'app/index.html', context=date_dict)

def help(request):
    helpdict = dict(
        help_insert='HELP PAGE'
    )
    return render(request, 'app/help.html', context=helpdict)
