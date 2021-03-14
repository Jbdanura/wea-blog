from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogListView.as_view(template_name="home.html"), name="home"),
    path("post/<int:pk>/", views.BlogDetailView.as_view(template_name="post_detail.html"),name="post_detail"),
    path("post/new", views.BlogCreateView.as_view(template_name="post_new.html"),name="post_new"),
    path("post/<int:pk>/edit",views.BlogUpdateView.as_view(template_name="post_edit.html"), name="post_edit"),
    path("post/<int:pk>/delete", views.BlogDeleteView.as_view(template_name="post_delete.html"), name="post_delete"),
]
