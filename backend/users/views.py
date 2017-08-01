from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import (
    View,
    TemplateView
)
from django.views.generic.edit import FormView
from django.urls import reverse
from django.core.urlresolvers import reverse_lazy

from allauth.account.views import SignupView

from .forms import (
    FinishProfileForm,
    AgentSignUpForm,
    CandidateSignUpForm
    )
from .mixins import FinishProfileMixin


User = get_user_model()


class Index(FinishProfileMixin, View):
    
    template_name = 'htmls/index.html'
    
    def get(self, request):
        
        return render(request, self.template_name)
        

class ProfileView(FinishProfileMixin, TemplateView):
    
    template_name = []
    
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        if self.request.user.account_type == User.ACCOUNT_CANDIDATE:
            context = {
                'data': 'this is candidate data'
            }
        elif self.request.user.account_type == User.ACCOUNT_AGENT:
            context = {
                'data': 'this is agent data'
            }
        return context
    
    def get_template_names(self):
        temp_name = super(ProfileView, self).get_template_names()
        if self.request.user.account_type == User.ACCOUNT_CANDIDATE:
            temp_name = 'htmls/profile_candidate.html'
        elif self.request.user.account_type == User.ACCOUNT_AGENT:
            temp_name = 'htmls/profile_agent.html'
        return temp_name

class FinishProfile(FormView):
    
    template_name = 'htmls/profile_finish.html'
    form_class = FinishProfileForm
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        user = self.request.user
        User.objects.filter(id=user.id).update(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            account_finished=True
        )
        return super(FinishProfile, self).form_valid(form)       



class CandidateSignUp(SignupView):
    
    template_name = 'account/allauth/sign-up-candidate.html'
    form_class = CandidateSignUpForm
    redirect_field_name = 'next'
    view_name = 'candidate_sign_up'
    
    def get_context_data(self, **kwargs):
        ret = super(CandidateSignUp, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret
        

class AgentSignUp(SignupView):
    
    template_name = 'account/allauth/sign-up-agent.html'
    form_class = AgentSignUpForm
    redirect_field_name = 'next'
    view_name = 'agent_sign_up'
    
    def get_context_data(self, **kwargs):
        ret = super(AgentSignUp, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret

