from django.test import TestCase
from tasks.forms import TaskForm
from tasks.models import Category

class TaskFormTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Test Category")

    def test_task_form_valid_data(self):
        # Test the form with valid data
        form = TaskForm(data={
            'title': 'Test Task',
            'due_date': '2025-01-01',
            'completed': False,
            'category': self.category.id
        })
        self.assertTrue(form.is_valid())

    def test_task_form_invalid_data(self):
        # Test the form with invalid data
        form = TaskForm(data={
            'title': '',
            'due_date': '',
            'completed': False,
            'category': self.category.id
        })
        self.assertFalse(form.is_valid())

    def test_task_form_missing_data(self):
        # Test the form with missing data
        form = TaskForm(data={})
        self.assertFalse(form.is_valid())

    def test_task_form_due_date_widget(self):
        # Test the due date widget of the form
        form = TaskForm()
        rendered_widget = form['due_date'].as_widget()
        self.assertIn('type="date"', rendered_widget)
        self.assertIn('class="datepicker"', rendered_widget)