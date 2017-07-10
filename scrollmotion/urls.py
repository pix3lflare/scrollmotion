from django.conf.urls import url
from django.contrib import admin
from scrollmotion import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
]
