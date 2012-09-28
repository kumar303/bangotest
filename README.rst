A test server to try out some mobile payments with Bango.

Deploy::

    cp bangotest/settings/local.py-dist bangotest/settings/local.py
    mkvirtualenv bangotest
    pip install -r requirements/prod.txt -r requirements/compiled.txt
