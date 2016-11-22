# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from django.shortcuts import render


def view_sample(request):
    context = {}
    return render(request, 'template_name.html', context)


class ClassySample(TemplateView):
    template_name = 'template_name.html'
