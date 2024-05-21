from django.shortcuts import redirect, render, HttpResponse
# approach 1: using requests
import requests
# method 2: using urllib
from urllib import request as rq

#----- for messages framework -------
from django.contrib import messages

# GET request
def get_api_data(request):
    url = 'http://127.0.0.1:8085/api/v1/companies/'
    try:
        response = requests.get(url) #.json()
        if response.status_code == 200:
            data = response.json()
            return render(request, 'api_data.html', {'apidata' : data})

    except Exception as ex:
        print(ex)
        messages.warning(request, "Some error occured, check logs for details")
        return render(request, 'api_data.html') # {'err' : ex}
    
# ------------- POST -----------------
def do_post_data(request):
    url = 'http://127.0.0.1:8085/api/v1/companies/'

    try:

        if request.method == "POST":
            # get data from form
            cname = request.POST.get('txtName')
            clocation = request.POST.get('txtLoc')
            cabout = request.POST.get('txtAbout')
            ctype = request.POST.get('ddlType')
            # cstatus = request.POST.get('rating') checkbox handling later

            payload = {
                'name': cname,
                'location': clocation,
                'about': cabout,
                'type': ctype,
                'active' : True
            }

            response = requests.post(url, json = payload)  # send as JSON
    
            if response.status_code == 201:   # ***201
                data = response.json()   # returns a dictionary object with all the details of newly added object including Primary Key & auto updated values
                print(data)
                messages.success(request, "Details stored successfully with ID: " + str(data["company_id"]) + " at time: " + str(data["added_date"]))
                # return data
            else:
                messages.warning(request, "Failed to save data..remote server did not respond properly")
                #return None
    
    except Exception as ex:
        print(ex)
        messages.warning(request, "Some error occured during save, pls check log for more details")
    
    # render in all cases
    return render(request, 'company_add.html')


# --------------- PUT = update all----------------------
def do_put_data(request, compid):
    url = 'http://127.0.0.1:8085/api/v1/companies/' + str(compid) + '/'  # must teminate with /

    if request.method == "POST":
        
        # get data from form
        cname = request.POST.get('txtName')
        clocation = request.POST.get('txtLoc')
        cabout = request.POST.get('txtAbout')
        ctype = request.POST.get('ddlType')
        # cstatus = request.POST.get('rating') checkbox handling later

        payload = {
            'name': cname,
            'location': clocation,
            'about': cabout,
            'type': ctype,
            'active' : True
        }

        response = requests.put(url, json = payload)  # send as JSON

        if response.status_code == 200:   # response 200
            data = response.json()   # returns a dictionary object with all the details of newly added object including Primary Key & auto updated values
            print(data)
            # return data
            messages.success(request, "Details updated successfully with Name: " + str(data["name"]) + ", Location: " + str(data["location"])+ ", About: " + str(data["about"]))
            
        else:
            messages.warning(request, "Some error occured during update, check logs for details")
            #return None

        return redirect('/getdata')  # redirect to view all

    else:  # * * * * * * * get details of the selected company by API Call  * * * * * * * 

        response = requests.get(url) #.json()
        if response.status_code == 200:
            data = response.json()
            return render(request, 'company_edit.html', {'apidata' : data})
        

# --------------- PATCH (limited fields)----------------------
def do_patch_data(request, compid):
    url = 'http://127.0.0.1:8085/api/v1/companies/' + str(compid) + '/'  # must teminate with /

    cname = request.POST.get('txtName')

    payload = {
        'name': cname
    }
    response = requests.patch(url, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


# --------------- DELETE (One)----------------------
def do_delete_data(request, compid):
    url = 'http://127.0.0.1:8085/api/v1/companies/' + str(compid) + '/'

    try:
        response = requests.delete(url)
    
        if response.status_code == 204:
            messages.success(request, "Details deleted successfully")
        else:
            messages.warning(request, "Failed to delete resource..remote server did not respond properly")
    except Exception as ex:
        print(ex)
        messages.warning(request, "Some error occured during delete, check logs for details")

    return redirect('/getdata')



#-============ using URLLIB ======================
def home(request):
    try:
        response = rq.urlopen('http://127.0.0.1:8085/api/v1/companies/')
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
    except Exception as ex:
        messages.warning(request, "Some error occured")
    return render(request, 'index.html')
