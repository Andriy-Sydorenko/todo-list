from django.urls import path

from todo_list_app.views import (TaskListView,
                                 TaskCreateView,
                                 TaskDetailView,
                                 TaskUpdateView,
                                 TaskDeleteView,
                                 TaskCompleteView,
                                 TaskUndoView,

                                 TagListView,
                                 TagCreateView,
                                 TagUpdateView,
                                 TagDeleteView)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path(
        "create/",
        TaskCreateView.as_view(),
        name="task-create"),
    path(
        "<int:pk>/",
        TaskDetailView.as_view(),
        name="task-detail"),
    path(
        "<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"),
    path(
        "<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"),
    path(
        "<int:pk>/complete/",
        TaskCompleteView.as_view(),
        name="task-complete"),
    path(
        "<int:pk>/undo/",
        TaskUndoView.as_view(),
        name="task-undo"),

    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list"),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create"),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"),
]

app_name = "todo_list_app"
