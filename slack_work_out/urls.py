from django.urls import path

from .views import CreateLogView, DoneLogView


app_name = 'slack_work_out'

urlpatterns = [
    path('', CreateLogView.as_view(), name='create_log'),
    path('done_log', DoneLogView.as_view(), name='done_log'),
]