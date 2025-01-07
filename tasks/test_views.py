from django.test import TestCase, Client
from django.urls import reverse
from tasks.models import Task, Category
from django.utils import timezone

class TaskViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Test Category")
        self.task = Task.objects.create(
            title="Test Task",
            due_date=timezone.make_aware(timezone.datetime(2025, 1, 1, 12, 0, 0)),
            completed=False,
            category=self.category
        )

    def test_home_view_status_code(self):
        # Test the status code of the home view
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_template_used(self):
        # Test the template used by the home view
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'tasks/index.html')

    def test_home_view_context(self):
        # Test the context data of the home view
        response = self.client.get(reverse('home'))
        self.assertIn('to_do_tasks', response.context)
        self.assertIn('done_tasks', response.context)
        self.assertEqual(len(response.context['to_do_tasks']), 1)
        self.assertEqual(response.context['to_do_tasks'][0], self.task)
        self.assertEqual(len(response.context['done_tasks']), 0)

    def test_task_creation_view(self):
        # Test the task creation view
        response = self.client.post(reverse('create_task'), {
            'title': 'New Task',
            'due_date': timezone.now(),
            'completed': False,
            'category': self.category.id
        })
