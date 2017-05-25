from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):

	def test_layout_and_styling(self):
		# 用户访问首页
		self.browser.get(self.server_url)
		self.browser.set_window_size(1024, 768)
		# 检查输入框居中显示
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width'] / 2,
			512,
			delta=5
			)
		# 新建一个清单，检查输入框依然居中显示
		inputbox.send_keys('testing\n')
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width'] / 2,
			512,
			delta=5
			)
