
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    # path('auth/', include('auth.urls')),
]



#  localhost:8000/auth/login