from django.contrib import admin
from .models import Project, ProjectMember


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "max_members", "status"]


admin.site.register(Project, ProjectAdmin)


class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ["member", "project"]


admin.site.register(ProjectMember, ProjectMemberAdmin)
