from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.home,
        name="home",
    ),
    path(
        "about",
        views.about,
        name="about",
    ),
    # int:pk = integer:primaryKey
    path(
        "contact/<int:pk>",
        views.contact,
        name="contact",
    ),
    path(
        "delete/<int:pk>",
        views.delete_contact,
        name="delete",
    ),
    path(
        "add-contact",
        views.add_contact,
        name="add_contact",
    ),
    # cant just use views.login because that is a built in function
    path("login/", views.login_user, name="login"),
    # cant just use views.logout because that is a built in function
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("update_user", views.update_user, name="update_user"),
    path("update_password", views.update_password, name="update_password"),
]
