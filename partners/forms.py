from django import forms

from .models import PartnerApplication


class PartnerApplicationForm(forms.ModelForm):
    class Meta:
        model = PartnerApplication
        fields = ["email", "message"]

        labels = {
            "email": "Email",
            "message": "Сообщение для администрации",
        }

        widgets = {
            "message": forms.Textarea(
                attrs={
                    "rows": 6,
                    "placeholder": "Напишите, чем занимается ваша организация и какое сотрудничество вы предлагаете.",
                }
            ),
        }