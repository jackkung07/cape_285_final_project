from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from .models import UserCreationForm
from django.http import JsonResponse
from django.http.response import HttpResponse

# Create your views here.
@csrf_exempt
def user_registration_web(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            login(request, user)
            return redirect('/portfolio')
    else:
        form = UserCreationForm()
    return render_to_response('portfolio/register.html', {
        'form': form,
    })


@login_required()
def home_page(request):
    return render(request, 'portfolio/home.html', {'backend_data': None})