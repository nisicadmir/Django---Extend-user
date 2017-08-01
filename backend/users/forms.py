from django import forms
from django.contrib.auth import get_user_model

from allauth.account.forms import SignupForm

from .models import Agent, Candidate


User = get_user_model()


class FinishProfileForm(forms.Form):
    
    first_name = forms.CharField(label='First name', min_length=5, max_length=160)
    last_name = forms.CharField(label='Last name',  min_length=5, max_length=160)


class CandidateSignUpForm(SignupForm):

    def save(self, request):
        user = super(CandidateSignUpForm, self).save(request)
        user.account_type = 1
        Candidate.objects.create(
            user_id=user.id
        )
        user.save()
        return user
        
        
class AgentSignUpForm(SignupForm):
    
    def save(self, request):
        user = super(AgentSignUpForm, self).save(request)
        user.account_type = 2
        Agent.objects.create(
            user_id=user.id
        )
        user.save()
        return user
