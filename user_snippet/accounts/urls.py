from django.urls import path, include
from .views import UsersView, UserView, UserDeleteView


urlpatterns = [
    path(
        "profiles/",
        include(
            [
                path("", UsersView.as_view(), name="users"),
                path(
                    "<slug:slug>/",
                    include(
                        [
                            path("", UserView.as_view(), name="single-user"),
                            path(
                                "delete/",
                                UserDeleteView.as_view(),
                                name="user-delete",
                            ),
                        ]
                    ),
                ),
            ]
        ),
    ),
]