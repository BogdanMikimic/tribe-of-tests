from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

import unittest

maximum_wait_time = 10  # wait for maximum 10 seconds
class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self) -> None:  # This code runs once BEFORE EACH test
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:  # This code runs once AFTER EACH test
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        """
        Either finishes the test early if it passes, or waits the full 10 seconds
        """

        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'table_of_notes')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > maximum_wait_time:
                    raise e
                time.sleep(0.5)


    def test_can_start_a_list_and_retrieve_it_later(self):  # this is a test (the name starts with test_)
        # David has heard about this new cool game. He goes to check out it's homepage
        self.browser.get(self.live_server_url)

        # He notices that the game has a "Tribe Home" word in the title
        self.assertIn('Tribe Home', self.browser.title, '"Tribe Home" not in page title, check page title')

        # He also notices that there is another page called story and he decides to check it out

        self.browser.get(self.live_server_url + '/story')
        self.assertIn('Story', self.browser.title, '"Story" not in page title, check page title')
        # the page is empty for now, but he goes to the third page which is called "My Notes" and he notices
        # that the name of the page is "My Notes"

        self.browser.get(self.live_server_url + '/my_notes')
        self.assertIn('My Notes', self.browser.title, '"My Notes" not in page title, check page title')
        # He notices that on the "My notes" page"there is a header called "My Journey Notes"
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('My Journey Notes', header_text, 'There is no "My Journey Notes" h1 element')
        # he is invited to write his first note in there
        new_note = self.browser.find_element(By.ID, 'new_note_field')
        self.assertEqual(new_note.get_attribute('placeholder'), 'Enter a new note')
        # he types "Explore the story"
        new_note.send_keys('Explore the story')
        # he presses "Enter" and the page displays 1: Explore the story
        new_note.send_keys(Keys.RETURN)
        time.sleep(2)
        self.wait_for_row_in_list_table('Explore the story')
        # table = self.browser.find_element(By.ID, 'table_of_notes')
        # rows = table.find_elements(By.TAG_NAME, 'tr')
        # self.assertTrue(any(row.text == 'Explore the story' for row in rows))

        # Upon checking the pages individually by url, he checks that all the navigation links bring up the page they
        # are designed to do


        # self.fail('Test is not finished, finish the test')



