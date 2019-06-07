# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings

# Create your views here.

def index(request):
    FOURSQUARE_AUTH_URL = "https://foursquare.com/oauth2/authenticate?client_id="+settings.FOURSQUARE_CLIENT+"&response_type=code&redirect_uri="+settings.HOSTNAME+"/app/fs_redirect"
    return render(request, 'app/index.html', {
        'name':'unknown',
        'FOURSQUARE_AUTH_URL':FOURSQUARE_AUTH_URL})

def fs_redirect(request):
    code, error = request.GET.get('code'), request.GET.get('error')
    
    return render(request, 'app/fs_redirect.html', {})
