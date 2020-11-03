from django.db import models


class Category(models.Model):
    """
    Single field class for Category Table
    By default Category was set to PK
    """
    category = models.CharField(max_length=250)

    def __str__(self):
        return self.category


class SubCategory(models.Model):
    """
    Single field class for Sub Category Table
    Category_name  was set to FK from Category Table
    """
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.category_name} - {self.subcategory}"
