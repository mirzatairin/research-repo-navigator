from django import forms
from .models import ScientificTool

class ToolSubmissionForm(forms.ModelForm):
    class Meta:
        model = ScientificTool
        fields = ['name', 'developer', 'description', 'repository_url', 'category']