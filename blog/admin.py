from django.contrib import admin
#importar modelo Post
from .models import Post
#con register se hace visible el Post
admin.site.register(Post)
