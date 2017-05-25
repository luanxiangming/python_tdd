from .base import FunctionalTest
import unittest

class ItemValidationTest(FunctionalTest):

	def test_cannot_add_empty_list_items(self):
		# 用户访问首页，提交了空待办事项
		# 输入框中没输入内容，用户按下回车键

		# 首页刷新并提示错误消息
		# 提示待办事项不能为空

		# 用户输入内容再次提交，这次成功了

		# 用户再次输入空待办事项

		# 在清单页面看到类似的错误消息

		# 输入文字之后就没问题了
		self.fail('write me!')

