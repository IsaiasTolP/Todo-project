from django import forms

from .models import Task


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'complete_before')
        widgets = {
            'complete_before': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'complete_before', 'done')
        widgets = {
            'complete_before': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
