from django.urls import path

from list.views import TagListView, index, TagCreateView, TagUpdateView, TagDeleteView, TaskCreateView, TaskUpdateView, \
    TaskDeleteView, TaskToggleStatusView

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tags/create/", TagCreateView.as_view(), name="tag_create"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag_update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag_delete"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task_update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task_delete"),
    path("toggle_status/<int:pk>/", TaskToggleStatusView.as_view(), name="toggle_status"),
]

app_name = "todo_list"
