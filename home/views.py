from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    # Check if the token is present in the session
    context['token_present'] = 'api_token' in request.session
    return render(request, 'home/index.html', context)