from django.shortcuts import render

from youtube_live.forms import *
from youtube_live.models import *


def submit(request):
    if request.method == "GET":
        context = {}
        context['form'] = SubmitMonitoredVideoForm()
        return render(
            request,
            "submit.html",
            context,
        )
