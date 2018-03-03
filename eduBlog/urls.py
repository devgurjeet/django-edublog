from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'admin/', admin.site.urls),

    # Blog app urls
    path(r'', include('posts.urls')),
    path(r'posts/', include('posts.urls')),
]
