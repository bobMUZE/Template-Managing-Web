from django import forms
from .models import Templates

class TemplateCreationForm(forms.ModelForm):
    class Meta:
        model = Templates
        fields = ['customer_id', 'site_id', 'permissions', 'module_id', 'tpl_url', 'tpl_path']

    customer_id = forms.CharField(
        label="customer_id",
        widget=forms.TextInput(attrs={
            "placeholder": "사용자 이름",
        })
    )