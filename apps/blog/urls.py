from django.urls import path

from apps.blog.views import bloglist

urlpatterns = [
    path('', bloglist, name='bloglist'),
]