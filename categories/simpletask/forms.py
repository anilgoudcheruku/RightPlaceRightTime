from django.forms import ModelForm

from .models import Category, SubCategory


class CategoryForm(ModelForm):
    """
    Single Text Field Form
    """
    class Meta:
        model = Category
        fields = ['category']


class SubCategoryForm(ModelForm):
    """
        Single Text Field Form Dependent on Category Table
    """
    class Meta:
        model = SubCategory
        fields = ['category_name', 'subcategory']



