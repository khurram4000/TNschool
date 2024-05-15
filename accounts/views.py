from django.shortcuts import render, redirect
import requests
from django.urls import reverse
from api import BASE_URL, LOGIN_END_POINT
# Create your views here.

# headers = {'Authorization': 'Token d122dc1c725e46c3445c85e7224d774da5013827'}
def login(request):
    if request.method == "POST":
        # Accessing form data from POST request
        username = request.POST.get('email')  # Assuming 'username' is the name of the input field in your form
        password = request.POST.get('password')  # Assuming 'password' is the name of the input field in your form
        data = {
                "username": username,
                "password": password
            }
        # resp = requests.get(BASE_URL + ENDPOINT, headers=headers)
        resp = requests.post(BASE_URL + LOGIN_END_POINT, json=data)
        # print(resp.status_code)
        # print(resp.json())
        if resp.status_code == 400:
            data = {
                'msg': "Invalid Credentials"
            }
            return render(request, "accounts/login.html", context=data)
        if resp.status_code == 200:
            request.session['api_token'] = resp.json()["key"]
            return redirect(reverse('dashboard'))
    return render(request, "accounts/login.html")


def logout(request):
    # Delete the token from the session
    if 'api_token' in request.session:
        del request.session['api_token']
    return redirect(reverse('login'))
