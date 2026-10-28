from django import forms

from .models import HelpRequest


class HelpRequestForm(forms.ModelForm):

    class Meta:
        model = HelpRequest
        fields = [
            "title",
            "description",
            "category",
            "address",
        ]

        labels = {
            "title": "Название",
            "description": "Описание",
            "category": "Категория помощи",
            "address": "Адрес",
        }

        widgets = {
            "description": forms.Textarea(attrs={
                "rows": 5,
            }),
        }