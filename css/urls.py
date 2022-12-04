from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('css/<int:css_id>/', view_css, name='view_css'),
    path('css/add-css/', add_css, name="add_css")
]
