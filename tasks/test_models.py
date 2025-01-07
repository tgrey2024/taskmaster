from django.core.exceptions import ValidationError
from django.utils import timezone
from django.test import TestCase
from tasks.models import Task, Category

class TaskModelTest(TestCase):

    def setUp(self):
        # Set up non-modified objects used by all test methods
        self.category = Category.objects.create(name="Test Category")
        self.task = Task.objects.create(
            title="Test Task",
            due_date=timezone.make_aware(timezone.datetime(2025, 1, 1, 12, 0, 0)),
            completed=False,
            category=self.category
        )

    def test_task_creation(self):
        # Test task creation
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.due_date, timezone.make_aware(timezone.datetime(2025, 1, 1, 12, 0, 0)))
        self.assertEqual(self.task.completed, False)
        self.assertEqual(self.task.category, self.category)

    def test_task_completed(self):
        # Test the completed status of the task
        self.assertEqual(self.task.completed, False)
        self.task.completed = True
        self.assertEqual(self.task.completed, True)

    def test_task_category(self):
        # Test the category of the task
        self.assertEqual(self.task.category, self.category)

    def test_task_title_length(self):
        # Test the title length of the task
        long_title = "a" * 256
        with self.assertRaises(ValidationError):
            task = Task(
                title=long_title,
                due_date=timezone.now(),
                completed=False,
                category=self.category
            )
            task.full_clean()  # This will call the clean method and raise the ValidationError
            task.save()  # Ensure save is called after full_clean