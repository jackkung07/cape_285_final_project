from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from .models import UserCreationForm
from yahoo_finance import Share
from django.http import JsonResponse
from django.http.response import HttpResponse
import json

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
    ethlst = list()
    idxlst = list()
    pdlist = list()
    APPL = Share('APPL')
    ADBE = Share('ADBE')
    NSRGY = Share('NSRGY')
    VTI = Share('VTI')
    IXUS = Share('IXUS')
    ILTB = Share('ILTB')

#random list
    MMM = Share('MMM')
    pdlist.append({"sticker": "MMM", "detail": MMM})
    ABT = Share('ABT')
    pdlist.append({"sticker": "ABT", "detail": ABT})
    ABBV = Share('ABBV')
    pdlist.append({"sticker": "ABBV", "detail": ABBV})
    ACN = Share('ACN')
    pdlist.append({"sticker": "ACN", "detail": ACN})
    ATVI = Share('ATVI')
    pdlist.append({"sticker": "ATVI", "detail": ATVI})
    AYI = Share('AYI')
    pdlist.append({"sticker": "AYI", "detail": AYI})
    AMD = Share('AMD')
    pdlist.append({"sticker": "AMD", "detail": AMD})
    AAP = Share('AAP')
    pdlist.append({"sticker": "AAP", "detail": AAP})
    AES = Share('AES')
    pdlist.append({"sticker": "AES", "detail": AES})
    AET = Share('AET')
    pdlist.append({"sticker": "AET", "detail": AET})
    AMG = Share('AMG')
    pdlist.append({"sticker": "AMG", "detail": AMG})
    AFL = Share('AFL')
    pdlist.append({"sticker": "AFL", "detail": AFL})
    APD = Share('APD')
    pdlist.append({"sticker": "APD", "detail": APD})
    AKAM = Share('AKAM')
    pdlist.append({"sticker": "AKAM", "detail": AKAM})
    ALB = Share('ALB')
    pdlist.append({"sticker": "ALB", "detail": ALB})
    ARE = Share('ARE')
    pdlist.append({"sticker": "ARE", "detail": ARE})
    AGN = Share('AGN')
    pdlist.append({"sticker": "AGN", "detail": AGN})
    LNT = Share('LNT')
    pdlist.append({"sticker": "LNT", "detail": LNT})
    ALXN = Share('ALXN')
    pdlist.append({"sticker": "ALXN", "detail": ALXN})
    GOOGL = Share('GOOGL')
    pdlist.append({"sticker": "GOOGL", "detail": GOOGL})


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

        return render(request, 'portfolio/test_ivan.html', {'result': json.dumps(rstlist)})
    return render(request, 'portfolio/home.html')