import copy

from django.shortcuts import (
    redirect,
    render,
)

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

    if request.method == "POST":
        # Get video info
        request_data = request.POST.dict()
        video_info = get_video_info(request_data['video_id'])

        # Handle video id
        working_data = copy.deepcopy(request_data)
        working_data['video_id'] = ''
        if 'id' in video_info:
            working_data['video_id'] = video_info['id']

        # Handle Form
        form = SubmitMonitoredVideoForm(
            working_data,
        )
        if not form.is_valid():
            return redirect("submit")

        # Handle validated form data
        form.save()
        return redirect("list")
