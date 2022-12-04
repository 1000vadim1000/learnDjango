from django.db import models
from django.urls import reverse
from db import get_cvs_data

class Product(models.Model):
    cost = models.IntegerField(
        verbose_name='Цена'
    )
    title = models.CharField(
        verbose_name='Название',
        max_length=255,
    )
    tilda_id = models.CharField(
        verbose_name='ID тильды',
        max_length=255
    )
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, default=1)

    def get_absolute_url(self):
        return reverse('view_css', kwargs={'css_id': self.pk})

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(
        max_length=500,
        db_index=True,
        verbose_name="Наименование категории"
    )

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title


#for i in get_cvs_data():
#    Product.objects.create(
#    cost=i['Price'],
#    title=i['Title'],
#    tilda_id=i['Tilda UID'],
#    )