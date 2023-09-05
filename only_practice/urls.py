from django.contrib import admin
from django.urls import path
from practice.views import run
urlpatterns = [
    path('admin/', admin.site.urls),
    path('<slug:groupname>/',run)
]
