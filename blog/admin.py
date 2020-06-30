from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):

    list_display = ['title','author', 'published_date']
    list_display_links = ['author', 'published_date']
    list_editable = ['title']
    list_filter = ['published_date']
    search_fields = ['title', 'text']

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
