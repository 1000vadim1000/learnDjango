from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import CssForm
from .models import Product, Category


def index(request):
    css = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'css': css,
        'title': 'Список продуктов',
        'categories': categories,
    }
    return render(request, template_name='css/index.html', context=context)


def get_category(request, category_id):
    css = Product.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'css/category.html', {'css': css, 'categories': categories,
                                                 'category': category})



def view_css(request, css_id):
    #css_item = Product.objects.get(pk=css_id)
    css_item = get_object_or_404(Product, pk=css_id)
    return render(request, "css/view_css.html", {"css_item": css_item})


def add_css(request):
    if request.method == 'POST':
        pass
    else:
        form = CssForm()
    return render(request, 'css/add_css.html', {'form': form})