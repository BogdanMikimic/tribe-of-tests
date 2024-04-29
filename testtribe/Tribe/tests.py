from django.test import TestCase
from Tribe.views import homepage, story, my_notes
from Tribe.models import Note


class DatabaseTests(TestCase):
    """
    Test the database tables and entries
    """
    def test_saving_and_receiving_notes(self):
        # create 2 note objects and save them in the database
        first_note_object = Note()
        first_note_object.text = 'The first (ever) note!'
        first_note_object.save()

        second_note_object = Note()
        second_note_object.text = 'Note the second'
        second_note_object.save()

        # retrieve the objects from the database
        saved_items = Note.objects.all()

        # check that they are 2
        self.assertEqual(len(saved_items), 2)

        # check that they contain the right data
        self.assertEqual(saved_items[0].text, 'The first (ever) note!')
        self.assertEqual(saved_items[1].text, 'Note the second')


class PagesRenderingTests(TestCase):

    def test_homepage_function_returns_the_right_html(self):
        # makes a request at a certain url, goes through the views function and returns a response containing the html
        response = self.client.get('/')
        # tests what template was used by the function
        self.assertTemplateUsed(response, 'Tribe/homepage.html')

    def test_credit_returns_right_html(self):
        response = self.client.get('/story')
        self.assertTemplateUsed(response, 'Tribe/story.html')

    def test_my_notes_function_returns_the_right_webpage(self):
        response = self.client.get('/my_notes')
        self.assertTemplateUsed(response, 'Tribe/my_notes.html')

    def test_post_request_and_response(self):
        # make a post request to the form field name = item_text with the data 'A new note'
        response = self.client.post('/my_notes', data={'item_text': 'A new note'})
        self.assertIn('A new note', response.content.decode())