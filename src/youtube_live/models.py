from django.db import models


class MonitoredVideo(models.Model):

    # Video metadata to LSM
    video_id = models.CharField(
        help_text="YouTube video id",
        max_length=50,
        primary_key=True,
        unique=True,
    )

    # Video data

    live_status = models.CharField(
        default="",
        help_text="Latest live status of the video.",
        max_length=50,
    )
    video_info = models.JSONField(
        default=dict,
        help_text="Latest video info",
    )

    # Monitor settings
    check_duration = models.IntegerField(
        default=10,
        help_text="The duration for video status checking in seconds.",
    )
    check_timeout = models.IntegerField(
        default=10,
        help_text="Timeout while checking the video in seconds.",
    )

    # Date & Time
    created_time = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_time = models.DateTimeField(
        auto_now=True,
        editable=False,
    )
