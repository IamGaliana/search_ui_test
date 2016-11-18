#! /usr/bin/evn python
# encoding:utf8
__author__ = 'gaoyanjun'


from src.test.common.search_common import *
from drivers.driver_handler import *
from conf.search_url import *
from src.utils.log_handler import *

QUERY_WORD = ''


class VerticalPublicationPage(unittest.TestCase):
    def test01_check_searchable(self):
        log_info('---------- check searchable ----------')
        log_info('  input query %s and send request ' % QUERY_WORD)
        self.searchcommon.send_search_query(unicode(QUERY_WORD, "utf-8"))

    def test02_check_vertical_area(self):
        log_info('---------- check vertical area ----------')
        self.searchcommon.vertical_search_check('pub')

    def test03_check_breadcrumb(self):
        log_info('---------- check breadcrumb ----------')
        self.searchcommon.breadcrumb_check(unicode(QUERY_WORD, "utf-8"), 'vertical_pub')

    def test04_check_tuijian_list(self):
        pass

    def test05_bottom_search(self):
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
    query_list = BasicFunc().get_query_list("vertical_pub")
    for query in query_list:
        QUERY_WORD = query
        log_info("QUERY - %s" % query)
        suit = unittest.defaultTestLoader.loadTestsFromTestCase(VerticalPublicationPage)
        unittest.TextTestRunner().run(suit)