from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^my-profile/', views.ProfileView.as_view(), name='my-profile'),
    url(r'^finish-profile/', views.FinishProfile.as_view(), name='finish-profile'),
    url(r'^sign-up-candidate/', views.CandidateSignUp.as_view(), name='sign-up-candidate'),
    url(r'^sign-up-agent/', views.AgentSignUp.as_view(), name='sign-up-agent'),
]