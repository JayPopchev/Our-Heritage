from django.urls import path

from preservation.views import preservation_add, preservation_detail, preservation_log_detail, preservation_edit, \
    preservation_delete

app_name = 'preservation'

urlpatterns = [
    # This matches the /dashboard/<slug>/preservation/ pattern
    path('<slug:artifact_slug>/preservation/', preservation_detail, name='detail'),
    path('<slug:artifact_slug>/preservation/add/',preservation_add, name='add'),
# View a single log
    path('<slug:artifact_slug>/preservation/<int:pk>/', preservation_log_detail, name='log_detail'),
    # Edit a log
    path('<slug:artifact_slug>/preservation/<int:pk>/edit/', preservation_edit, name='edit'),
    # Delete a log
    path('<slug:artifact_slug>/preservation/<int:pk>/delete/', preservation_delete, name='delete'),
]