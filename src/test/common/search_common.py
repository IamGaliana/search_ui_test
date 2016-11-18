#! /usr/bin/env python
# encoding: utf8
__author__ = 'gaoyanjun'
import sys
sys.path.append("../../utils")

from drivers.driver_handler import *
from conf.search_elements import *
from src.utils.log_handler import *
import unittest
import time
import ConfigParser


class SearchCommon(DriverHandler, unittest.TestCase):
    def send_search_query(self, query):
        self.send_keys(SearchElements.SearchAreaElements.query_input, query)
        self.click(SearchElements.SearchAreaElements.search_btn)

    def get_tab_attribute(self):
        tabs = ()
        all_prod_tab = SearchElements.TabAreaElements.all_product_tab
        dd_sell_prod_tab = SearchElements.TabAreaElements.dd_sell_product_tab
        tabs = (all_prod_tab, dd_sell_prod_tab)
        return tabs

    def vertical_search_check(self, template='pub'):
        if template == 'pub':
            log_info('  -> vertical pub template')
            pub_main_area = SearchElements.VerticalPublicationElement.main_pub_area
            pub_main_img = SearchElements.VerticalPublicationElement.main_pub_img
            pub_main_title = SearchElements.VerticalPublicationElement.main_pub_title
            pub_main_preprice = SearchElements.VerticalPublicationElement.main_pub_pre_price
            pub_main_nowprice = SearchElements.VerticalPublicationElement.main_pub_now_price
            pub_main_discount = SearchElements.VerticalPublicationElement.main_pub_discount
            pub_main_author = SearchElements.VerticalPublicationElement.main_pub_author
            pub_main_press = SearchElements.VerticalPublicationElement.main_pub_press
            pub_main_star = SearchElements.VerticalPublicationElement.main_pub_star
            pub_main_comment = SearchElements.VerticalPublicationElement.main_pub_comment
            pub_main_intro = SearchElements.VerticalPublicationElement.main_pub_info
            pub_main_shopcart = SearchElements.VerticalPublicationElement.main_pub_shopcart
            pub_main_collect = SearchElements.VerticalPublicationElement.main_pub_collect

            is_main_area_exist = self.is_element_exist(pub_main_area)
            is_main_img_exist = self.is_element_exist(pub_main_img)
            is_main_title_exist = self.is_element_exist(pub_main_title)
            is_main_preprice_exist = self.is_element_exist(pub_main_preprice)
            is_main_nowprice_exist = self.is_element_exist(pub_main_nowprice)
            is_main_discount_exist = self.is_element_exist(pub_main_discount)
            is_main_author_exist = self.is_element_exist(pub_main_author)
            is_main_press_exist = self.is_element_exist(pub_main_press)
            is_main_star_exist = self.is_element_exist(pub_main_star)
            is_main_comment_exist = self.is_element_exist(pub_main_comment)
            is_main_intro_exist = self.is_element_exist(pub_main_intro)
            is_main_shopcart_exist = self.is_element_exist(pub_main_shopcart)
            is_main_collect_exist = self.is_element_exist(pub_main_collect)

            try:
                log_info('  ->check - main_area existence')
                self.assertTrue(is_main_area_exist)
                log_info('  ->check - main_image existence')
                self.assertTrue(is_main_img_exist)
                log_info('  ->check - main_title existence')
                self.assertTrue(is_main_title_exist)    
                log_info('  ->check - main_pre_price existence')
                self.assertTrue(is_main_preprice_exist)    
                log_info('  ->check - _main_now_price existence')
                self.assertTrue(is_main_nowprice_exist)    
                log_info('  ->check - main_discount existence')
                self.assertTrue(is_main_discount_exist)    
                log_info('  ->check - main_author existence')
                self.assertTrue(is_main_author_exist)    
                log_info('  ->check - main_image existence')
                self.assertTrue(is_main_press_exist)    
                log_info('  ->check - main_star existence')
                self.assertTrue(is_main_star_exist)                
                log_info('  ->check - main_comment existence')
                self.assertTrue(is_main_comment_exist)    
                log_info('  ->check - main_intro existence')
                self.assertTrue(is_main_intro_exist)    
                log_info('  ->check - main_shopcart existence')
                self.assertTrue(is_main_shopcart_exist)    
                log_info('  ->check - main_collect existence')
                self.assertTrue(is_main_collect_exist)
            except AssertionError, e:
                log_error('- [vertical_search_check] - assertion error, message:%s' % e.message)
            except:
                log_error('- [vertical_search_check] - '
                          'something was wrong ,not AssertionError, main area in pub template')

            shop_pub_area = SearchElements.VerticalPublicationElement.shop_pub_area
            shop_pub_sort = SearchElements.VerticalPublicationElement.shop_pub_sort
            shop_pub_list_press = SearchElements.VerticalPublicationElement.shop_pub_list_press
            shop_pub_list_price = SearchElements.VerticalPublicationElement.shop_pub_list_price
            shop_pub_list_comment = SearchElements.VerticalPublicationElement.shop_pub_list_comment
            shop_pub_list_cart = SearchElements.VerticalPublicationElement.shop_pub_list_cart
            shop_pub_list_collect = SearchElements.VerticalPublicationElement.shop_pub_list_collect

            is_shop_area_exist = self.is_element_exist(shop_pub_area)
            is_shop_sort_exist = self.is_element_exist(shop_pub_sort)
            is_shop_press_exist = self.is_element_exist(shop_pub_list_press)
            is_shop_price_exist = self.is_element_exist(shop_pub_list_price)
            is_shop_comment_exist = self.is_element_exist(shop_pub_list_comment)
            is_shop_cart_exist = self.is_element_exist(shop_pub_list_cart)
            is_shop_collect_exist = self.is_element_exist(shop_pub_list_collect)
            try:
                log_info('  ->check - shop_area existence')
                self.assertTrue(is_shop_area_exist)
                log_info('  ->check - shop_sort existence')
                self.assertTrue(is_shop_sort_exist)
                log_info('  ->check - shop_press existence')
                self.assertTrue(is_shop_press_exist)
                log_info('  ->check - shop_price existence')
                self.assertTrue(is_shop_price_exist)
                log_info('  ->check - shop_comment existence')
                self.assertTrue(is_shop_comment_exist)
                log_info('  ->check - shop_cart existence')
                self.assertTrue(is_shop_cart_exist)
                log_info('  ->check - shop_collect existence')
                self.assertTrue(is_shop_collect_exist)
            except AssertionError, e:
                log_error('- [vertical_search_check] - assertion error, message:%s' % e.message)
            except:
                log_error('- [vertical_search_check] - '
                          'something was wrong ,not AssertionError, shop area in pub template')
        elif template == 'mall':
            log_info('  ->vertical mall template: check products in vertical area')
            whole_area = SearchElements.VerticalMallElement.whole_area
            product_band = SearchElements.VerticalMallElement.product_band
            new_product1 = SearchElements.VerticalMallElement.new_product1
            new_product1_img = SearchElements.VerticalMallElement.new_product1_img
            new_product1_name = SearchElements.VerticalMallElement.new_product1_name
            new_product1_price = SearchElements.VerticalMallElement.new_product1_price

            is_whole_area_exist = self.is_element_exist(whole_area)
            is_product_band_exist = self.is_element_exist(product_band)
            is_new_product1_exist = self.is_element_exist(new_product1)
            is_new_product1_img_exist = self.is_element_exist(new_product1_img)
            is_new_product1_name_exist = self.is_element_exist(new_product1_name)
            is_new_product1_price_exist = self.is_element_exist(new_product1_price)
            try:
                log_info('  ->check - whole_area existence')
                self.assertTrue(is_whole_area_exist)
                log_info('  ->check - product_band existence')
                self.assertTrue(is_product_band_exist)
                log_info('  ->check - product existence')
                self.assertTrue(is_new_product1_exist)
                log_info('  ->check - product image existence')
                self.assertTrue(is_new_product1_img_exist)
                log_info('  ->check - product name existence')
                self.assertTrue(is_new_product1_name_exist)
                log_info('  ->check - product price existence')
                self.assertTrue(is_new_product1_price_exist)
            except AssertionError, e:
                log_error('- [vertical_search_check] - assertion error, message:%s' % e.message)
            except:
                log_error('- [vertical_search_check] - something was wrong ,not AssertionError, mall template')
        elif template == 'cloth':
            whole_area = SearchElements.VerticalClothElements.whole_area
            direct_shop_logo = SearchElements.VerticalClothElements.direct_shop_logo
            direct_shop_name = SearchElements.VerticalClothElements.direct_shop_name
            promote_info = SearchElements.VerticalClothElements.promote_info
            product_band = SearchElements.VerticalClothElements.product_band
            new_product1 = SearchElements.VerticalClothElements.new_product1
            new_product1_img = SearchElements.VerticalClothElements.new_product1_img
            new_product1_price = SearchElements.VerticalClothElements.new_product1_price

            is_whole_area_exist = self.is_element_exist(whole_area)
            is_shop_logo_exist = self.is_element_exist(direct_shop_logo)
            is_shop_name_exist = self.is_element_exist(direct_shop_name)
            is_promote_info_exist = self.is_element_exist(promote_info)
            is_product_band_exist = self.is_element_exist(product_band)
            is_new_product1_exist = self.is_element_exist(new_product1)
            is_new_product1_img_exist = self.is_element_exist(new_product1_img)
            is_new_product1_price_exist = self.is_element_exist(new_product1_price)
            try:
                log_info('  ->check - whole_area existence')
                self.assertTrue(is_whole_area_exist)
                log_info(' ->check - shop logo existence')
                self.assertTrue(is_shop_logo_exist)
                log_info('  ->check - shop name existence')
                self.assertTrue(is_shop_name_exist)
                log_info('  ->check - promote info existence' % is_promote_info_exist)
                self.assertTrue(is_promote_info_exist)
                log_info('  ->check - product band existence')
                self.assertTrue(is_product_band_exist)
                log_info('  ->check - products existence')
                self.assertTrue(is_new_product1_exist)
                log_info('  ->check - product image existence')
                self.assertTrue(is_new_product1_img_exist)
                log_info('  ->check - product price existence')
                self.assertTrue(is_new_product1_price_exist)
            except AssertionError, e:
                log_error('- [vertical_search_check] - assertion error, message:%s' % e.message)
            except:
                log_error('- [vertical_search_check] - something was wrong ,not AssertionError -, cloth area')
        else:
            pass

    def breadcrumb_check(self, query, template='common'):
        if template == 'vertical_pub':
            breadcrumb_all = SearchElements.BreadCrumbElements.vertical_pub_crumball
            query_word = SearchElements.BreadCrumbElements.vertical_pub_query
        else:
            breadcrumb_all = SearchElements.BreadCrumbElements.crumb_all
            query_word = SearchElements.BreadCrumbElements.search_word
            product_total_cnt = SearchElements.BreadCrumbElements.product_total
        is_breadcrumb_exists = self.is_element_exist(breadcrumb_all)
        is_query_exists = self.is_element_exist(query_word)
        try:
            log_info('  ->check - breadcrumb_all existence')
            self.assertTrue(is_breadcrumb_exists)
            log_info('  ->check - query existence')
            self.assertTrue(is_query_exists)
            if template != 'vertical_pub':
                is_total_cnt_exists = self.is_element_exist(product_total_cnt)
                log_info('  ->check - total count existence')
                self.assertTrue(is_total_cnt_exists)

            # breadcrumb_all_text = self.text(breadcrumb_all)
            # log_info('  ->check - actual breadcrumb_all text')
            # self.assertEqual(breadcrumb_all_text, u'全部', "breadcrumb_all text is wrong")
            query_text = self.text(query_word)
            log_info('  ->check - actual query text')
            self.assertEqual(query_text, query)
        except AssertionError, e:
            log_error('- [breadcrumb_check] - message:%s' % e.message)
        except UnicodeEncodeError, e:
            log_error('- [breadcrumb_check] - message:%s' % e.message)
        except:
            log_error('- [breadcrumb_check] - something was wrong ,neither AssertionError nor UnicodeEncodeError')

    def tabs_check(self):
        tab_elements = self.get_tab_attribute()
        all_product = tab_elements[0]
        dd_sell = tab_elements[-1]
        is_all_exists = self.is_element_exist(all_product)
        try:
            log_info("  ->check - all tab existence")
            self.assertTrue(is_all_exists)
            log_info("  ->check - dd_sell tab existence")
            is_dd_sell_exists = self.is_element_exist(dd_sell)
            self.assertTrue(is_dd_sell_exists)         
            
            log_info('  ->switch to dd_sell tab')
            self.click(dd_sell)
            is_dd_sell_selected = self.get_attribute(dd_sell, "class")
            self.assertEqual(is_dd_sell_selected, "now")
            
            log_info('  ->switch to all_product tab')
            self.click(all_product)
            is_all_selected = self.get_attribute(all_product, "class")
            self.assertEqual(is_all_selected, "now")
        except AssertionError, e:
            log_error('- [tabs_check] - message:%s' % e.message)        

        log_info('  ->success')

    def filter_area_check(self):
        filter_name = SearchElements.FilterAreaElements.left_part
        filter_value = SearchElements.FilterAreaElements.right_part
        is_name_exists = self.is_element_exist(filter_name)
        is_value_exists = self.is_element_exist(filter_value)
        try:
            log_info('  ->check - filter area left part existence')
            self.assertTrue(is_name_exists)
            log_info('  ->check - filter area right part existence')
            self.assertTrue(is_value_exists)
        except AssertionError, e:
            log_error('- [filter_area_check] - message:%s' % e.message)    

        log_info('  ->success')

    def sort_bar_check(self):
        default_sort = SearchElements.SortAreaElements.sort_default_btn
        sale_sort = SearchElements.SortAreaElements.sort_sale_btn
        review_sort = SearchElements.SortAreaElements.sort_review_btn
        publish_sort = SearchElements.SortAreaElements.sort_new_btn
        price_low_sort = SearchElements.SortAreaElements.sort_price_btn
        price_high_sort = SearchElements.SortAreaElements.sort_price_btn

        is_default_sort_exist = self.is_element_exist(default_sort)
        is_sale_exist = self.is_element_exist(sale_sort)
        is_review_sort_exist = self.is_element_exist(review_sort)
        is_publish_sort_exist = self.is_element_exist(publish_sort)
        is_lowprice_sort_exist = self.is_element_exist(price_low_sort)
        is_highprice_sort_exist = self.is_element_exist(price_high_sort)

        try:
            log_info("  ->check default sort bar existence")
            self.assertTrue(is_default_sort_exist)
            log_info("  ->check sale sort bar existence")
            self.assertTrue(is_sale_exist)
            log_info("  ->check _review sort bar existence")
            self.assertTrue(is_review_sort_exist)
            log_info("  ->check publish sort bar existence")
            self.assertTrue(is_publish_sort_exist)
            log_info("  ->check lowprice sort bar existence")
            self.assertTrue(is_lowprice_sort_exist)
            log_info("  ->check highprice sort bar existence")
            self.assertTrue(is_highprice_sort_exist)

            log_info('  ->click default sort')
            self.click(default_sort)
            default_class = self.get_attribute(default_sort[:-2], "class")
            self.assertEqual(default_class, "on")

            log_info('  ->click sale sort')
            self.click(sale_sort)
            sale_class = self.get_attribute(sale_sort[:-2], "class")
            self.assertEqual(sale_class, "on tools_to_float")

            log_info('  ->click review sort')
            self.click(review_sort)
            review_class = self.get_attribute(review_sort[:-2], "class")
            self.assertEqual(review_class, "on tools_to_float")

            log_info('  ->click publish time sort')
            self.click(publish_sort)
            publish_class = self.get_attribute(publish_sort[:-2], "class")
            self.assertEqual(publish_class, "on")

            log_info('  ->click low price sort')
            self.click(price_low_sort)
            price_low_class = self.get_attribute(price_low_sort+"/span", "class")
            self.assertEqual(price_low_class, "icon icon_t")

            log_info('  ->click high price sort')
            self.click(price_high_sort)
            price_high_class = self.get_attribute(price_high_sort+"/span", "class")
            self.assertEqual(price_high_class, "icon icon_b")

            log_info('  ->restore to default sort')
            self.click(default_sort)
            default_class = self.get_attribute(default_sort[:-2], "class")
            self.assertEqual(default_class, "on")
        except AssertionError, e:
            log_error('- [sort_bar_check] - message:%s' % e.message)

        log_info('  ->success')

    def price_box_check(self):
        price_low_input = SearchElements.SortAreaElements.sort_lowprice_input
        price_high_input = SearchElements.SortAreaElements.sort_highprice_input
        price_confirm_btn = SearchElements.SortAreaElements.price_change_btn
        price_clear_btn = SearchElements.SortAreaElements.price_clear_btn

        is_lowprice_input_exist = self.is_element_exist(price_low_input)
        is_highprice_input_exist = self.is_element_exist(price_high_input)
        try:
            log_info("  ->check low price textbox existence")
            self.assertTrue(is_lowprice_input_exist)

            log_info("  ->check high price textbox existence")
            self.assertTrue(is_highprice_input_exist)

            log_info('  ->input price, low price=10, high price=100')
            self.send_keys(price_low_input, "10")
            self.send_keys(price_high_input, "100")
            log_info('  ->click confirm button')
            self.click(price_confirm_btn)
            time.sleep(3)

            log_info('  ->clear price')
            self.click(price_low_input)
            self.click(price_clear_btn)
            self.assertEquals(self.text(price_low_input), "")
            self.assertEquals(self.text(price_high_input), "")
            self.click(price_confirm_btn)
            log_info('  ->click clear and confirm button')
            time.sleep(3)
        except AssertionError, e:
            log_error('- [price_box_check] - message:%s' % e.message)
        log_info('  ->success')

    def destination_check(self):
        destination_box = SearchElements.SortAreaElements.destination_box
        destination_select_box = SearchElements.SortAreaElements.destination_select_box
        is_destination_box_exist = self.is_element_exist(destination_box)
        try:
            log_info('  ->check destination box existence')
            self.assertTrue(is_destination_box_exist)
            log_info('  ->click destination box')
            self.click(destination_box)
            log_info('  ->check destination select box appearance')
            is_des_select_box_exist = self.is_element_exist(destination_select_box)
            self.assertTrue(is_des_select_box_exist)
        except AssertionError, e:
            log_error('- [destination_check] - message:%s' % e.message)
        log_info('  ->success')

    def checkboxes_check(self, template='pub'):
        log_info('  ->check checkboxes:')
        dd_sell_ckb = SearchElements.SortAreaElements.dd_sell_ckb
        stock_ckb = SearchElements.SortAreaElements.instock_ckb
        promo_ckb = SearchElements.SortAreaElements.promo_ckb
        exclusive_ckb = SearchElements.SortAreaElements.exclusive_ckb
        wph_ckb = SearchElements.SortAreaElements.wph_ckb
        pre_sale_ckb = SearchElements.SortAreaElements.presale_ckb
        oversea_ckb = SearchElements.SortAreaElements.oversea_ckb
        try:
            self.checkbox_verify(dd_sell_ckb, 'dd_sell_checkbox')
            self.checkbox_verify(stock_ckb, 'stock_checkbox')
            self.checkbox_verify(promo_ckb, 'promo_checkbox')
            self.checkbox_verify(exclusive_ckb, 'exclusive_checkbox')
            self.checkbox_verify(wph_ckb, 'wph_checkbox')
            self.checkbox_verify(pre_sale_ckb, 'pre_sale_checkbox')
            if template in ('mall', 'cloth'):
                self.checkbox_verify(oversea_ckb, 'oversea_checkbox')
        except AssertionError, e:
            log_error('- [checkboxes_check] - message:%s' % e.message)
        log_info('  ->success')

    def checkbox_verify(self, element, name):
        ckb_frame = SearchElements.SortAreaElements.ckb_frame
        class_name = self.get_attribute(element, "class")
        is_ckb_exist = self.is_element_exist(element)

        log_info('  ->check box existence for %s' % name)
        self.assertTrue(is_ckb_exist)

        # unchecked-checked
        # if class_name == "":
        #     print '  element is not checked now, click checkbox '
        #     self.mouse_hover(ckb_frame)
        #     self.click(ckb_frame)
        #     self.click(element)
        #     time.sleep(3)
        #     self.assertEqual(self.get_attribute(element, "class"), "on", "%s class should be 'on'" % class_name)
        #     print '  element is checked'
        #
        #     print '  element is checked now, click checkbox'
        #     self.click(ckb_frame)
        #     self.click(element)
        #     time.sleep(3)
        #     self.assertEqual(self.get_attribute(element, "class"), "", "%s class should be ''" % class_name)
        #     print '  element is un-checked'
        # # checked-unchecked
        # elif class_name == "on":
        #     print '  element is checked now, click checkbox'
        #     self.click(ckb_frame)
        #     self.click(element)
        #     time.sleep(3)
        #     self.assertEqual(self.get_attribute(element, "class"), "", "%s class should be ''" % class_name)
        #     print '  element is un-checked'
        #
        #     print '  element is not checked now, click checkbox'
        #     self.click(ckb_frame)
        #     self.click(element)
        #     time.sleep(3)
        #     self.assertEqual(self.get_attribute(element, "class"), "on", "%s class should be 'on'" % class_name)
        #    print '  element is un-checked'

    def module_switch_check(self):
        grid_btn = SearchElements.SortAreaElements.grid_btn
        list_btn = SearchElements.SortAreaElements.list_btn
        is_grid_exist = self.is_element_exist(grid_btn)
        is_list_exist = self.is_element_exist(list_btn)
        try:
            log_info("  -> check grid module existence")
            self.assertTrue(is_grid_exist)
            log_info("  -> check list module existence")   
            self.assertTrue(is_list_exist)
            
            log_info('  ->click grid module')
            self.click(grid_btn)
            grid_class = self.get_attribute(grid_btn, "class")
            self.assertEqual(grid_class, "on")
    
            log_info('  ->click list module')
            self.click(list_btn)
            list_class = self.get_attribute(list_btn, "class")
            self.assertEqual(list_class, "on")
    
            log_info('  ->restore to grid module')
            self.click(grid_btn)
            grid_class = self.get_attribute(grid_btn, "class")
            self.assertEqual(grid_class, "on")
        except AssertionError, e:
            log_error('- [module_switch_check] - message:%s' % e.message)
        log_info('  ->success')

    def page_turn_check(self):
        pageturn_left = SearchElements.SortAreaElements.left_pageturn_btn
        pageturn_right = SearchElements.SortAreaElements.right_pageturn_btn
        page_num_tab = SearchElements.SortAreaElements.page_num
        is_pageturn_left_exist = self.is_element_exist(pageturn_left)
        is_pageturn_right_exist = self.is_element_exist(pageturn_right)
        try:
            log_info("  -> check page turn left button existence")
            self.assertTrue(is_pageturn_left_exist)
            log_info("  -> check page turn right button existence")
            self.assertTrue(is_pageturn_right_exist)
                
            pageturn_left_class = self.get_attribute(pageturn_left, "class")
            pageturn_right_class = self.get_attribute(pageturn_right, "class")
            page_num = self.text(page_num_tab)
            # current is the first page
            if "none" in pageturn_left_class and "on" in pageturn_right_class:
                log_info('  ->page turn to right')
                self.click(pageturn_right)
                new_page_num = self.text(page_num_tab)
                self.assertTrue(int(new_page_num) == int(page_num) + 1)
    
                log_info('  ->page turn to left')
                self.click(pageturn_left)
                new_page_num = self.text(page_num_tab)
                self.assertTrue(int(new_page_num) == int(page_num))
        except AssertionError, e:
            log_error('- [page_turn_check] - message:%s' % e.message)

        log_info('  ->success')

    def product_area_check(self, template, mode="big_pic"):
        grid_btn = SearchElements.SortAreaElements.grid_btn
        list_btn = SearchElements.SortAreaElements.list_btn
        all_product_element = SearchElements.ProductAreaElements.all_products

        log_info('  ->loop in product list, template:%s, mode:%s' % (template, mode))
        if mode.lower() == 'big_pic':
            self.click(grid_btn)
            all_product_list = self.find_elements_list(all_product_element)
        elif mode.lower() == 'list':
            self.click(list_btn)
            all_product_list = self.find_elements_list(all_product_element)

        for i in range(len(all_product_list)):
                product = all_product_list[i]
                # cloth and mall template
                if template.lower() in ('cloth', 'mall'):
                    image = product.find_element_by_xpath(".//a[@class='pic']")
                    price = product.find_element_by_xpath(".//p[@class='price']/span").text
                    main_title = product.find_element_by_xpath(".//p[@class='name']/a[@name='itemlist-title']")\
                        .get_attribute('title')
                    sub_title = product.find_element_by_xpath(".//p[@class='search_hot_word']").text
                    #shop_name = product.find_element_by_xpath(".//p[@class='link']/a").text
                    if mode.lower() == 'big_pic':
                        star = product.find_element_by_xpath(".//p[@class='star']/span[@class='level']")
                        comment = product.find_element_by_xpath(".//p[@class='star']/a[@name='itemlist-review']")
                        #if template.lower() == 'cloth':
                            #pic_list_show = product.find_element_by_xpath(".//div[@class='pic_list_show']")
                    elif mode.lower() == 'list':
                        star = product.find_element_by_xpath(
                            ".//p[@class='search_star_line']/span[@class='search_star_black']")
                        comment = product.find_element_by_xpath(
                            ".//p[@class='search_star_line']/a[@name='itemlist-review']")
                elif template.lower() == 'pub':
                    image = product.find_element_by_xpath(".//a[@class='pic']")
                    price = product.find_element_by_xpath(
                        ".//p[@class='price']/span[1]").text
                    main_title = product.find_element_by_xpath(".//p[@class='name']/a[@name='itemlist-title']")\
                        .get_attribute('title')
                    if mode.lower() == 'big_pic':
                        sub_title = product.find_element_by_xpath(".//p[@class='search_hot_word']").text
                        star = product.find_element_by_xpath(".//p[@class='star']/span[@class='level']")
                        comment = product.find_element_by_xpath(".//p[@class='star']/a[@name='itemlist-review']")
                    elif mode.lower() == 'list':
                        sub_title = product.find_element_by_xpath(".//p[@class='detail']").text
                        book_author = product.find_element_by_xpath(".//p[@class='search_book_author']/span[1]")
                        star = product.find_element_by_xpath(
                            ".//p[@class='search_star_line']/span[@class='search_star_black']")
                        comment = product.find_element_by_xpath(
                            ".//p[@class='search_star_line']/a[@name='itemlist-review']")
                        publisher = product.find_element_by_xpath(".//p[@class='search_book_author']/span[2]")
                        cart_btn = product.find_element_by_xpath(".//p[@class='bottom_p']/a[@name='Buy']").text
                        collect_btn = product.find_element_by_xpath(".//p[@class='bottom_p']/a[@name='collect']").text

                #log_info('  ->product %s, main_title:%s, price:%s' % ((i+1), main_title, price))
                try:
                    log_info("  -> check product image existence")
                    self.assertIsNotNone(image)
                    log_info("  -> check product price existence")
                    self.assertIsNotNone(price)
                    log_info("  -> check product main_title existence")
                    self.assertIsNotNone(main_title)
                    log_info("  -> check product sub_title existence")
                    self.assertIsNotNone(sub_title)
                    log_info("  -> check product star existence")
                    self.assertIsNotNone(star)
                    log_info("  -> check product comment existence")
                    self.assertIsNotNone(comment)

                    if template.lower() == 'pub'and mode.lower() == 'list':
                        log_info("  -> check product book_author existence")
                        self.assertIsNotNone(book_author)
                        log_info("  -> check product publisher existence")
                        self.assertIsNotNone(publisher)
                        log_info("  -> check product cart_btn existence")
                        self.assertIsNotNone(cart_btn)
                        log_info("  -> check product collect_btn existence")
                        self.assertIsNotNone(collect_btn)
                except AssertionError, e:
                    log_error('- [product_area_check] - message:%s' % e.message)

        log_info('  ->success')

    def bottom_search_check(self, query):
        try:
            log_info('  ->send query to search box')
            self.send_keys(SearchElements.BottomSearchElements.bottom_search_box, query)
            log_info('  ->click search button')
            self.click(SearchElements.BottomSearchElements.bottom_search_btn)
        except:
            log_error('- [bottom_search_check] - something was wrong')
        log_info('  ->success')


class BasicFunc:
    def get_query_list(self, section_name):
        # get query from config file
        config_file = "../../data/search_query.ini"
        conf = ConfigParser.ConfigParser()
        query_list = []
        try:
            conf.read(config_file)
        except Exception, e:
            log_error("exception:", e.message)

        sections = conf.sections()
        for section in sections:
            if section == section_name:
                options = conf.options(section)
                for option in options:
                    query = conf.get(section, option)
                    query_list.append(query)
        return query_list