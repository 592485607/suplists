from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')

        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_retrieve_it_later(self):

        #伊迪听说有一个很酷的在线待办事项应用
        # 她去看了这个应用首页
        self.browser.get('http://localhost:8000')
        print(self.browser.title)
        #她注意到网页的标题和头部都包含了"To-Do"这个词
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        #应用邀请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #她在一个文本框中输入了"buy peacock feathers"（购买孔雀羽毛）
        #伊迪丝的爱好是使用假蝇做饵钓鱼
        inputbox.send_keys('Buy peacock feathers')

        #她按回车键后,页面更新了。
        # 待办事项表格中显示了"1:Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)

        import time
        time.sleep(10)
        table = self.browser.find_element_by_id('id_list_table')

        rows = table.find_element_by_tag_name('tr')

        # self.assertTrue(
        #     any(row.text == '1: Buy peacock feathers' for row in rows),
        #     "New to-do item did not appear in table -- its text was:\n%s" % (
        #         table.text,
        #     )
        # )
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        #页面中又显示了一个文本框,可以输入其他的待办事项
        #她输入了:Use peacock feathers to make a fly"（使用孔雀羽毛做假蝇）

        # 伊迪丝做事很有条理
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # 页面再次更新，清单中显示了这两个待办事项
        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        # self.assertIn(
        #     '2: Use peacock feathers to make a fly',
        #     [row.text for row in rows]
        # )
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # 伊迪丝想知道这个网站是否会记住她的清单
        # 她看到网站为她生成了一个唯一的URL
        # 页面中有一些文字解说这个功能
        self.fail('Finish the test!')
        # 她访问那个URL，发现待办事项清单还在

        #她很满意，去睡觉了


if __name__ == '__main__':
    #warnings='ignore' 作用禁止抛出resourceWarning异常
    unittest.main(warnings='ignore')
