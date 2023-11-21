from django import forms


class SearchForm(forms.Form):
    search_term = forms.CharField(label='search', max_length=255)
