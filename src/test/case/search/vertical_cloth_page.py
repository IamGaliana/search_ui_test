#! /usr/bin/evn python
# encoding:utf8
__author__ = 'gaoyanjun'


from src.test.common.search_common import *
from drivers.driver_handler import *
from conf.search_url import *
from src.utils.log_handler import *

QUERY_WORD = ''


class VerticalClothPage(unittest.TestCase):
    def test01_check_searchable(self):
        log_info('---------- check searchable ----------')
        log_info('  input query %s and send request ' % QUERY_WORD)
        self.searchcommon.send_search_query(unicode(QUERY_WORD, "utf-8"))

    def test02_check_vertical_area(self):
        log_info('---------- check vertical area ----------')
        self.searchcommon.vertical_search_check('cloth')

    def test03_check_breadcrumb(self):
        log_info('---------- check breadcrumb ----------')
        self.searchcommon.breadcrumb_check(unicode(QUERY_WORD, "utf-8"))

    def test04_check_tabs(self):
        log_info('---------- check tabs ----------')
        self.searchcommon.tabs_check()

    def test05_check_filter(self):
        log_info('---------- check filter ----------')
        self.searchcommon.filter_area_check()

    def test06_check_sort(self):
        log_info('---------- check sorting ----------')
        self.searchcommon.sort_bar_check()

    def test07_check_price(self):
        log_info('---------- check price ----------')
        self.searchcommon.price_box_check()

    def test08_check_destination(self):
        log_info('---------- check destination ----------')
        self.searchcommon.destination_check()

    def test09_check_checkboxes(self):
        log_info('---------- check checkboxes ----------')
        self.searchcommon.checkboxes_check('pub')

    def test10_check_module(self):
        log_info('---------- check module switch ----------')
        self.searchcommon.module_switch_check()

    def test11_check_top_pageturn(self):
        log_info('---------- check page turn on top ----------')
        self.searchcommon.page_turn_check()

    def test12_check_product_bigpic(self):
        log_info('---------- check products ----------')
        self.searchcommon.product_area_check('cloth', 'big_pic')

    def test13_check_product_list(self):
        log_info('---------- check products ----------')
        self.searchcommon.product_area_check('cloth', 'list')

    def test14_bottom_pageturn_check(self):
        log_info('---------- check page turn at bottom ----------')
        pass

    def test15_bottom_search(self):
        log_info('---------- check search box at bottom ----------')
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
    query_list = BasicFunc().get_query_list("vertical_cloth")
    for query in query_list:
        QUERY_WORD = query
        log_info("QUERY - %s" % query)
        suit = unittest.defaultTestLoader.loadTestsFromTestCase(VerticalClothPage)
        unittest.TextTestRunner().run(suit)