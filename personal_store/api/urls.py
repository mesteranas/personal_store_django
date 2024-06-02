from django.urls import path
from . import views
urlpatterns=[
    path("items",views.viewItems.as_view()),
    path("comments",views.Comments.as_view()),
    path("accounts/create",views.CreateNewAccount.as_view()),
    path("accounts/login",views.login.as_view()),
    path("accounts/changePassword",views.ChangePassword.as_view()),
    path("accounts/editProfile",views.EditProfile.as_view()),
    path("accounts/viewProfile",views.ViewProfile.as_view()),
    path("accounts/delete",views.DeleteAccount.as_view())
]