from django.views.generic import (CreateView, ListView,
                                  UpdateView, DeleteView)

from .forms import CategoryForm, SubCategoryForm
from .models import Category, SubCategory
from django.shortcuts import render


class CategoryCreateView(CreateView):
    """
        Inherit Class Based Create View and assign necessary template
        and models
    """
    model = Category
    template_name = 'category-creation.html'
    form_class = CategoryForm
    success_url = '/categories'


class CategoryView(ListView):
    """
        Inherit Class Based List View and assign necessary template and models
    """
    model = Category
    context_object_name = 'cats'
    template_name = 'my-categories.html'


class CategoryUpdateView(UpdateView):
    """
        Inherit Class Based Update View and assign necessary template and
        models
    """
    model = Category
    template_name = 'category-edit.html'
    form_class = CategoryForm
    success_url = '/categories'


class CategoryDeleteView(DeleteView):
    """
        Inherit Class Based Delete View and assign necessary template and
        models
    """
    model = Category
    template_name = 'category-delete.html'
    form_class = CategoryForm
    success_url = '/categories'


class SubCategoryCreateView(CreateView):
    """
        Inherit Class Based Create View and assign necessary template
        and models
    """
    model = SubCategory
    template_name = 'sub-category-creation.html'
    form_class = SubCategoryForm
    success_url = '/subcategories'


class SubCategoryView(ListView):
    """
        Inherit Class Based List View and assign necessary template and models
    """
    model = SubCategory
    template_name = 'my-sub-categories.html'


class SubCategoryUpdateView(UpdateView):
    """
        Inherit Class Based Update View and assign necessary template and
        models
    """
    model = SubCategory
    template_name = 'sub-category-edit.html'
    form_class = SubCategoryForm
    success_url = '/subcategories'


class SubCategoryDeleteView(DeleteView):
    """
        Inherit Class Based Delete View and assign necessary template and
        models
    """
    model = SubCategory
    template_name = 'sub-category-delete.html'
    form_class = SubCategoryForm
    success_url = '/categories'


class TaskView(ListView):
    """
        Inherit Class Based List View and assign necessary template and models
    """
    model = Category
    form_class = CategoryForm
    template_name = 'TaskView.html'


def load_sub_categories(request):
    """
    Ajax call for dynamic filtering on selection of Category value
    :param request:
    :return: json to dropdown.html template
    """
    category = request.GET.get('category')
    sub_categories = SubCategory.objects.filter(id=category)
    return render(request, 'dropdown.html',
                  {'sub_cats': sub_categories})

