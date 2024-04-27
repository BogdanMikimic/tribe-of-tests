from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:  # This code runs once BEFORE EACH test
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:  # This code runs once AFTER EACH test
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  # this is a test (the name starts with test_)
        # David has heard about this new cool game. He goes to check out it's homepage
        self.browser.get('http://localhost:8000')

        # He notices that the game has a "Tribe Home" word in the title
        self.assertIn('Tribe Home', self.browser.title)

        # He also notices that the title of the page asks him what is his name
        # below, there is a logo of a goat
        # and below that there is a text box that says 'your name'
        # he enters his name and presses enter and the greeting message changes to his name
        # and the name field dissapears


        self.fail('Test is not finished, finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')


