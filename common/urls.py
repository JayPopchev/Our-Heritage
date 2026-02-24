from django.urls import path

from common.views import about_page

app_name = 'common'
urlpatterns = [
    path('', about_page, name='about'),
]