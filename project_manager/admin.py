from django.contrib import admin

from project_manager.models import Architect, Client, Project, Phase, Task

# Register your models here.
admin.site.register(Architect)
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Phase)
admin.site.register(Task)
