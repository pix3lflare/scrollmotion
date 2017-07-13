from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from scrollmotion import views, api_views


router = routers.SimpleRouter()
router.register(r'image', api_views.ImageViewSet)


urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url('^register/$', views.Register.as_view(), name='register'),
    url('^login/$', auth_views.LoginView.as_view(), name='login'),
    url('^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
