from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVistorTest(unittest.TestCase):
	"""docstring for NewVistorTest"""
	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# 用户查看应用首页
		self.browser.get('http://localhost:8000')

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

		table = self.browser.find_element_by_id('id_list_table')
		rows = self.browser.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1. Buy peacock feathers' for row in rows)
			)

		# 页面中又显示了一个输入框，可以输入其他待办事项
		# 用户输入了‘Use peacock feathers to make a fly’
		# 用户做事很有条理
		self.fail('Finish the test!')

		# 页面再次更新， 清单中显示了这两个待办事项

		# 用户想知道这个网站是否会记住他的清单

		# 用户看到网站为他生成了一个唯一的url
		# 而且页面中有一些文字来解说这个功能

		# 用户访问那个url发现他的待办事项列表还在

		# 用户满意地去睡觉了

if __name__ == '__main__':
	unittest.main()	




