from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Project, ProjectMember, Task, Comment
from datetime import datetime

User = get_user_model()

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('testpass123'))

class ProjectModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
        )
        self.project = Project.objects.create(
            name='Test Project',
            description='Test Project Description',
            owner=self.user
        )

    def test_project_creation(self):
        self.assertEqual(self.project.name, 'Test Project')
        self.assertEqual(self.project.description, 'Test Project Description')
        self.assertEqual(self.project.owner, self.user)

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
        )
        self.project = Project.objects.create(
            name='Test Project',
            description='Test Project Description',
            owner=self.user
        )
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Task Description',
            status='To Do',
            priority='Medium',
            assigned_to=self.user,
            project=self.project,
            due_date=datetime.strptime('2024-12-31', '%Y-%m-%d')
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'Test Task Description')
        self.assertEqual(self.task.status, 'To Do')
        self.assertEqual(self.task.priority, 'Medium')
        self.assertEqual(self.task.assigned_to, self.user)
        self.assertEqual(self.task.project, self.project)
        self.assertEqual(self.task.due_date.strftime('%Y-%m-%d'), '2024-12-31')

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
        )
        self.project = Project.objects.create(
            name='Test Project',
            description='Test Project Description',
            owner=self.user
        )
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Task Description',
            status='To Do',
            priority='Medium',
            assigned_to=self.user,
            project=self.project,
            due_date='2023-12-31'
        )
        self.comment = Comment.objects.create(
            content='Test Comment',
            user=self.user,
            task=self.task
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.content, 'Test Comment')
        self.assertEqual(self.comment.user, self.user)
        self.assertEqual(self.comment.task, self.task)
