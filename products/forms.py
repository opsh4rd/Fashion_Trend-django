from django import forms


class SearchForm(forms.Form):
    search_term = forms.CharField(label='search', max_length=255)


class SendMessage(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'stext-111 cl2 plh3 size-116 p-l-62 p-r-30',
                                                            'placeholder': 'Your Email Address'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'stext-111 cl2 plh3 size-120 p-lr-28 p-tb-25',
                                                        'placeholder': 'How Can We Help?'}))
