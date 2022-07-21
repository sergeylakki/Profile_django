from django.views.generic import DetailView

from .models import *
from django.contrib.auth.models import User

class UserDetailView(DetailView):

    model = User
    template_name = 'user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['character'] = DinamicChUser.objects.filter(user_id=1).filter(visible=True)
        return context
