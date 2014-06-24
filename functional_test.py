#!/usr/bin/env python3
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app.
        # She goes to checkout its homepage
        self.browser.get('http://localhost:8000')

        # She notices te page title and header mention to-do list
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

# She is invited to enter a to-do item straight away

# She types "Buy peacock feathers" into a text box
#(Edith's hobby is fly fishing)

# When she hits enter, the page updates, and now the page lists
# "1: Buy Peacock feathers" as an item in a to-do list

# There is still a text bos inviting her to add another item. She
# enters "Use peacock feathers to make a fly"
# (Edith is very methodical)

# The page updates again, and now shows both items on her list

# Edit wonders whether the site will remember her list. The she sees that
# The site has generated a unique URL for her with explanatory text

# She visits the URL - her to-do list is still there

# Satisfied, she goes back to sleep
if __name__ == '__main__':
    unittest.main(warnings='ignore')
