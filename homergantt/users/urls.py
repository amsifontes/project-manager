from django.urls import path

from homergantt.users.views import (
    user_list_view,
    user_redirect_view,
    user_update_view,
    user_detail_view,
)
from project_manager.views import (
    render_projects,
)
app_name = "users"
urlpatterns = [
    path("", view=user_list_view, name="list"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    # path("<str:username>/", view=render_projects, name="detail"), JJW - Stacy - michael
]
