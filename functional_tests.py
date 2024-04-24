from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:  # This code runs once BEFORE EACH test
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:  # This code runs once AFTER EACH test
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  # this is a test (the name starts with test_)
        # David has heard about this new cool game. He goes to check out it's homepage
        self.browser.get('http://localhost:8000')

        # He notices that the game has a "Test Tribe Home" word in the title
        self.assertIn('Tribe Home', self.browser.title)
        # self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')


