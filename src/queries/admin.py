from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Dataset)
admin.site.register(Video)
admin.site.register(Query)
admin.site.register(QueryResult)
admin.site.register(Match)
admin.site.register(Signature)
admin.site.register(ProcessState)
