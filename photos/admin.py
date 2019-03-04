
from django.contrib import admin
from .models import Photo, Topic, Location


# class PhotoInline(admin.TabularInline):
#     fieldsets = [
#         ('Basic Info', {'fields': ['description']}),
#         ('Upload Image', {'fields': ['image']})
#     ]
#     model = Photo
#     extra = 3
#
#
# class TopicAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['name']}),
#     ]
#     inlines = [PhotoInline]


admin.site.register(Topic)
admin.site.register(Photo)
admin.site.register(Location)
