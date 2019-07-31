from django.contrib import admin
from django.urls import path
import blogapp.views

urlpatterns = [
    path('<int:blog_id>',blogapp.views.detail, name="detail"),
    path('write/', blogapp.views.write, name="write"),
    path('create/', blogapp.views.create, name="create"),
    path('newblog/', blogapp.views.blogpost, name="newblog")
]