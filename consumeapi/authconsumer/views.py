from django.shortcuts import render, redirect
import requests
import json # for storing to file in json format

#----- for messages framework -------
from django.contrib import messages

# ==============================================================================
#                       USER AUTHENTICATION
# ==============================================================================

def registeruser(request):
    regurl = "http://localhost:8088/api/register/"

    if request.method == "POST":
        uname = request.POST.get('txtUname')
        upass = request.POST.get('txtUpass')
        uemail = request.POST.get('txtEmail')
        
        payload = {
            'username': uname, 
            'password': upass,
            'email' : uemail
        }

        try:
            response = requests.post(regurl, json = payload)  # response contains login token

            if response.status_code == 201:
                
                # Extract the token from the response
                # token =  response.json().get('token')

                # Save token to a file
                # with open('token.json', 'w') as file:
                #     json.dump({'token': token}, file)

                #set a msg
                messages.success(request, "User registration successfull")
                # redirect to login page
                return redirect('login-user')
            else:
                messages.warning(request, "Failed to save data.")
        except Exception as ex:
            print(ex)
            messages.warning(request, "An error occurred during the save process.")

    return render(request, 'register.html')

# ============ LOGIN ================
# @csrf_exempt  ??????

def loginuser(request):
    loginurl = 'http://localhost:8088/api/login/'

    if request.method == "POST":
        uname = request.POST.get('txtUname')
        upass = request.POST.get('txtUpass')
        
        credentials = {
            'username': uname, 
            'password': upass
        }

        try:
            response = requests.post(loginurl, json = credentials)  # response contains login token

            if response.status_code == 200:
                
                # Extract the token from the response
                # token =  response.json().get('token')
                # OR
                data = response.json()
                token = data['token']

                print('Token is ============== ' + token)

                # Save the token for future API calls -
                # Option 1: in session
                request.session['authToken'] = token
                request.session['active_uname'] =  data['act_uname']  # 'PD USER' #
                

                """ # Option 2: in a file
                with open('token.json', 'w') as file:
                    json.dump({'token': token}, file)
                """

                #set a msg
                messages.success(request, "Login successfull")
                # redirect to dashboard
                return redirect('get-data')
            else:
                messages.warning(request, "Incorrect credential, please try again.")
        except Exception as ex:
            print(ex)
            messages.warning(request, "An error occurred during login. Please try again")

    # render login page
    return render(request, 'login.html')


# ============== LOGOUT =================
def logoutuser(request):

    # Load token 
    # Option 1: from session
    token = request.session.get('authToken', None)

    """ Option 2: from a filefrom file
    with open('token.json', 'r') as file:
        data = json.load(file)
        token = data['token']
    """

    if token:
        print('Token to destroy ================== ' + token)
        # Use the token for subsequent requests
        headers = {
            'Authorization': f'Token {token}'
        }

        logouturl = 'http://localhost:8088/api/logout/'
        
        try:
            response = requests.post(logouturl, headers = headers)  # response contains login token

            if response.status_code == 200:
                
                # Extract the logout msg from the response
                rmsg = response.json().get('message')

                # Clear token & username from SESSION
                try:
                    del request.session['authToken']
                    del request.session['active_uname']
                except KeyError:
                    pass

                #set a msg
                messages.success(request, rmsg)
                # redirect to login page
                # xxxx return render(request, 'auth-signin.html')  xxxx not directly render...form submission for login does not redirecthere
                return redirect('login-user')
                
            else:
                messages.warning(request, "Opration failed.") 
                # redirect to dash
        except Exception as ex:
            print(ex)
            messages.warning(request, "An error occurred during logout.")
    else:
        messages.warning(request, "User not authenticated. Please login")
        return redirect('login-user')
    
    return redirect('get-data')

# =================================================================================
# Simple original approach
# =================================================================================

"""
import json # for storing to file in json format

def login_by_api(request):
    # URL for the login endpoint
    login_url = 'http://localhost:8085/api/auth/login/'

    # Credentials for authentication
    credentials = {
        'username': 'your_username',
        'password': 'your_password'
    }

    # Sending POST request to login endpoint
    response = requests.post(login_url, data=credentials)

    # Extract the token from the response
    token = response.json().get('token')

    # Save token to a file
    with open('token.json', 'w') as file:
        json.dump({'token': token}, file)


    print(f'Token: {token}')


# ++++++++++ get the token from file & call to logout ++++++++++++
def logout_by_json(request):
    # Load token from file
    with open('token.json', 'r') as file:
        data = json.load(file)
        token = data['token']

    # Use the token for subsequent requests
    headers = {
        'Authorization': f'Token {token}'
    }
"""

    # ........... further operations with this token

    # response = requests.get('http://localhost:8000/api/some-protected-endpoint/', headers=headers)
    # print(response.json())

    # Example POST request
    # data = {'key1': 'value1', 'key2': 'value2'}
    # response = requests.post('http://localhost:8000/api/some-protected-endpoint/', headers=headers, json=data)
    # print(response.json())

"""
# ============ USING Environment variables=================
# >>>>>>> Seeting in env variable >>>>>>>>>>>> export API_TOKEN=your_token_here

import os
import requests

# Read token from environment variable
token = os.getenv('API_TOKEN')
"""