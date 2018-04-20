from django.urls import path

from Blog import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blogs/', views.blog_list, name="blog_list"),
    path('blogs/<int:blog_id>', views.blog_detail, name="blog_detail"),
    path('blogs/add', views.blog_add, name="blog_add"),
    path('blogs/delete/<int:blog_id>', views.blog_delete, name="blog_delete"),
    path('blogs/update/<int:blog_id>', views.blog_update, name="blog_update"),

]