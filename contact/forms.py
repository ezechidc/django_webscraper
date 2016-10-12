from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=120, required=True)
    contact_email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)