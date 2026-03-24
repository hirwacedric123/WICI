from django import forms

from .models import ContactInquiry


class ContactInquiryForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = ["full_name", "email", "organization", "inquiry_type", "message"]
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "name@example.com"}),
            "organization": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Organization (optional)"}
            ),
            "inquiry_type": forms.Select(attrs={"class": "form-select"}),
            "message": forms.Textarea(
                attrs={"class": "form-control", "rows": 5, "placeholder": "How can we help?"}
            ),
        }
