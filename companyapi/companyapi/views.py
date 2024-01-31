from django.http import HttpResponse, JsonResponse

from django.core import serializers

def home_page(request):
    #print('Home page requested')
    
    """
    names = [
        'anil','sumit','rahul'
    ]

    return JsonResponse(names, safe=False) # to allow non-dict objects to be serialized set safe = False
    """

    names = {"r01": "anil",
             "r02": "sumit",
             "r03": "rahul"}
    return JsonResponse(names)

    """
    data = serializers.serialize('json', names)
    return HttpResponse(data, content_type='application/json')
   """ 

#above approach is good when creating 2-3 apis
# but while creating entire backend with api s use the DRF