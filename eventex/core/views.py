# coding: utf-8
from django.shortcuts import render
from eventex.core.models import Speaker


def home(request):
    return render(request, 'index.html')


def speaker_detail(request, slug):
    context = {'speaker': Speaker()}
    return render(request, 'core/speaker_detail.html', context)
