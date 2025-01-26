from django.urls import path
from . views import (
    UserLoginView,
    LogoutView,
)

urlpatterns = [
    path('api/login/', UserLoginView.as_view(), name="login"),
    path('api/logout/', LogoutView.as_view(), name="logout"),

]
