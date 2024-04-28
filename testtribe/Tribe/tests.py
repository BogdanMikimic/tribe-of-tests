from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from Tribe.views import homepage, story, my_notes

class HomepageTest(TestCase):

    def test_homepage_function_returns_the_right_html(self):
        # makes a request, goes through the views function and returns a response containing the html
        response = self.client.get('/')
        # tests what template was used by the function
        self.assertTemplateUsed(response, 'Tribe/homepage.html')

    def test_credit_returns_right_html(self):
        response = self.client.get('/story')
        self.assertTemplateUsed(response, 'Tribe/story.html')

    def test_my_notes_function_returns_the_right_webpage(self):
        response = self.client.get('/my_notes')
        self.assertTemplateUsed(response, 'Tribe/my_notes.html')