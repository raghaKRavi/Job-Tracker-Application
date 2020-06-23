from django.urls import path
from .views import (
                # PostListView,
                PostDetailView,
                PostCreateView,
                PostUpdateView,
                PostDeleteView
                )
from . import views

urlpatterns = [
    path('', views.home, name='jobTrack-home'),
    path('job/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('job/new/', PostCreateView.as_view(), name='post-create'),
    path('job/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('job/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='jobTrack-about'),

]
