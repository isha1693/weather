from django import forms
from .models import Question
from .models import Person
from .models import Address

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            "pub_date": forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control',
            'min': '2023-01-01T00:00', 
            'max': '2024-12-31T23:59',  
        })
    }
class NameForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'email', 'age', 'phone', 'city']

class SearchForm(forms.Form):
    q = forms.CharField(label='Search', max_length=100, required=False)

class PersonFilterForm(forms.Form):
   name = forms.CharField(required=False)
   city = forms.CharField(required=False)

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'state', 'zipcode']