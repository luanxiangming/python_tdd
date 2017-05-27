import sys
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class FunctionalTest(StaticLiveServerTestCase):
	"""docstring for NewVistorTest"""
	@classmethod
	def setUpClass(cls):
		for arg in sys.argv:
			if 'liveserver' in arg:
				cls.server_url = 'http://' + arg.split('=')[1]
				return
			super().setUpClass()
			cls.server_url = cls.live_server_url

	def teatDownClass(cls):
		if cls.server_url == cls.live_server_url:
			super().tearDownClass()

	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = self.browser.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def get_item_input_box(self):
		return self.browser.find_element_by_id('id_text')