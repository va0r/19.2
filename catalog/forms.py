from django import forms

from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        """
        Стилизация формы
        """

        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ('created_at', 'modified_at',)

    def __check(self, field):
        PROHIBITED_WORDS = ('бесплатно', 'биржа', 'дешево', 'казино', 'крипта',
                            'криптовалюта', 'обман', 'полиция', 'радар')
        cleaned_data = self.cleaned_data[field]
        for word in PROHIBITED_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'ОШИБКА: запрещенное слово <<{word}>>.'
                                            f' Нельзя добавлять продукты с подобным названием или описанием.')
        return cleaned_data

    def clean_title(self):
        self.__check('title')

    def clean_description(self):
        self.__check('description')
