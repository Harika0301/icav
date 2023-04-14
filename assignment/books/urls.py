from django.urls import path, include

from .views import LoginAPIView
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', LoginAPIView.as_view(), name='login_api'),
    path('register/',views.register, name="register"),
    path('books/details/',login_required(views.csv_import),name="csv_import"),
    path('logout/',views.logout,name="logout"),
]

