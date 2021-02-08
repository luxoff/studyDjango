from django import forms
from .models import UsersMessages, Category


class UserMessageForm(forms.ModelForm):
    user_name = forms.CharField(max_length=50, min_length=3,
                                widget=forms.TextInput(attrs={'type': 'text', 'id': 'name', 'class': 'form-control',
                                                              'placeholder': 'Ім\'я', 'required': 'required'}))

    user_email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email', 'id': 'email',
                                                                'class': 'form-control',
                                                                'placeholder': 'Електронна пошта',
                                                                'required': 'required'}))

    message = forms.CharField(max_length=300, widget=forms.Textarea(
        attrs={'name': 'message', 'id': 'message', 'class': 'form-control',
               'rows': '4', 'placeholder': 'Повідомлення',
               'required': 'required'}))

    class Meta():
        model = UsersMessages
        fields = ('user_name', 'user_email', 'message')

