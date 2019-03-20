from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

# needed for admin honeypot path
from django.conf.urls import url

from project_manager import views as project_manager_views
# hello, create_project, update_project, create_phase, update_phase

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    # path('', views.homepage, name="home"),
    
    path("projects/", project_manager_views.render_projects),
    path("my-projects/<client_id>", project_manager_views.client_projects),
    path("create-project/", project_manager_views.create_project),
    path("update-project/<project_id>", project_manager_views.update_project),
    # path("admin/", include('admin_honeypot.urls', namespace='admin_honeypot')),
    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),

    
    # User management
    path(
        "users/",
        include("homergantt.users.urls", namespace="users"),
    ),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
