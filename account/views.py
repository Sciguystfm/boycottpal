import string
import random

from account.disqus import get_disqus_sso
from account.forms import UserForm, PasswordForm, TokenForm
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
import json
from uszipcode import ZipcodeSearchEngine
import operator
from boycotted.models import *
import datetime
import feedparser
from account.models import Token, BoycottUser
from django.core.mail import send_mail

TOKEN_EXPIRE= datetime.timedelta(1)

def token_generator(size=20, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Create your views here.
def home(request):
    import feedparser
    cnn = feedparser.parse('http://rss.cnn.com/rss/cnn_topstories.rss')
    fox = feedparser.parse('http://feeds.foxnews.com/foxnews/latest')
    news = json.loads(json.dumps(list(zip(cnn.entries[:25],fox.entries[:25]))))

    my_boycotts_json=[]
    top_boycotts_json=[]
    trending_boycotts_json=[]
    raw_alert = request.GET.get('alert')
    if raw_alert == None:
        alert=""
    else:
        alert=raw_alert
    if request.user.is_authenticated():
        my_boycotts=[]
        for my_boycott in request.user.boycotts.all():
            zipcode=my_boycott.target.zip
            if zipcode == "":
                location = " "
            else:
                search = ZipcodeSearchEngine()
                location = search.by_zipcode(zipcode)

                location = "("+ str(location.City) + ", " + str(location.State)+") "

            my_bct = {
                'name':my_boycott.target.name,
                'location':location,
                'reason':my_boycott.reason,
                'id': my_boycott.id,
                'target_id':my_boycott.target.id
            }
            my_boycotts.append(my_bct)

        my_boycotts_json = json.loads(json.dumps(my_boycotts))
    trending_boycotts=[]
    top_boycotts=[]
    for top_boycott in Boycotted.objects.all():
        zipcode = top_boycott.zip
        if zipcode == "":
            location = " "
        else:
            search = ZipcodeSearchEngine()
            location = search.by_zipcode(zipcode)

            location = "(" + str(location.City) + ", " + str(location.State) + ") "



        top_bct={
            'name':top_boycott.name,
            'id':top_boycott.id,
            'num':top_boycott.boycotts.count(),
            'location':location
        }
        top_boycotts.append(top_bct)

    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(7)

    for trending_boycott in Boycotted.objects.filter(date__range=[start_week,end_week]):
        zipcode = trending_boycott.zip
        if zipcode == "":
            location = " "
        else:
            search = ZipcodeSearchEngine()
            location = search.by_zipcode(zipcode)

            location = "(" + str(location.City) + ", " + str(location.State) + ") "

        trend_bct={
            'name':trending_boycott.name,
            'id':trending_boycott.id,
            'num':trending_boycott.boycotts.count(),
            'location':location
        }
        trending_boycotts.append(trend_bct)

    def getKey(boycott):
        return int(boycott['num'])

    top_boycotts_json = json.loads(json.dumps(sorted(top_boycotts, key=getKey, reverse=True)[:25]))
    trending_boycotts_json = json.loads(json.dumps(sorted(trending_boycotts, key=getKey, reverse=True)[:10]))







    return render(request, 'home.html',{
        'alert':alert,
        'my_boycotts': my_boycotts_json,
        'top_boycotts':top_boycotts_json,
        'trending_boycotts':trending_boycotts_json,
        'news':news
    })



def Signup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            # process data in form
            user = form.save()


            user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'],
                                    )


            if user is not None:
                login(request, user)
            return HttpResponseRedirect('/?alert=signup')


    else:
        form = UserForm()


    return render(request, 'signup.html', {'form': form})

def _get_disqus_sso(user):
    if user.is_authenticated():
        disqus_sso = get_disqus_sso(
            user.id,
            user.username,
            user.email, )
    else:
        disqus_sso = get_disqus_sso()
    return disqus_sso


def reset_password(request, token):
    token_obj=Token.objects.filter(token=token)
    if token_obj.count() == 0:
        token_obj=None
    else:
        token_obj=token_obj[0]
    if (token_obj is None ) or (token_obj.date - datetime.datetime.now(datetime.timezone.utc) > TOKEN_EXPIRE):
        return HttpResponseRedirect('/?alert=expired')
    else:
        if request.method == 'POST':
            password_form = PasswordForm(data=request.POST)
            if password_form.is_valid():
                # Save boycotted values to access
                user=token_obj.user
                user.password = password_form.save(commit=False).password
                user.save()
                token_obj.delete()
                login(request, user)

                return HttpResponseRedirect('/?alert=password')

        else:
            password_form = PasswordForm()


        return render(request, 'reset_password.html', {
            'password_form': password_form,
            'username': token_obj.user.username,
            'token': token
        })

def get_reset(request):
    if request.method == 'POST':
        token_form = TokenForm(data=request.POST)
        if token_form.is_valid():
            # process data in form
            cleanEmail=token_form.cleaned_data
            email=cleanEmail.get('email')
            user = BoycottUser.objects.get(email=email)
            token=token_generator()
            Token.objects.create(
                user=user,
                token=token
            )
            send_mail('Boycott Pal Password Recovery', 'Here is your password reset link: ' +token, 'app62196690@heroku.com', [email],
                      fail_silently=False)

            return HttpResponseRedirect('/?alert=reset')


    else:
        token_form = TokenForm()


    return render(request, 'get_reset.html', {'token_form':token_form})

