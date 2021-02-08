from django import forms
from main.models import Category


class AddCategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=40,
                            widget=forms.TextInput(attrs={'type': 'text', 'id': 'title', 'class': 'form-control',
                                                          'placeholder': 'Назва категорії', 'required': 'required'}))
    category_order = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'number', 'id': 'catOrder', 'class': 'form-control',
                                      'placeholder': 'Порядковий номер категорії', 'required': 'required'}))

    is_visible = forms.BooleanField(initial=False, required=False)

    is_special = forms.BooleanField(initial=False, required=False)

    class Meta():
        model = Category
        fields = ('title', 'category_order', 'is_visible', 'is_special')
