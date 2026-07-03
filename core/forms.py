import re

from django import forms

from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "phone", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "نام شما",
                    "maxlength": 100,
                    "class": "form-control bg-color-tertiary",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "placeholder": "شماره تلفن",
                    "maxlength": 20,
                    "class": "form-control bg-color-tertiary",
                    "dir": "ltr",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "placeholder": "پیام",
                    "maxlength": 5000,
                    "rows": 5,
                    "class": "form-control bg-color-tertiary",
                }
            ),
        }

    def clean_website(self):
        if self.cleaned_data.get("website"):
            raise forms.ValidationError("اسپم شناسایی شد")
        return ""

    def clean_name(self):
        MIN_NAME_LENGTH = 3

        name = self.cleaned_data["name"].strip()

        if len(name) < MIN_NAME_LENGTH:
            raise forms.ValidationError("نام باید حداقل دارای سه کاراکتر باشد")

        return name

    def clean_phone(self):
        phone = self.cleaned_data["phone"].strip()
        pattern = r"\+?[0-9]{8,20}"

        if not re.fullmatch(pattern, phone):
            raise forms.ValidationError("لطفا شماره تلفن معتبری را وارد کنید")

        return phone
