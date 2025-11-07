import json
import random
from copy import deepcopy
from datetime import datetime, timedelta


from django.http import HttpResponseForbidden
from django.shortcuts import render, HttpResponse

from django.utils.translation import gettext_lazy as _

# from django_ratelimit.exceptions import Ratelimited

# from inquiry.models import Inquiry

# def rate_limiter_view(request, *args, **kwargs):
#     return render(request, 'ratelimit.html', status=429)


def view_404(request, *args, **kwargs):
    return render(request, '404.html', status=404)


# def handler_403(request, exception=None):
#     if isinstance(exception, Ratelimited):
#         return HttpResponse('Sorry too many requests, please wait', status=429)
#     return HttpResponseForbidden('Forbidden')


def home_view(request):
    return render(request, 'home.html', status=200)


def home_test(request):
    return render(request, 'home_test.html', status=200)