from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class CustomUser(AbstractUser):
    
    ACCOUNT_CANDIDATE = 1
    ACCOUNT_AGENT = 2
    
    
    ACCOUNT_TYPE_CHOICES = (
        (ACCOUNT_CANDIDATE, _('Candidate')),
        (ACCOUNT_AGENT, _('Agnet')),
    )
    
    account_finished = models.BooleanField(
                    _('User finished registration'),
                    default=False
                    )
    account_type = models.IntegerField(
                    _('User account type'), 
                    choices=ACCOUNT_TYPE_CHOICES,
                    default=1
                    )

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        
    @property
    def profile(self):
        if self.account_type == self.ACCOUNT_AGENT:
            return self.agent
        elif self.account_type == self.ACCOUNT_CANDIDATE:
            return self.candidate  


class Agent(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='agent'
        )
    
    
class Candidate(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='candidate'
        )