#! /usr/bin/evn python
# encoding:utf8
__author__ = 'gaoyanjun'

from src.test.common.search_common import *
from drivers.driver_handler import *
from conf.search_url import *
from src.utils.log_handler import *


QUERY_WORD = ''


class NewClothPage(unittest.TestCase):
    def test01_check_searchable(self):
        log_info('test case 1: check searchable')
        log_info('  input query %s and send request ' % QUERY_WORD)
        self.searchcommon.send_search_query(unicode(QUERY_WORD, "utf-8"))

    def test02_check_breadcrumb(self):
        log_info('test case 2: check breadcrumb')
        self.searchcommon.breadcrumb_check(unicode(QUERY_WORD, "utf-8"))

    def test03_check_tabs(self):
        log_info('test case 3: check tabs')
        self.searchcommon.tabs_check()

    def test04_check_filter(self):
        log_info('test case 4: check filter')
        self.searchcommon.filter_area_check()

    def test05_check_sort(self):
        log_info('test case 5: check sorting')
        self.searchcommon.sort_bar_check()

    def test06_check_price(self):
        log_info('test case 6: check price')
        self.searchcommon.price_box_check()

    def test07_check_destination(self):
        log_info('test case 7: check destination')
        self.searchcommon.destination_check()

    def test08_check_checkboxes(self):
        log_info('test case 8: check checkboxes')
        self.searchcommon.checkboxes_check('pub')

    def test09_check_module(self):
        log_info('test case 9: check module switch')
        self.searchcommon.module_switch_check()

    def test10_check_top_pageturn(self):
        log_info('test case 10: check page turn on top')
        self.searchcommon.page_turn_check()
        self.longMessage = True

    def test11_check_product_bigpic(self):
        log_info('test case 11: check products')
        self.searchcommon.product_area_check('cloth', 'big_pic')

    def test12_check_product_list(self):
        log_info('test case 12: check products')
        self.searchcommon.product_area_check('cloth', 'list')

    @unittest.skip("test13_bottom_pageturn_check")
    def test13_bottom_pageturn_check(self):
        log_info('test case 13: check page turn at bottom')
        pass

    def test14_bottom_search(self):
        log_info('test case 14: check search box at bottom')
        self.searchcommon.bottom_search_check(unicode(QUERY_WORD, "utf-8"))

    @classmethod
    def setUpClass(cls):
        cls.searchcommon = SearchCommon("firefox")
        cls.searchcommon.goto(SearchURL.basic_search_url)
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        log_info(u". 退出浏览器")
        cls.searchcommon.quit()

if __name__ == '__main__':
    query_list = BasicFunc().get_query_list("new_cloth")
    failures = 0
    for query in query_list:
        QUERY_WORD = query
        log_info("QUERY - %s" % query)
        # suit = unittest.defaultTestLoader.loadTestsFromTestCase(NewClothPage)
        # unittest.TextTestRunner().run(suit)
        # result = unittest.TestResult()
        # suit(result)

        #testcase = NewClothPage('test01_check_searchable')
        #testcase.longMessage = True
        # runner = unittest.TextTestRunner()
        # runner.run(testcase)
        testsuite = unittest.TestSuite()
        testsuite.addTest(NewClothPage('test01_check_searchable'))
        testsuite.addTest(NewClothPage('test02_check_breadcrumb'))
        unittest.TextTestRunner().run(testsuite)
        res = unittest.TestResult()
        testsuite.run(res)
        #testsuite(res)
        print res