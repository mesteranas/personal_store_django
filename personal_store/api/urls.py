from django.urls import path
from . import views
urlpatterns=[
    path("/items/view",views.viewItems.as_view()),
    path("/items/get/<int:pk>",views.getItems.as_view())
]