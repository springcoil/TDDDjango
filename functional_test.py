#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_ide('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item'
                         )


        # She types "Buy peacock feathers" into a text box
        #(Edith's hobby is fly fishing)
        input.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy Peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows)
                        )


        # There is still a text bos inviting her to add another item. She
        # enters "Use peacock feathers to make a fly"
        # (Edith is very methodical)
        self.fail('Finish the test!')

# The page updates again, and now shows both items on her list

# Edit wonders whether the site will remember her list. The she sees that
# The site has generated a unique URL for her with explanatory text

# She visits the URL - her to-do list is still there

# Satisfied, she goes back to sleep
if __name__ == '__main__':
    unittest.main(warnings='ignore')
