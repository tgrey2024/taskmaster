from django.test import TestCase, Client
from django.utils import timezone
from taskmaster.models import LogMessage
from django.urls import reverse

class TestLogMessageModel(TestCase):

    def setUp(self):
        self.log_message = LogMessage.objects.create(
            message="Test log message"
        )

    def test_log_message_creation(self):
        self.assertEqual(self.log_message.message, "Test log message")
        self.assertIsNotNone(self.log_message.created_at)

    def test_log_message_str(self):
        expected_str = f"'Test log message' logged on {self.log_message.created_at.strftime('%A, %d %B, %Y at %X')}"
        self.assertEqual(str(self.log_message), expected_str)


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_not_found_url(self):
        response = self.client.get('/non-existent-url/')
        self.assertEqual(response.status_code, 404)