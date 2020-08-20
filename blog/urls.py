from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:pk>', views.EntryDetail.as_view(), name='entry_detail'),
]
