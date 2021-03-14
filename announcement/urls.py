from django.contrib import admin
from django.urls import path
import result.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', result.views.home, name="home"),
    path('pass_fail/',result.views.pass_fail, name="pass_fail"),
]