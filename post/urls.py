from django.urls import path
from . import views
app_name = 'post'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/update/<int:pk>/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
]
