from django.urls import path

from Api import views

urlpatterns = [
    path('blogs/', views.blog_list, name="blog_list"),
    path('blogs/<int:blog_id>', views.blog_detail, name="blog_detail"),
]