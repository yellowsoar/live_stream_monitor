from django import forms
from django.utils.translation import gettext_lazy as _

from youtube_live.models import MonitoredVideo


class SubmitMonitoredVideoForm(forms.ModelForm):

    class Meta:
        model = MonitoredVideo
        fields = [
            "video_id",
            "check_duration",
            "check_timeout",
        ]
        labels = {
            "video_id": _("Monitor Target"),
        }
        help_texts = {
            "video_id": _("Video Id or an URL"),
        }
