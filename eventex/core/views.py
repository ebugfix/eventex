# coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from eventex.core.models import Speaker, Talk
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    context = {'speaker': speaker}
    return render(request, 'core/speaker_detail.html', context)


class TalkList(TemplateView):
    template_name = 'core/talk_list.html'

    def get_context_data(self, **kwargs):
        ctx = super(TalkList, self).get_context_data(**kwargs)
        ctx.update({
            'morning_talks': Talk.objects.at_morning(),
            'afternoon_talks': Talk.objects.at_afternoon(),
        })
        return ctx


def talk_detail(request, pk):
    talk = get_object_or_404(Talk, pk=pk)
    context = {
        'talk': talk,
    }
    return render(request, 'core/talk_detail.html', context)
