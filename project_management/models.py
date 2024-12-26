from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from external.models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group, Permission

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(
        Group,
        related_name='project_management_users',
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        verbose_name=_('groups'),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='project_management_user_permissions',
        blank=True,
        help_text=_('Specific permissions for this user.'),
        verbose_name=_('user permissions'),
    )

class Project(BaseModel):
    name = models.CharField(max_length=255, help_text=_("What is the name of the project?"))
    description = models.TextField(help_text=_("What is the project about?"))
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_projects', help_text=_("Who is the owner of the project?"))

class ProjectMember(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Member', 'Member'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, help_text=_("What is the role of the member?"))

class Task(BaseModel):
    STATUS_CHOICES = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    ]
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(help_text=_("What is the task about?"))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, help_text=_("What is the status of the task?"))
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, help_text=_("What is the priority of the task?"))
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks', help_text=_("Who is assigned to this task?"))
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks', help_text=_("Which project does this task belong to?"))
    due_date = models.DateTimeField(_("Expiry Date"), help_text=_("What is the expiry date of the task?"))

class Comment(BaseModel):
    content = models.TextField(help_text=_("What is the content of the comment?"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', help_text=_("Who made the comment?"))
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments', help_text=_("Which task does this comment belong to?"))
