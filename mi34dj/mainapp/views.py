#from django.views.decorators.http import require_POST
from django.template.response import HttpResponse, TemplateResponse
from django.shortcuts import redirect
from django.conf import settings

from forms import FormWithCaptcha

from mi34dj.adssh import generate_login, generate_password, ADSsh

# Create your views here.

def index(request):
    data = {}

    if request.method == 'GET':
        form = FormWithCaptcha()
 
    elif request.method == 'POST':
        form = FormWithCaptcha(request.POST)
        if form.is_valid() or settings.DEBUG:
            # create user
            ad = ADSsh(settings.ADSSH_HOST, user=settings.ADSSH_LOGIN,
                       password=settings.ADSSH_PASSWORD, allow_agent=False)
            ad.connect(check=False)
            login = generate_login()
            password = generate_password()
            retcode, stdout, stderr = ad.create_user(login, password)
            if retcode:
                return TemplateResponse(request, 'error.html',
                                        {'error_message': stdout + stderr})
            
            #return TemplateResponse(request, 'success.html', data)
            #http://localhost:8000/media/EricomAccessNowWebComponent/start.html?address=xxx&username=aaa&password=bbb&autostart=true
            """
            url = "%sEricomAccessNowWebComponent/start.html?address=%s&domain=%s&username=%s&password=%s&autostart=true" % (
                    settings.MEDIA_URL, settings.RDP_HOST, settings.RDP_DOMAIN,
                    login, password)
            """
            url = "%sEricomAccessNowWebComponent/start.html" % settings.MEDIA_URL
            response = redirect(url)
            response.set_cookie("EAN_autostart", "true")
            response.set_cookie("EAN_address", settings.RDP_HOST)
            response.set_cookie("EAN_full_address", "")
            response.set_cookie("EAN_username", login)
            response.set_cookie("EAN_password", password)
            response.set_cookie("EAN_domain", settings.RDP_DOMAIN)
            return response

    data['form'] = form
    return TemplateResponse(request, 'index.html', data)
