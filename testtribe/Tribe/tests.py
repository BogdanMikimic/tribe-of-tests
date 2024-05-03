from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from Tribe.views import *
from Tribe.models import Notes, Resources
from datetime import datetime
from decimal import Decimal


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

    def test_saving_receiving_and_modifying_data_from_the_resources_table(self):
        # Create an image file
        image = SimpleUploadedFile("Tribe/IMG/TestImages/test_image.png", b"file_content", content_type="image/png")
        # create a database record - a fictitious resource called wook
        new_resource = Resources()
        new_resource.resource_name = 'wool'
        new_resource.resource_image = image
        new_resource.max_storage_capacity = Decimal('42.53')
        new_resource.stored_resource_quantity = Decimal('35.12')
        new_resource.stored_resource_quantity_at_time = datetime.now()
        new_resource.production_per_second = Decimal('0.05')
        new_resource.consumption_per_second = Decimal('0.02')
        new_resource.net_production_per_second = Decimal('0.03')
        new_resource.one_unit_weight = Decimal('2.00')
        # save the object
        new_resource.save()
        # check the object is saved correctly
        saved_object = Resources.objects.latest('resource_name')
        self.assertIsNotNone(saved_object, 'There is no object instance saved in the database')
        self.assertEqual(saved_object.resource_name, 'wool', 'The name of the resource is not "wool"')
        self.assertTrue(saved_object.resource_image, 'There is no saved image')
        print('my stored value', saved_object.max_storage_capacity)
        self.assertEqual(saved_object.max_storage_capacity, Decimal('42.53'), 'The saved value for the max storage is not 42.53')
        self.assertEqual(saved_object.stored_resource_quantity, Decimal('35.12'), 'The saved value for the stored qty is not 35.12')
        self.assertTrue(saved_object.stored_resource_quantity_at_time, 'There is no time object saved')
        self.assertEqual(saved_object.production_per_second, Decimal('0.05'), 'The saved value for prod per sec is not 0.05')
        self.assertEqual(saved_object.consumption_per_second, Decimal('0.02'), 'The saved value for consumption per sec is not 0.02')
        self.assertEqual(saved_object.net_production_per_second, Decimal('0.03'), 'The saved value for net prod per sec is not 0.05')
        self.assertEqual(saved_object.one_unit_weight, Decimal('2.00'), 'The saved value for unit weight is not 2.00')



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