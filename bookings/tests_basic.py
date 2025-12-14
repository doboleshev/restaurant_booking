from django.test import TestCase
from django.urls import reverse

class BookingTests(TestCase):
    def test_home_page(self):
        """Test that home page loads correctly"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Мезонин")
