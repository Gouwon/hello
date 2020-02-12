from django import forms


class PostSearchForm(forms.Form):
    search = forms.CharField(label='Search Word')