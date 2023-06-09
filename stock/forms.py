from django import forms
from .models import Transaction, User, Portfolio
from django.contrib.auth.forms import UserCreationForm


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['stock', 'transaction_type', 'quantity', 'price']

class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2']




class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})