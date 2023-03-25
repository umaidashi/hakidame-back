from django.contrib import admin

from .models import Hakidame, Tag, HakidameTag

admin.site.register(Hakidame)
admin.site.register(Tag)
admin.site.register(HakidameTag)
