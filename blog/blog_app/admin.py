from django.contrib import admin
from .models import Post

#create structure what displayed the model on the administration site. Create filter etc.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','publish', 'status']
    list_filter = ['status','created','publish','author']
    search_fields = ['title', 'body']
    prepopylated_fields = {'slug':('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS

