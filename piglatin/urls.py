from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    url(r'^translator/', views.translator, name="translator"),
    url(r'^aboutus/', views.about_us, name="aboutus"),
]
