from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import unittest

MAX_WAIT = 10

class NewVisitorTest(StaticLiveServerTestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def wait_for_row_in_list_table(self, row_text):
		start_time = time.time()
		while True: 
			try:
				table = self.browser.find_element_by_id('id_list_table')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return
			except (AssertionError, WebDriverException) as e:
				if time.time() - start_time > MAX_WAIT: 
					raise e
				time.sleep(0.5)

	def test_can_start_a_list_for_one_user(self):

		self.browser.get(self.live_server_url)

		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		
		self.assertIn('To-Do', header_text)

		#enter item in box
		input_box = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			input_box.get_attribute('placeholder'), 
			'Enter a to-do item'
			)

		#she types
		input_box.send_keys('Buy peacock feathers')

		#she hits enter
		input_box.send_keys(Keys.ENTER)

		self.wait_for_row_in_list_table('1: Buy peacock feathers')

		input_box = self.browser.find_element_by_id('id_new_item')
		input_box.send_keys('Use peacock feathers to make a fly')
		input_box.send_keys(Keys.ENTER)

		self.wait_for_row_in_list_table('1: Buy peacock feathers')
		self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

		#self.fail('Finish the test!')


	def test_multiple_users_can_start_lists_at_different_urls(self):
		self.browser.get(self.live_server_url)
		input_box = self.browser.find_element_by_id('id_new_item')
		input_box.send_keys('Buy peacock feathers')
		input_box.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy peacock feathers')

		#her list has a unique URL
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')

		#francis comes along

		self.browser.quit()
		self.browser = webdriver.Firefox()

		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('make a fly', page_text)

		input_box = self.browser.find_element_by_id('id_new_item')
		input_box.send_keys('Buy milk')
		input_box.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy milk')

		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url, edith_list_url)

		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertIn('Buy milk', page_text)


