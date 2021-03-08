from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogListView.as_view(template_name="home.html"), name="home"),
    path("post/<int:pk>/", views.BlogDetailView.as_view(template_name="post_detail.html"),name="post_detail"),
]
