from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # David has heard about this new cool game. He goes to check out it's homepage
        self.browser.get('http://localhost:8000')

        # He notices that the game has a "Test Tribe Home" word in the title
        self.assertIn('Tribe Home', self.browser.title)
        # self.fail('Finish the test')

        # He clicks on the main house and reads about the


if __name__=='__main__':
    unittest.main(warnings='ignore')


