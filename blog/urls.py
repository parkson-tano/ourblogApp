from django.urls import path
from .views import index, blogpost


urlpatterns = [
    path('', index, name='index'),
    path('blogpost/', blogpost, name='blogpost'),

]