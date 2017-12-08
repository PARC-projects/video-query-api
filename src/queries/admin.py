from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Dataset)
admin.site.register(Video)
admin.site.register(Query)
admin.site.register(MatchArray)
admin.site.register(Signature)
