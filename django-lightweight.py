import os
import sys


#Boilerplate MAGIC PART
from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.shortcuts import render

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from django.conf import settings
DEBUG = True
SECRET_KEY = 'this_is_secret'
ALLOWED_HOSTS = ['*']
settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [ os.path.join(BASE_DIR, "templates"),],
            'APP_DIRS': True,
        },
    ]

)
# end boilerplate magic part


# DO THE REAL JOB AND CHANGES

#
def index(request):
    return HttpResponse('Hello World')

# Function for /template path
def template_func(request):
    return render(request, 'hello_template.html')

# URL MAPPING
urlpatterns = (
    url(r'^$', index),
    url(r'^template$', template_func),
)

# END DO THE REAL JOB



# Some system magic ... irrelevant for the lesson
application = get_wsgi_application()
if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
# end of system magic
