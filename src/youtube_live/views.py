import copy

from django.shortcuts import (
    redirect,
    render,
)
from django.views.generic.list import ListView

from youtube_live.forms import *
from youtube_live.models import *
from youtube_live.utils import *


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


class MonitoredVideoListView(ListView):
    model = MonitoredVideo
    paginate_by = 9
    template_name = "monitoredvideo_list.html"
    ordering = ['-updated_time']
