from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, FormView, CreateView, UpdateView
from .models import *


class UserDetailView(DetailView):

    model = Person
    template_name = 'user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['character'] = CharacteristicsUser.objects.filter(user_id=1).filter(visible=True)
        return context

@method_decorator(csrf_exempt, name='dispatch')
class CharacteristicsUserCreateView(CreateView):
    model = CharacteristicsUser
    fields = ['characteristic_id', 'value']
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user
        self.object.save()
        return super(CharacteristicsUserCreateView, self).form_valid(form)


class CharacteristicsUserUpdateView(UpdateView):
    model = CharacteristicsUser
    template_name = 'profile_main/characteristicsuser_form.html'
    fields = ['characteristic_id', 'value']
    template_name_suffix = reverse_lazy('main')


@method_decorator(csrf_exempt, name='dispatch')
class ActionUserCreateView(CreateView):
    model = ActionUser
    fields = ['action_id', 'value', 'start_datetime', 'end_datetime']
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user
        self.object.save()
        return super(ActionUserCreateView, self).form_valid(form)

def main(request):
    return redirect('user', request.user.id)