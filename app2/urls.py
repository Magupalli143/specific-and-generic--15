from django.urls import path
from app2.views import *
app_name='app2'
urlpatterns=[
    path('file2/',file2,name='file2'),
]