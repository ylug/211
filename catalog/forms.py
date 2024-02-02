from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'price_for_one',)

    def clean_name(self):
        cleanned_data = self.cleaned_data['name']

        stop_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for i in stop_list:
            if i in cleanned_data:
                raise forms.ValidationError(f'В названии присутствует недопустимое слово - {i}')

        return cleanned_data

    def clean_description(self):
        cleanned_data = self.cleaned_data['description']

        stop_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for i in stop_list:
            if i in cleanned_data:
                raise forms.ValidationError(f'В описании присутствует недопустимое слово - {i}')

        return cleanned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


class ProductModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'publication',)
