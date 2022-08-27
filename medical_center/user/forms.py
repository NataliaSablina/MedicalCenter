from django import forms


class HelpUserForm(forms.Form):
    email = forms.EmailField(label="From", required=True)
    message = forms.CharField(label="How can we help?", required=True)
