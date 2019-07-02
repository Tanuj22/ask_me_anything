from django.urls import path
from users.api.views import CurrentUserAPI

urlpatterns = [
    path("user/", CurrentUserAPI.as_view(), name="current-user")
]
