import requests
from django.shortcuts import render
from api import BASE_URL, GET_ALL_ASSIGNED_COURSES_END_POINT, GET_COURSE_LECTURES_END_POINT
from decorators import token_required
# Create your views here.

@token_required
def dashboard(request):
    context = {}
    # Check if the token is present in the session
    context['token_present'] = 'api_token' in request.session
    api_token = request.session.get('api_token')
    # get assigned courses
    headers = {'Authorization': f'Token {api_token}'}
    resp = requests.get(BASE_URL + GET_ALL_ASSIGNED_COURSES_END_POINT, headers=headers)
    # print(resp.status_code)
    # print(resp.json())
    assigned_courses = resp.json()["data"]
    context['assigned_courses'] = assigned_courses
    return render(request, "dashboard/dashboard.html", context)

@token_required
def course_lectures(request, id):
    context = {}
    # Check if the token is present in the session
    context['token_present'] = 'api_token' in request.session
    api_token = request.session.get('api_token')
    # get assigned courses
    headers = {'Authorization': f'Token {api_token}'}
    # print(GET_COURSE_LECTURES_END_POINT + f"{id}/")
    resp = requests.post(BASE_URL + GET_COURSE_LECTURES_END_POINT + f"{id}/", headers=headers)
    print(resp.status_code)
    print(resp.json())
    assigned_courses = resp.json()["data"]
    context['lectures'] = assigned_courses

    return render(request, "dashboard/lectures.html", context)
