from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from Tribe.views import homepage, story, my_notes

class HomepageTest(TestCase):

    # ============ tests that the path in urls.py calls the right function in views.py ============
    def test_root_url_resolves_to_homepage_view(self):
        # tests if homepage routs to the right views function
        returned_object_containing_function = resolve('/')  # needs "/" before path even if in urls.py does not exist
        self.assertEqual(returned_object_containing_function.func, homepage)

    def test_credits_url_calls_proper_view_function(self):
        # this one uses the resolve function Django uses when he searches for the view function associated with a path
        # in this case ('/story') the path is the path to the story page
        # in this case resolve eiter finds the path and returns an object containing the function associated
        # or throws a juicy 404 error
        returned_object_containing_function = resolve('/story')  # needs "/" before path even if in urls.py does not exist
        # this one tests if the .function parameter of the returned object is the function that is called in views
        self.assertEqual(returned_object_containing_function.func, story)

    def test_my_notes_url_calls_proper_view_function(self):
        returned_object_containing_function = resolve('/my_notes')
        self.assertEqual(returned_object_containing_function.func, my_notes, '"My Notes" url did not returned the expected my_notes function')



    # ============ tests that the views.py function returns the right .html file ============

    def test_homepage_function_returns_the_right_html(self):
        # tests the homepage
        request = HttpRequest
        response = homepage(request)
        html = response.content.decode('utf-8')
        # tests that there is a html returned
        self.assertTrue(html.startswith('\n<!DOCTYPE html>'), 'Seems like your returned file is not a html file')
        # tests the title of the page
        self.assertIn('<title>Test Tribe Home</title>', html, 'The name of the page is not the expected one')
        # tests that the page loaded entirely
        self.assertTrue(html.endswith('</html>'))


    def test_credit_returns_right_html(self):
        # standard request object, method==get
        request = HttpRequest()
        # simulates a request to the story function I have defined in views.py that should return
        # a response object with various data, including the story.html.
        response = story(request)
        # extract the html as a string
        html = response.content.decode('utf-8')
        # check that is indeed a html file you got back (I am inheriting from base.html, so it starts with a newline)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>'), 'Seems like your returned file is not a html file')
        # checks that the title of the page is <title>Credits</title>
        self.assertIn('<title>The Story</title>', html, 'The name of the page is not the expected one')
        # checks that the file ends with <html> -that the whole page loaded was loaded
        self.assertTrue(html.endswith('</html>'), 'Looks like the page didn`t loaded all the way down')

    def test_my_notes_function_returns_the_right_webpage(self):
        request = HttpRequest()
        response = my_notes(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('\n<!DOCTYPE html>'), 'Seems like your returned file is not a html file')

        self.assertTrue(html.endswith('</html>'), 'Looks like the page didn`t loaded all the way down')