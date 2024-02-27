from celery.exceptions import Ignore

from live_stream_monitor.celery import app
from youtube_live.models import *
from youtube_live.utils import *


@app.task(
    ignore_result=True,
    serializer="pickle",
)
def check_video(
    primary_key,
):
    query_object = MonitoredVideo.objects.get(
        pk=primary_key,
    )
    video_info = get_video_info(
        query_object.video_id,
    )
    query_object.live_status = video_info.get(
        'live_status',
        {},
    )
    query_object.video_info = video_info
    query_object.save()

    if query_object.live_status in [
        'is_live',
    ]:
        raise Ignore()
