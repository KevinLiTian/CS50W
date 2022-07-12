""" Forms """

from django import forms

class NewPageForm(forms.Form):
    """ Form for New Page """
    title = forms.CharField(max_length=10, label='', required=True,
        widget=forms.TextInput(attrs={'placeholder': "Title",
                                'class':'col-sm-11',
                                'style':'top:0.5rem'}))

    content = forms.CharField(label='',
        widget=forms.Textarea(attrs={'placeholder': "Content",
                                'class':'col-sm-11',
                                'style':'top:1rem'}))
