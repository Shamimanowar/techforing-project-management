from django.contrib import admin
from .models import Project, Task, ProjectMember, User, Comment

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 0
    can_delete = False
    
    def has_change_permission(self, request, obj = None):
        return super().has_change_permission(request, obj)

class TaskInline(admin.TabularInline):
    model = Task
    extra = 0
    can_delete = True
    
    def has_change_permission(self, request, obj = None):
        return super().has_change_permission(request, obj)
    
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    can_delete = True
    
    def has_change_permission(self, request, obj = None):
        return super().has_change_permission(request, obj)
    

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined', 'last_login')
    search_fields = ('username', 'email')
    ordering = ['-date_joined', ]

    inlines = [
        ProjectInline,
        ]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'owner__username', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    ordering = ['-created_at', ]
    inlines = [
        TaskInline,
        ]

@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ('project__name', 'user__username', 'role',)
    search_fields = ('project__name', 'user__username')
    ordering = ['project__name', ]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'priority', 'assigned_to__username', 'project__name', 'created_at', 'due_date')
    search_fields = ('title', 'description')
    ordering = ['-created_at', ]
    inlines = [
        CommentInline,
        ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'user__username', 'task__title', 'task__project__name', 'created_at')
    search_fields = ('content', 'user__username')
    ordering = ['-created_at', ]