from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name="starting-page"),
    path('posts', views.posts, name="posts"),
    path('posts/<slug:post>', views.specific_post, name="specific-post")
]
