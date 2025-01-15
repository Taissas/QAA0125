import time
from pages.homepage import Homepage
from pages.product import ProductPage


def test_open_s6(browser):
    homepage = Homepage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is("Samsung galaxy s6")


def test_two_monitors(browser):
    homepage = Homepage(browser)
    homepage.open()
    homepage.click_monitor()
    time.sleep(3)
    homepage.check_products_count(2)
