from django.urls import path
from core.views import (
    HomeView,
)
from django.contrib.auth.decorators import login_required
urlpatterns  = [
    path('feed/', (HomeView.as_view()), name='home_feed'),
]