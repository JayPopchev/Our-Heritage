from django.urls import path, include

import preservation
from artifacts.views import dashboard, artifact_detail, home_page, artifact_edit, artifact_delete, artifact_create, \
    exhibition_list, exhibition_detail

app_name = 'artifacts'
urlpatterns = [
    path('', home_page, name='home'),
    path('dashboard/', dashboard, name='list'),
    path('dashboard/add/', artifact_create, name='create'),
    path('dashboard/<slug:slug>/', artifact_detail, name='detail'),
    path('dashboard/<slug:slug>/edit/', artifact_edit, name='edit'),
    path('dashboard/<slug:slug>/delete/', artifact_delete, name='delete'),
    path('dashboard/', include('preservation.urls')),
    path('exhibitions/', exhibition_list, name='exhibition_list'),
    path('exhibitions/<int:pk>/', exhibition_detail, name='exhibition_detail'),
]