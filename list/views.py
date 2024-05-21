from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from list.forms import TagForm, TaskForm
from list.models import Task, Tag


def index(request):
    tasks = Task.objects.all().order_by("is_done", "-created_at")
    return render(request, "list/index.html", {"tasks": tasks})


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("list:tag_list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("list:tag_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("list:tag_list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("list:index")


class TaskToggleStatusView(generic.RedirectView):
    pattern_name = "list:index"

    def get_redirect_url(self, *args, **kwargs):
        task = Task.objects.get(pk=self.kwargs["pk"])
        task.is_done = not task.is_done
        task.save()
        return reverse_lazy("list:index")
