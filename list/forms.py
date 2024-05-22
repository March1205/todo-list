from django import forms
from list.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        input_formats=['%d.%m.%Y %H:%M']
    )

    class Meta:
        model = Task
        fields = ("content", "deadline", "tags", "is_done")


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name",)
