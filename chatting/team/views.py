from django.shortcuts import render, redirect

from django.http import HttpResponse
from authomatic.core import Authomatic
from authomatic.adapters import DjangoAdapter

from team.config import CONFIG
from team.models import UserInfo

authomatic = Authomatic(CONFIG, 'teammario')


def home_page(request):
    return render(request, 'home.html')


def login_page(request, provider_name):
    # We we need the response object for the adapter.
    res_redirect = redirect('/team/main')
    # Start the login procedure.
    result = authomatic.login(DjangoAdapter(request, res_redirect), provider_name)

    # If there is no result, the login procedure is still pending.
    # Don't write anything to the response if there is no result!
    if result:
        '''
        # If there is result, the login procedure is over and we can write to response.
        response.write('<a href="/">Home</a>')
        response.write(dir(result))

        if result.error:
            # Login procedure finished with an error.
            response.write('<h2>Damn that error: {0}</h2>'.format(result.error.message))

        elif result.user:
            # OAuth 2.0 and OAuth 1.0a provide only limited user data on login,
            # We need to update the user to get more info.
            if not (result.user.name and result.user.id):
                result.user.update()
            # Check if user's id is already exists
            response.write(u'<h1>Hi {0}</h1>'.format(result.user.name))
            response.write(u'<h2>Your id is: {0}</h2>'.format(result.user.id))
        '''

    # return response
    return res_redirect


def main_page(request):
    return render(request, 'main.html')