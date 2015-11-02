from .form import RegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect


def index(request):
    return HttpResponseRedirect('/accounts/login/')


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@csrf_protect
def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()

    variables = RequestContext(request, {
        'form': form
    })

    return render_to_response(
        'registration/register.html',
        variables,
    )
