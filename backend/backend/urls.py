from django.conf.urls import url, include
from django.contrib import admin

from allauth.account.views import LoginView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^', include('users.urls')),
]
