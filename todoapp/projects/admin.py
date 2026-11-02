from django.contrib import admin
from .models import Project,ProjectMember

class Projectadmin(admin.ModelAdmin):
    list_display=['name','max_members','status']
admin.site.register(Project,Projectadmin)
class Projectmemberadmin(admin.ModelAdmin):
    list_display=['member','project']
admin.site.register(ProjectMember,Projectmemberadmin)
