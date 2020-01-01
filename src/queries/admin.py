from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(SearchSet)
admin.site.register(Video)
admin.site.register(VideoClip)
admin.site.register(Query)
admin.site.register(QueryResult)
admin.site.register(Match)
admin.site.register(Feature)
admin.site.register(ProcessState)
admin.site.register(DnnStream)
admin.site.register(Profile)
