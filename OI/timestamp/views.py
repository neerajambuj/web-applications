from django.shortcuts import render
import json
import requests
from django.http import HttpResponse
# Create your views here.
def fetch_data(request):
    print("Fetching")
    URL = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
    #location = "delhi technological university"
    #PARAMS = {'address':location}
    r = requests.get(url = URL) #, params = PARAMS)
    data = r.json() 
    print(data)
    return HttpRequestResponse(json.dumps(data))
