from django.contrib import admin

from youtube_live.models import *


class MonitoredVideoAdmin(admin.ModelAdmin):
    class Meta:
        model = MonitoredVideo


admin.site.register(
    MonitoredVideo,
    MonitoredVideoAdmin,
)
