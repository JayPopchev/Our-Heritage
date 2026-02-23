from django.urls import path

from artifacts.views import dashboard, artifact_detail, home_page

app_name = 'artifacts'
urlpatterns = [
    path('', home_page, name='home'),
    path('dashboard/', dashboard, name='list'),
    #path('dashboard/add/',
    path('dashboard/<slug:slug>/', artifact_detail, name='detail'),
    #path('dashboard/<slug:slug>/edit/),
    #path('dashboard/<slug:slug>/delete/),
]