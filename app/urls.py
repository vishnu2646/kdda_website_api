from django.urls import path
from . import views

urlpatterns = [
    path('events', views.event_list, name='events'),
    path('events/<int:pk>', views.event_detail, name='event_detail'),
    path('events/create', views.event_create, name='event_create'),
    path('events/<int:pk>/delete', views.event_delete, name='event_delete'),
]