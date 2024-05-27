from django.urls import path
from . import views
urlpatterns=[
    path("",views.home_,name="homePage"),
    path("contect/",views.Contect,name="contect"),
    path("about/",views.about,name="about"),
    path("changeLanguage",views.changeLanguage,name="changeLanguage"),
    path("accounts/new",views.newaccound,name="newaccound"),
    path("accounts/login",views.login,name="login"),
    path("accounts/logout",views.logout,name="logout"),
 path("accounts/settings",views.settings,name="accountSettings")   ,
 path("accounts/delete",views.deletacc,name="deleteaccount"),
 path("accounts/changePassword",views.changePassword,name="changePassword"),
 path("account/changeProfile",views.changeProfiel,name="changeProfile"),
 path("item/<int:pk>",views.viewItem,name="viewItem"),
 path("item/<int:pk>/comments",views.comment,name="comments"),
 path("item/<int:itemPk>/comments/<int:commentPk>/delete",views.deleteComment,name="deleteComment"),
 path("items/category=<str:category>&sort=<str:sort>",views.home_,name="Items"),
 path("items/search",views.search,name="search"),
 path("item/<int:pk>/buy",views.buy,name="buy")
]