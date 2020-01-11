from django import forms
from django.core.validators import RegexValidator
from .models import Country


class CountryChangeForm(forms.ModelForm):
    name = forms.CharField(widget=forms.PasswordInput, required=False,
                               validators=[
                                   RegexValidator(r'^.{6,}$', 'Name must has at least 6 characters.')])

    def __init__(self, *args, **kwargs):
        super(CountryChangeForm, self).__init__(*args, **kwargs)
        self.fields['country'].required = True
        self.fields['slug'].required = True

    def save(self, commit=True):
        country = super(CountryChangeForm, self).save(commit=False)

        if commit:
            country.save()
        return country

    # def clean_data(self):
    #     return self.cleaned_data.get('data')

    class Meta:
        model = Country
        fields = ('country', 'slug')
