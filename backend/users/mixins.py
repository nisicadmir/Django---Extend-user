from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import (
    HttpResponseRedirect,
    JsonResponse,
)


User = get_user_model()


class FinishProfileMixin(LoginRequiredMixin):
    """
    Only allow candidates to access this page. Otherwise, redirect them back to their dashboard page.
    """
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.account_finished == False:
            if request.is_ajax():
                return JsonResponse({
                    'success': False,
                    'message': 'Not Authorized',
                })
            return HttpResponseRedirect(reverse_lazy('finish-profile'))
        return super(FinishProfileMixin, self).dispatch(request, *args, **kwargs)