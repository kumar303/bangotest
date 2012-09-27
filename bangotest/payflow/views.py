import logging
import pprint

from django import http
from django.shortcuts import render

import bleach
import commonware
from funfactory.log import log_cef
from mobility.decorators import mobile_template
from session_csrf import anonymous_csrf


log = commonware.log.getLogger('playdoh')


def home(request):
    return render(request, 'payflow/home.html', {})


def process(request):
    log.info(pprint.pformat(dict(request.REQUEST.items())))
    return http.HttpResponse('logged request')
