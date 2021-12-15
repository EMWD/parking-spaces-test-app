from django.http.response import HttpResponseNotAllowed
from django.views import generic
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Task
from .utils import *
from django.shortcuts import redirect
from django.contrib.auth import logout

from .forms import *
from .models import *
from .utils import *


class TaskListView(PostListMixin, generic.ListView):
    queryset = Task.objects.order_by('-created_on')
    template_name = 'index.html'


class TaskDetailView(PostDetailMixin, generic.DetailView):
    model = Task
    template_name = 'task_detail.html'


class AddTaskView(AccessMixin, CreateView):
    form_class = AddTaskForm
    template_name = 'add_task.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if AccessMixin().get_access_by_request(self.request):
            form.save(commit=False)
            return super(AddTaskView, self).form_valid(form)
        else:
            return HttpResponseNotAllowed('Only for admin')


class EditTaskView(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'edit_task.html'
    success_url = reverse_lazy('home')


class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = reverse_lazy('home')


class AboutPageView(TemplateView):

    template_name = 'about.html'


class PolicyPageView(TemplateView):
    template_name = 'policy.html'


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')