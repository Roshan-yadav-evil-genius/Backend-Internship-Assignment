from django.urls import path
from .views import V3App,V3AppCrud

urlpatterns = [
    path("events",V3App.as_view()),
    path("events/<int:id>",V3AppCrud.as_view())
]
