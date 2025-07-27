from django.contrib import admin
from django.urls import path, include

from apps.users.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('user/', include('apps.users.urls')),
    path('todo/', include('apps.todo.urls')),
    path('blog/', include('apps.blog.urls')),
]
