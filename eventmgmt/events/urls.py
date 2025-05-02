from django.urls import path
from . import views
from .views import MonthListView, EventListView  # ✅ make sure EventListView is included

urlpatterns = [
    path('', views.MonthListView.as_view(), name='month_list'),
    path('<str:month>/', EventListView.as_view(), name='event-list'),

]
