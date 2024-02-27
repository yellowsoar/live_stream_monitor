from django.db.models.signals import post_save
from django.dispatch import receiver

from youtube_live.models import *
from youtube_live.tasks import *
from youtube_live.utils import *


@receiver(
    post_save,
    sender=MonitoredVideo,
)
def send_to_task_queue(
    sender,
    instance,
    created,
    **kwargs,
):
    if all(
        [
            not created,
            not instance.live_status
            in [
                'is_live',
            ],
        ],
    ):
        return

    check_video.apply_async(
        (instance.video_id,),
        retry=True,
        max_retries=None,
        countdown=instance.check_duration,
    )
