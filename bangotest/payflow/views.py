import pprint

from django.shortcuts import render

import bleach
import commonware
from lxml import etree
import requests


log = commonware.log.getLogger('playdoh')


def home(request):
    return render(request, 'payflow/home.html', {})

# Below are handlers for redirect URLs that are
# assigned to Bango numbers using the Setup and Config
# section of Bango. The Bango numbers that begin the
# requests are in templates/payflow/home.html

def process(request):
    """Process a payment response redirect."""
    log.info(pprint.pformat(dict(request.REQUEST.items())))
    qs = request.META['QUERY_STRING']
    res = requests.get('https://xml.bango.net/tokenCheck.aspx?%s' % qs)
    tr = etree.fromstring(res.content)
    # This verifies that the request actually came from Bango.
    valid = tr.attrib['success'] == 'true'
    log.info('valid? %s' % valid)
    if not valid:
        log.error('response: %s' % res.content)
    return render(request, 'payflow/process.html',
                  {'valid': valid,
                   'request': request.REQUEST})


def identity(request):
    """Process an identity response redirect."""
    log.info(pprint.pformat(dict(request.REQUEST.items())))
    token = request.REQUEST.get('p')
    # This is where we could verify our own signature
    # to make sure the identity request originated from us.
    valid = token == 'ourtoken'
    log.info('valid? %s' % valid)
    return render(request, 'payflow/identity.html',
                  {'valid': valid,
                   'request': request.REQUEST})
