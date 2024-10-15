from django import forms

from .models import Task

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'content', 'date_limit')
        widgets = {
            'date_limit': forms.DateTimeInput(attrs={'type':'datetime-local'})
        }