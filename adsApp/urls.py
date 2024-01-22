from django.urls import path
from .views import ad_template, refresh_ad

urlpatterns = [
    path('', ad_template, name='ad_template'),
    path('refresh_ad/', refresh_ad, name='refresh_ad'),
]