from django.forms import ModelForm, ImageField
from django.core.exceptions import ValidationError

from .models import Product

BAD_WORDS = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]


class ProductForm(ModelForm):
    """
    Форма для создания и редактирования товара интернет-магазина
    """
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """
        Стилизация формы при инициализации
        """
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Название товара"
        })
        self.fields["description"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Описание товара",
            "rows": 4
        })
        self.fields["photo"].widget.attrs.update({
            "class": "form-control"
        })
        self.fields["category"].widget.attrs.update({
            "class": "form-select"
        })
        self.fields["price_per_unit"].widget.attrs.update({
            "class": "form-control"
        })

    def clean_price_per_unit(self):
        """
        Проверка, что цена товара неотрицательна
        """
        price_per_unit = self.cleaned_data["price_per_unit"]
        if price_per_unit < 0:
            raise ValidationError("Цена товара не может быть меньше нуля")
        return price_per_unit

    def clean_name(self):
        """
        Проверка наличия нецензурных слов в полях name и description
        """
        name = self.cleaned_data["name"]
        for word in BAD_WORDS:
            if word in name.lower():
                self.add_error("name", f"В названии товара не может содержаться слово '{word}'")
        return name

    def clean_description(self):
        """
        Проверка наличия нецензурных слов в полях name и description
        """
        description = self.cleaned_data["description"]
        for word in BAD_WORDS:
            if word in description.lower():
                self.add_error("description", f"В описании товара не может содержаться слово '{word}'")
        return description

    def clean_photo(self):
        photo = self.files.get("photo")
        max_size = 5 * 1024 ** 2
        if photo:
            if photo.size > max_size:
                raise ValidationError("Размер изображения не должен превышать 5 Мб")
            elif photo.content_type not in ["image/jpeg", "image/jpg", "image/png"]:
                raise ValidationError("Можно загрузить файлы только форматов JPEG, JPG, PNG")
            return photo
        else:
            return False
