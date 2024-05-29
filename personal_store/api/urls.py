from django.urls import path
from . import views
urlpatterns=[
    path("items",views.viewItems.as_view()),
    path("comments",views.Comments.as_view())

]