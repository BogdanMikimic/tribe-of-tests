from django.test import TestCase
from Tribe.views import *
from Tribe.models import Notes


class DatabaseTests(TestCase):
    """
    Test the database tables and entries
    """
    def test_saving_and_receiving_notes(self):
        # works directly on the database (on a test copy of it)
        # create 2 note objects and save them in the database
        first_note_object = Notes()
        first_note_object.text = 'The first (ever) note!'
        first_note_object.save()

        second_note_object = Notes()
        second_note_object.text = 'Note the second'
        second_note_object.save()

        # retrieve the objects from the database
        saved_items = Notes.objects.all()

        # check that they are 2
        self.assertEqual(len(saved_items), 2)

        # check that they contain the right data
        self.assertEqual(saved_items[0].text, 'The first (ever) note!')
        self.assertEqual(saved_items[1].text, 'Note the second')


class PagesRenderingTests(TestCase):

    def test_homepage_function_returns_the_right_html(self):
        # makes a request at a certain url, goes through the views function and returns a response containing the html
        response = self.client.get('/tribe_village')
        # tests what template was used by the function
        self.assertTemplateUsed(response, 'Tribe/tribe_village.html')

    def test_credit_returns_right_html(self):
        response = self.client.get('/story')
        self.assertTemplateUsed(response, 'Tribe/story.html')

    def test_my_notes_function_returns_the_right_webpage(self):
        response = self.client.get('/my_notes')
        self.assertTemplateUsed(response, 'Tribe/my_notes.html')

    def test_workshops_function_returns_the_right_webpage(self):
        response = self.client.get('/workshops')
        self.assertTemplateUsed(response, 'Tribe/workshops.html')

    def test_jungle_function_returns_the_right_webpage(self):
        response = self.client.get('/jungle')
        self.assertTemplateUsed(response, 'Tribe/jungle.html')

    def test_credits_page_form_POST_request_correctly_sends_a_submitted_note_data_to_database(self):
        # Fill in the form with a new note
        self.client.post('/my_notes', data={'item_text': 'Clean lint out of goat bellybutton'})
        # get the database last submission and check if it is your item
        self.assertEqual(Notes.objects.latest('text').text,
                         'Clean lint out of goat bellybutton',
                         'The last database submission is not "Clean lint out of goat bellybutton"' )

    def test_that_credits_page_returns_a_GET_redirect_after_a_POST_request(self):
        # make a post request (fill the form)
        response = self.client.post('/my_notes', data={'item_text': 'Clean lint out of goat bellybutton'})
        # check that response has status 302 (redirect)
        self.assertEqual(response.status_code, 302, 'The redirect after the POST request was not performed')
        # check that the redirected page is the initial page url
        self.assertEqual(response['location'], '/my_notes', f'The user was not redirected to the same page "/my_notes"')

    #TODO: check links