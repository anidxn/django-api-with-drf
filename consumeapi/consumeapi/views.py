from django.shortcuts import render, HttpResponse
# approach 1: using requests
import requests
# method 2: using urllib
from urllib import request as rq

# Create your views here.
def get_api_data(request):
    try:
        response = requests.get('http://127.0.0.1:8000/api/v1/companies/').json()
        return render(request, 'api_data.html', {'apidata' : response})
    except Exception as ex:
        print(ex)
        return render(request, 'api_data.html', {'err' : ex})


def home(request):
    response = rq.urlopen('http://127.0.0.1:8000/api/v1/companies/')
    if response.code ==200:
        # return HttpResponse("Status: OK")
        print("Status: OK")
        print("Returned : ", response)
        data = response.read()
        print(type(data))
        print('Length : ', len(data))
        print('Meta data ', response.peek())
    # content = data.decode("json")
    # print(content)
    return render(request, 'index.html')
