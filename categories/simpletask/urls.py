"""RPRT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^categories/', views.CategoryView.as_view(), name='all_categories'),
    url(r'^category-create$', views.CategoryCreateView.as_view(),
        name='create_cat'),
    url(r'^category-update/(?P<pk>[-\w]+)$',
        views.CategoryUpdateView.as_view(), name='CategoryUpdate'),
    url(r'^category-delete/(?P<pk>[-\w]+)$',
        views.CategoryDeleteView.as_view(), name='CategoryDelete'),
    url('subcategories/', views.SubCategoryView.as_view(),
        name='all_sub_categories'),
    url(r'^subcategory-create$', views.SubCategoryCreateView.as_view(),
        name='create_sub_cat'),
    url(r'^sub-category-update/(?P<pk>[-\w]+)$',
        views.SubCategoryUpdateView.as_view(), name='SubCategoryUpdate'),
    url(r'^sub-category-delete/(?P<pk>[-\w]+)$',
        views.SubCategoryDeleteView.as_view(), name='SubCategoryDelete'),
    url('ajax/load_sub_categories/', views.load_sub_categories,
        name='ajax_load_categories'),
    url(r'Home', views.TaskView.as_view(), name='Home'),
url(r'^$', TemplateView.as_view(template_name='base.html'),
        name='index')

]