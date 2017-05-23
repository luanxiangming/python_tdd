from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(LiveServerTestCase):
	"""docstring for NewVistorTest"""
	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = self.browser.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		# 用户查看应用首页
		self.browser.get(self.live_server_url)

		# 用户看到网页标题和头部包含'To-Do'
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)	

		# 应用邀请用户输入一个待办事项
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

		# 用户在文本框中输入‘Buy peacock feathers’
		# 用户的爱好是用假蝇作饵钓鱼
		inputbox.send_keys('Buy peacock feathers')

		# 用户按回车键后页面更新了
		# 待办事项表格中显示了‘1. Buy peacock feathers’
		inputbox.send_keys(Keys.ENTER)
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')
		self.check_for_row_in_list_table('1: Buy peacock feathers')

		# 页面中又显示了一个输入框，可以输入其他待办事项
		# 用户输入了‘Use peacock feathers to make a fly’
		# 用户做事很有条理
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

		# 页面再次更新， 清单中显示了这两个待办事项
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

		# 另一个新用户francis访问网站

		## 我们使用新浏览器会话
		## 确保之前的用户edith的信息不会从cookie中泄露
		self.browser.quit()
		self.browser = webdriver.Chrome()

		# francis访问首页
		# 页面中看不到edith的清单
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('make a fly', page_text)

		# francis输入一个新待办事项，新建一个清单
		# 他不像edith那样兴趣盎然
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)

		# francis获得了他的唯一url
		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url, edith_list_url)

		# 这个页面还是没有edith的清单
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('make a fly', page_text)

		# 两个人很满意


if __name__ == '__main__':
	unittest.main()	




