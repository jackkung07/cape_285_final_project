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
            aapl_f = 0
            AAPL = Share('AAPL')
            aapl_f = float(str(AAPL.get_percent_change_from_year_low())[0:-1]) + \
                     float(str(AAPL.get_percent_change_from_200_day_moving_average())[0:-1]) + \
                     float(str(AAPL.get_percent_change_from_50_day_moving_average())[0:-1]) - \
                     float(str(AAPL.get_percent_change_from_year_high())[0:-1])

            adbe_f = 0
            ADBE = Share('ADBE')
            adbe_f = float(str(ADBE.get_percent_change_from_year_low())[0:-1]) + \
                     float(str(ADBE.get_percent_change_from_200_day_moving_average())[0:-1]) + \
                     float(str(ADBE.get_percent_change_from_50_day_moving_average())[0:-1]) - \
                     float(str(ADBE.get_percent_change_from_year_high())[0:-1])

            nsrgy_f = 0
            NSRGY = Share('NSRGY')
            nsrgy_f = float(str(NSRGY.get_percent_change_from_year_low())[0:-1]) + \
                      float(str(NSRGY.get_percent_change_from_200_day_moving_average())[0:-1]) + \
                      float(str(NSRGY.get_percent_change_from_50_day_moving_average())[0:-1]) - \
                      float(str(NSRGY.get_percent_change_from_year_high())[0:-1])

            total_f = aapl_f + adbe_f + nsrgy_f
            aapl_pct = aapl_f/float(total_f)
            adbe_pct = adbe_f/float(total_f)
            nsrgy_pct = nsrgy_f/float(total_f)
            aaplD = {"sticker":"AAPL","name":AAPL.get_name(),"aloc_pct":str(aapl_pct),"aloc_amt":str(allotment*aapl_pct)}
            adbeD = {"sticker":"ADBE","name":ADBE.get_name(),"aloc_pct":str(adbe_pct),"aloc_amt":str(allotment*adbe_pct)}
            nsrgyD = {"sticker":"NSRGY","name":NSRGY.get_name(),"aloc_pct":str(nsrgy_pct),"aloc_amt":str(allotment*nsrgy_pct)}
            rstlist.append(aaplD)
            rstlist.append(adbeD)
            rstlist.append(nsrgyD)


            ethical_investment = True

        if 'growth' in request.POST.keys():
            growth_investment = True
        if 'index' in request.POST.keys():
            VTI = Share('VTI')
            IXUS = Share('IXUS')
            ILTB = Share('ILTB')



    #        rstlist.append(vtlD)
    #        rstlist.append(ixusD)
    #        rstlist.append(iltbD)

            index_investment = True
        if 'quality' in request.POST.keys():
            quality_investment = True
        if 'value' in request.POST.keys():
            value_investment = True

        return render(request, 'portfolio/home.html', {'result': json.dumps(rstlist)})
    return render(request, 'portfolio/home.html')