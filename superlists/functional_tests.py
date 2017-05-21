from selenium import webdriver
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
		self.fail('Finish the test!')

		# 应用邀请用户输入一个待办事项

		# 用户在文本框中输入‘Buy peacock feathers’
		# 用户的爱好是用假蝇作饵钓鱼

		# 用户按回车键后页面更新了
		# 待办事项表格中显示了‘1. Buy peacock feathers’

		# 页面中又显示了一个输入框，可以输入其他待办事项
		# 用户输入了‘Use peacock feathers to make a fly’
		# 用户做事很有条理

		# 页面再次更新， 清单中显示了这两个待办事项

		# 用户想知道这个网站是否会记住他的清单

		# 用户看到网站为他生成了一个唯一的url
		# 而且页面中有一些文字来解说这个功能

		# 用户访问那个url发现他的待办事项列表还在

		# 用户满意地去睡觉了

if __name__ == '__main__':
	unittest.main()	




