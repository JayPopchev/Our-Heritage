from django.urls import path

from categories.views import category_list, category_detail, category_create, category_edit, category_delete

app_name = 'categories'

urlpatterns = [
    path('', category_list, name='list'),
    path('<int:pk>/', category_detail, name='detail'),
    path('add/', category_create, name='create'),
    path('<int:pk>/edit/', category_edit, name='edit'),
    path('<int:pk>/delete/', category_delete, name='delete'),
]