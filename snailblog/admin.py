from django.contrib import admin
from .models import Post, Comment

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)

from embed_video.admin import AdminVideoMixin
from .models import Item

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)