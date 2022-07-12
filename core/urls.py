from django.urls import path
from .views import double


urlpatterns = [
    path('', double, name='double_number'),
]
