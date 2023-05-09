from django.shortcuts import render
import sys
import pandas as pd
import datetime
from datetime import date
sys.path.insert(1, 'Programs/covid_ml')


from covid_model import *
# Create your views here.

df = pd.read_csv('media/India.csv')

def input(request):
    return render(request, 'covid.html')


def result(request):
    dd = int(request.POST["DD"])
    mm = int(request.POST["MM"])
    yy = int(request.POST["YY"])

    date_fut = datetime.date(yy, mm, dd)
    date_fin = datetime.date(2023,3,9)
    today = int((date_fut - date_fin).days)
    
    if today > 0:
        today += max(df['Day'])
        res=(make_pred(today))
    else:
        res = 'Sorry Cant Predict Past !!!!'
    title = 'Covid Prediction'
    return render(request, "covid.html", {'title':title,'result': res})
