from django.shortcuts import render, redirect
from authomatic.core import Authomatic
from authomatic.adapters import DjangoAdapter
from team.config import CONFIG
from team.models import UserInfo

authomatic = Authomatic(CONFIG, 'teammario')


def home_page(request):
    return render(request, 'home.html')


def login_page(request, provider_name):

    # We we need the response object for the adapter.
    res_redirect = redirect('main')

    # Start the login procedure.
    result = authomatic.login(DjangoAdapter(request, res_redirect), provider_name)

    # If there is no result, the login procedure is still pending.
    # Don't write anything to the response if there is no result!
    if result:
        user_info_model = UserInfo
        if not (result.user.name and result.user.id):
            result.user.update()
        user_id = format(result.user.id)
        user_name = format(result.user.name)

        if user_info_model.objects.filter(user_id=user_id).exists():
            request.session['user_id'] = user_id
            return res_redirect
        else:
            user_info = user_info_model.objects.create(user_id=user_id, user_name=user_name)
            user_info.save()
            request.session['user_id'] = user_id
            return res_redirect

    return res_redirect


def main_page(request):
    user_info_model = UserInfo
    user_id = request.session['user_id']
    if user_info_model.objects.filter(user_id=user_id).exists():
        user_info = user_info_model.objects.get(user_id=user_id)
        return render(request, 'main.html', {'user_info': user_info})

    return render(request, 'main.html')


def log_out(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return render(request, 'home.html')
