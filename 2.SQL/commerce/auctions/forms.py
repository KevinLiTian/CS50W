""" Useful Forms """

from django import forms


class NewListingForm(forms.Form):
    """ Create New Listing """
    title = forms.CharField(max_length=20, label='', required=True,
            widget=forms.TextInput(attrs={'placeholder': "Listing Title"}))
    description = forms.CharField(max_length=128, label='', required=True,
        widget=forms.Textarea(attrs={"placeholder":"Listing Description"}))
    price = forms.CharField(label='', required=True,
        widget=forms.NumberInput(attrs={"placeholder":"Starting Price", "step": 0.01, "min":0}))
    url = forms.CharField(label='',
        widget=forms.URLInput(attrs={"placeholder":"Image URL"}))
