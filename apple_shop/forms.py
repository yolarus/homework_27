from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(ModelForm):
    """
    Форма для создания и редактирования товара интернет-магазина
    """
    class Meta:
        model = Product
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        bad_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

        for word in bad_words:
            if word in cleaned_data["name"].lower() or word in cleaned_data["description"].lower():
                raise ValidationError(f"В названии или описании товара не может содержаться слово '{word}'")
        return cleaned_data
