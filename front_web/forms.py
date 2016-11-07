__author__ = 'liushuman'

from django import forms


class PaperForm(forms.Form):
    time = forms.CharField(max_length=10)
    title = forms.CharField(max_length=200)
    authors = forms.CharField(label='authors', max_length=200)
    institutions = forms.CharField(label='institutions', max_length=300)
    abstract = forms.CharField(label='abstract')
    notes = forms.CharField(label='notes')
    state = forms.CharField(label='state')
    tags = forms.CharField(label='tags')