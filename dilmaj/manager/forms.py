from django import forms

class WordCreateForm(forms.Form):
    name = forms.CharField()
    faTranslate = forms.CharField()
    enTranslate = forms.CharField()
    voice = forms.FileField(required=False)
    image = forms.FileField(required=False)