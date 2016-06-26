import os, sys
virtual_env = os.path.expanduser('~/virtualenv/lik')
activate_this = os.path.join(virtual_env, 'bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.insert(0, os.path.expanduser('~/django'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "likreklama.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()