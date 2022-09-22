from django.contrib import admin

# Register your models here.
# streamblocks/admin.py

from django.contrib import admin
from streamfield.admin import StreamBlocksAdmin

from streamblocks.models import RichText, Page, ImageWithText

admin.site.unregister(RichText)
admin.site.register(Page)


@admin.register(RichText)
class RichTextBlockAdmin(StreamBlocksAdmin, admin.ModelAdmin):
    pass
