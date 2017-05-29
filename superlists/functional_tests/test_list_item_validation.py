from .base import FunctionalTest
import unittest

class ItemValidationTest(FunctionalTest):

	def get_error_element(self):
		return self.browser.find_element_by_css_selector('.has-error')


	def test_cannot_add_empty_list_items(self):
		# 用户访问首页，提交了空待办事项
		# 输入框中没输入内容，用户按下回车键
		self.browser.get(self.server_url)
		self.get_item_input_box().send_keys('\n')

		# 首页刷新并提示错误消息
		# 提示待办事项不能为空
		# error = self.get_error_element()
		# self.assertEqual(error.text, 'You cannot have an empty list item')

		# 用户输入内容再次提交，这次成功了
		self.get_item_input_box().send_keys('Buy milk\n')
		self.check_for_row_in_list_table('1: Buy milk')

		# 用户再次输入空待办事项
		self.get_item_input_box().send_keys('\n')
		# 在清单页面看到类似的错误消息
		# error = self.get_error_element()
		# self.assertEqual(error.text, 'You cannot have an empty list item')
		
		# 输入文字之后就没问题了
		self.get_item_input_box().send_keys('Make tea\n')
		self.check_for_row_in_list_table('1: Buy milk')
		self.check_for_row_in_list_table('2: Make tea')

	def test_cannot_add_duplicate_items(self):
		# 用户访问首页，新建一个清单
		self.browser.get(self.server_url)
		self.get_item_input_box().send_keys('Buy wellies\n')
		self.check_for_row_in_list_table('1: Buy wellies')

		# 他不小心输入了一个重复的待办事项
		self.get_item_input_box().send_keys('Buy wellies\n')

		# 他看到一条有帮助的错误信息
		self.check_for_row_in_list_table('1: Buy wellies')
		error = self.get_error_element()
		self.assertEqual(error.text, 'You have already got this in your list')

	def test_error_messages_are_cleared_on_input(self):
		self.browser.get(self.server_url)
		self.get_item_input_box().send_keys('\n')
		error = self.browser.find_elements_by_css_selector(
			'#id_text:invalid'
			)
		self.assertEqual(len(error), 1)
		self.get_item_input_box().send_keys('a')
		error = self.browser.find_elements_by_css_selector(
			'#id_text:invalid'
			)
		self.assertEqual(len(error), 0)
