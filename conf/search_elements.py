#! /usr/bin/env python
#encoding:utf8
__author__ = 'gaoyanjun'


class SearchElements(object):

    class SearchAreaElements(object):
        query_input = "xpath->.//*[@id='key_S']"
        search_btn = "xpath->.//*[@id='form_search_new']/input[9]"
        category_select = "xpath->.//*[@id='search_all_category']"

    class TabAreaElements(object):
        all_product_tab = "xpath->.//*[@id = 'J_tab']/a[1]/li[text()='全部商品']"
        dd_sell_product_tab = "xpath->.//*[@id='J_tab']/a[2]/li[text()='当当自营']"

    class BreadCrumbElements(object):
        crumb_all = "xpath->.//a[@name='breadcrumb-all']"
        search_word = "xpath->.//span[@class='search_word']"
        product_total = "xpath->.//span[@class='sp total']"

        vertical_pub_crumball = "xpath->.//div[@class='breadcrumb']/div[@class='left']/span[1]"
        vertical_pub_query = "xpath->.//div[@class='breadcrumb']/div[@class='left']/" \
                                  "span[@class='current breadcrumb_lable']/span"

    class FilterAreaElements(object):
        left_part = "xpath->.//*[@id='navigation']/ul/li[1]/div[1]"
        right_part = "xpath->.//*[@id='navigation']/ul/li[1]/div[2]"

    class SortAreaElements(object):
        sort_default_btn = "xpath->.//*[@id='go_sort']/div/ul/li[1]/a"
        sort_sale_btn = "xpath->.//*[@id='go_sort']/div/ul/li[2]/a"
        sort_review_btn = "xpath->.//*[@id='go_sort']/div/ul/li[3]/a"
        sort_new_btn = "xpath->.//*[@id='go_sort']/div/ul/li[4]/a"
        sort_price_btn = "xpath->.//*[@id='go_sort']/div/ul/li[5]/a"

        sort_lowprice_input = "xpath->.//*[@id='input_lowprice']"
        sort_highprice_input = "xpath->.//*[@id='input_highprice']"
        price_change_btn = "xpath->.//*[@id='price_btn_yes']"
        price_clear_btn = "xpath->.//*[@id='price_btn_cls']"
        destination_box = "xpath->.//*[@id='go_sort']/div/ul/li[7]/div"
        destination_select_box = "xpath->.//*[@id='go_sort']/div/ul/li[7]/div/div"

        ckb_frame = "xpath->.//*[@id='go_sort']/div[@class='top']/div[@class='bottom']"
        dd_sell_ckb = "xpath->.//a[@name='sort-self-run']"
        instock_ckb = "xpath->.//a[@name='sort-instock']"
        promo_ckb = "xpath->.//a[@name='sort-promotion']"
        exclusive_ckb = "xpath->.//a[@name='exclusive_price']"
        wph_ckb = "xpath->.//a[@name='sort-wph']"
        presale_ckb = "xpath->.//a[@name='sort-pre-sale']"
        oversea_ckb = "xpath->.//a[@name='sort-overseas']"

        grid_btn = "xpath->.//a[@name='sort-grid']"
        list_btn = "xpath->.//a[@name='sort-list']"

        left_pageturn_btn = "xpath->.//*[@id='go_sort']/div/div[@class='data']/a[1]"
        right_pageturn_btn = "xpath->.//*[@id='go_sort']/div/div[@class='data']/a[2]"
        page_num = "xpath->.//*[@id='go_sort']/div/div[@class='data']/span[1]"

    class ProductAreaElements(object):
        all_products = "xpath->.//*[@class='con shoplist']/ul/li"
        product_image = "xpath->.//a[@name='itemlist-picture' and @class='pic']"
        product_main_title = "xpath->.//a[@name='itemlist-title']"
        product_sub_title = "xpath->.//p[@class='search_hot_word']"
        product_dd_sale_price = "xpath->.//*span[@class='search_now_price']"
        product_sale_price = "xpath->.//*span[@class='search_pre_price']"
        product_discount = "xpath->.//*span[@class='search_discount']"

        product_author = "xpath->.//a[@name='itemlist-author']"
        product_publisher = "xpath->.//*a[@name='P_cbs']"

        product_star = "xpath->.//p[@class='star']/span[@class='level']"
        product_comment = "xpath->.//p[@clas='star']/a[@name='itemlist-review']"

        product_shop = "xpath->.//p[@class='link']/a[@name='itemlist-shop-name']"

        product_detail = "xpath->.//*p[@class='detail']"
        product_cart = "xpath->.//*a[@name='Buy' and @class='search_btn_cart']"
        product_collect = "xpath->.//*a[@name='collect' and @class='search_btn_collect']"

    class BottomPageTurnElements(object):
        prev_button = "xpath->.//div[@class='paging']/ul[@name='Fy']/li[1]/a"
        current_page = "xpath->.//div[@class='paging']/ul[@name='Fy']/li[2]/a"
        next_page = "xpath->.//div[@class='paging']/ul[@name='Fy']/li[3]/a"
        next_button = "xpath->.//div[@class='paging']/ul[@name='Fy']/li[4]/a"
        page_input = "xpath->.//div[@class='paging']/ul[@name='Fy']/li[@class='page_input']/input[@id='t__cp']"
        confirm_button = \
            "xpath->.//div[@class='paging']/ul[@name='Fy']/li[@class='page_input']/input[@id='click_get_page']"

    class BottomSearchElements(object):
         bottom_search_box = "xpath->.//input[@id='relate_search']"
         bottom_search_btn = "xpath->.//input[@name='search-button']"

    class VerticalClothElements(object):
        whole_area = "xpath->.//*[@id='vshop_direct']"
        direct_shop_logo = "xpath->.//*[@id='vshop_direct']/div[1]/div/a[@name='shopdirect-shop-logo']"
        direct_shop_name = "xpath->.//*[@id='vshop_direct']/div[1]/div/a[@name='shopdirect-shop-name']"
        promote_info = "xpath->.//*[@id='vshop_direct']/div[1]/p[1]/a"

        product_band = "xpath->.//*[@id='vshop_direct']/div[@class='cloth_band_show']"
        new_product1 = "xpath->.//div[@id='shop_page']/ul/li[1]/a[@name='shopdirect-new-product']"
        new_product1_img = "xpath->.//div[@id='shop_page']/ul/li[1]/a[@name='shopdirect-new-product']/img"
        new_product1_price = \
            "xpath->.//div[@id='shop_page']/ul/li[1]/a[@name='shopdirect-new-product']/span[@class='price']"

    class VerticalMallElement(object):
        whole_area = "xpath->.//*[@id='vshop_direct']"
        product_band = "xpath->.//*[@id='vshop_direct']/div[@class='cloth_band_show']"
        new_product1 = "xpath->.//div[@id='shop_page']/ul/li[1]"
        new_product1_img = "xpath->.//div[@id='shop_page']/ul/li[1]/a[@class='pic']/img"
        new_product1_name = "xpath->.//div[@id='shop_page']/ul/li[1]/a[@class='name']"
        new_product1_price = "xpath->.//div[@id='shop_page']/ul/li[1]/p[@class='price_p']/span"

    class VerticalPublicationElement(object):
        main_pub_area = "xpath->.//*[@id='search_book_main']"
        main_pub_img = "xpath->.//*[@id='search_book_main']/a[@class='search_result_pic']/img"
        main_pub_title = "xpath->.//*[@id='search_book_main']/div/h3/a[@name='main-product-title']/span"
        main_pub_now_price = \
            "xpath->.//*[@id='search_book_main']/div/p[@class='search_result_compare']/span[@class='search_now_price']"
        main_pub_pre_price = \
            "xpath->.//*[@id='search_book_main']/div/p[@class='search_result_compare']/span[@class='search_pre_price']"
        main_pub_discount = \
            "xpath->.//*[@id='search_book_main']/div/p[@class='search_result_compare']/span[@class='search_discount']"
        main_pub_author = \
            "xpath->.//*[@id='search_book_main']/div/p[@class='search_book_author']/span[@name='main-product-author']"
        main_pub_press = \
            "xpath->.//*[@id='search_book_main']/div/p[@class='search_book_author']/a[@name='main-product-press']"
        main_pub_star = \
            "xpath->.//*[@id='search_book_main']/div/p[@class='search_star_line']/span[@class='search_star_black']"
        main_pub_comment = \
            "xpath->.//*[@id='search_book_main']/div/p[@class='search_star_line']/a[@name='main-product-review']"
        main_pub_info = \
            "xpath->.//*[@id='search_book_main']/div/p[@class='search_book_intro']"
        main_pub_shopcart = \
            "xpath->.//*[@id='search_book_main']/div/p[6]/a[@name='main-product-add-to-cart']"
        main_pub_collect = \
            "xpath->.//*[@id='search_book_main']/div/p[6]/a[@name='main-product-collect']"
        shop_pub_area = "xpath->.//div[@class='search_result_bottom']"
        shop_pub_sort = \
            "xpath->.//div[@class='search_result_bottom']/div[@class='search_result_sort']/select[@name='psort']"
        shop_pub_list_press = \
            "xpath->.//div[@class='search_result_bottom']/ul/li[1]/ul/li[@class='search_result_press']"
        shop_pub_list_price = \
            "xpath->.//div[@class='search_result_bottom']/ul/li[1]/ul/li[@class='search_result_price']"
        shop_pub_list_comment = \
            "xpath->.//div[@class='search_result_bottom']/ul/li[1]/ul/li[@class='search_result_comment']"
        shop_pub_list_cart = \
            "xpath->.//div[@class='search_result_bottom']/ul/li[1]/ul/li[@class='search_result_btn']/" \
            "a[@class='search_btn_cart']"
        shop_pub_list_collect = \
            "xpath->.//div[@class='search_result_bottom']/ul/li[1]/ul/li[@class='search_result_btn']/" \
            "a[@class='search_btn_collect']"