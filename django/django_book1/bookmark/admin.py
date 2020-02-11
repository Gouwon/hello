from django.contrib import admin

from .models import Bookmark


# Register your models here.
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'url',
    )

## same as above
# class BookmarkAdmin(admin.ModelAdmin):
#     list_display = (
#         'id', 'title', 'url',
#     )

# admin.site.register(Bookmark, BookmarkAdmin)