from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(template_name="signup.html"), name="signup"),
]