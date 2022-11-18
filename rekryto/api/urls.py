from django.urls import path
from .views import Get
urlpatterns = [
    path('url_name/', Get.as_view(), name='get_url'),
]
