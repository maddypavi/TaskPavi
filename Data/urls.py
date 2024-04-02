from django.urls import path, include
from Data.routes import router


urlpatterns = [
    path("", include(router.urls), name="Data"),
]
