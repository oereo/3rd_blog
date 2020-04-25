from django.contrib import admin
from django.urls import path
import blogpost.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogpost.views.home, name="home"),# home.html
    path('blog/<int:blog_id>', blogpost.views.detail, name ="detail"), #detail.html
    path('blog/new', blogpost.views.new, name= "new"),
    path('blog/create', blogpost.views.create, name="create"),
    path('blog/edit/<int:blog_id>', blogpost.views.edit, name = "edit"),
    path('blog/update/<int:blog_id>', blogpost.views.update, name = "update"),
    path('blog/delete/<int:blog_id>', blogpost.views.delete, name = "delete"),
]
