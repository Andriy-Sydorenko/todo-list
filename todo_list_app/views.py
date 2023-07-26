from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from todo_list_app.forms import (TaskSearchForm,
                                 TaskForm,

                                 TagForm,
                                 TagSearchForm)
from todo_list_app.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5
    ordering = ["is_done"]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)

        content = self.request.GET.get("content", "")
        context["search_form"] = TaskSearchForm(initial={
            "content": content
        })
        return context

    def get_queryset(self):
        queryset = Task.objects.prefetch_related("tags").order_by(
            "is_done", "-created_at"
        )
        form = TaskSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                content__icontains=form.cleaned_data["content"]
            )
        return queryset


class TaskDetailView(generic.DetailView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list_app:index")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo_list_app/task_form.html"


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = "todo_list_app/task_confirm_delete.html"
    success_url = reverse_lazy("todo_list_app:index")


class TaskCompleteView(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs["pk"])
        task.is_done = True
        task.save()

        query_params = self.request.GET.copy()
        current_page = self.request.GET.get("page", 1)
        query_params["page"] = current_page
        url = f"{reverse('todo_list_app:index')}?{query_params.urlencode()}"
        return url


class TaskUndoView(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs["pk"])
        task.is_done = False
        task.save()

        query_params = self.request.GET.copy()
        current_page = self.request.GET.get("page", 1)
        query_params["page"] = current_page
        url = f"{reverse('todo_list_app:index')}?{query_params.urlencode()}"
        return url


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")
        context["search_form"] = TagSearchForm(initial={
            "name": name
        })
        return context

    def get_queryset(self):
        queryset = Tag.objects.order_by("name")
        form = TagSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo_list_app:tag-list")


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "todo_list_app/tag_form.html"


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    template_name = "todo_list_app/tag_confirm_delete.html"
    success_url = reverse_lazy("todo_list_app:tag-list")
