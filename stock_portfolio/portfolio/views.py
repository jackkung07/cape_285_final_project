from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from .models import UserCreationForm
from yahoo_finance import Share
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
    rstlist = list()
    apple = Share('APPL')
    adobe = Share('ABDE')
    nestle = Share('NSRGY')
    vti = Share('VTI')
    ixus = Share('IXUS')
    iltb = Share('ILTB')


    if request.method == 'POST':
        allotment = int(str(request.POST['allotment']))
        ethical_investment = False
        growth_investment = False
        index_investment = False
        quality_investment = False
        value_investment = False
        if 'ethical' in request.POST.keys():
            data = {}
            data['sticker'] = 'ADBE'
            data['name'] = adobe.get_name()
            data['price'] = adobe.get_price()
            rstlist.append(data)
            data['sticker'] = 'APPL'
            data['name'] = apple.get_name()
            data['price'] = apple.get_price()
            rstlist.append(data)
            ethical_investment = True

        if 'growth' in request.POST.keys():
            growth_investment = True
        if 'index' in request.POST.keys():
            rstlist.append(vti.get_name())
            rstlist.append(iltb.get_name())
            rstlist.append(ixus.get_name())
            index_investment = True
        if 'quality' in request.POST.keys():
            quality_investment = True
        if 'value' in request.POST.keys():
            value_investment = True

        return render(request, 'portfolio/home.html', {'result': rstlist})
    return render(request, 'portfolio/home.html')