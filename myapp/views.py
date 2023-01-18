from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from myapp import support_functions
from myapp.models import *


# Create your views here.
def home(request):
    data = {}
    import datetime
    time=datetime.datetime.now()
    data["time_of_day"] = time
    print(time)
    return render(request, "home.html", context= data)

def maintenance(request):
    data = dict()
    try:
        choice = request.GET['selection']
        if choice == "currencies":
            support_functions.add_currencies(support_functions.get_currency_list())
            c_list = Currency.objects.all()
            print("Got c_list", len(c_list))
            data['currencies'] = c_list
            return HttpResponseRedirect(reverse('currencies'))
    except:
        pass
    return render(request,"maintenance.html",context=data)