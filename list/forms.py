from django import forms
from list.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(widget=forms.DateInput(
        attrs={"type": "date"}
    ))

    class Meta:
        model = Task
        fields = ("content", "deadline", "tags", "is_done")


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name",)
