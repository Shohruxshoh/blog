from django.urls import path
from .views import BlogListView, BlogAppDetailView, BlogAppCreateVeiw, BlogAppUpdateView, BlogAppDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogAppDetailView.as_view(), name="post_detail"),
    path('post/new/', BlogAppCreateVeiw.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', BlogAppUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogAppDeleteView.as_view(), name='post_delete'),
]