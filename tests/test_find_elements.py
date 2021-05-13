from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_title(browser):
    wait = WebDriverWait(browser, 5)
    browser.get(browser.url)
    wait.until(EC.title_is('Your Store'))
    assert browser.title == 'Your Store'


def test_find_el_main(browser):
    browser.get(browser.url)
    browser.find_element_by_xpath('//*[@id="logo"]/h1/a')
    browser.find_element_by_name('search')
    browser.find_element_by_id('cart')
    browser.find_element_by_link_text('iPhone')
    browser.find_elements_by_partial_link_text('Terms & Cond')


def test_find_el_catalog(browser):
    browser.get(browser.url + '/index.php?route=product/category&path=20')
    browser.find_element_by_css_selector('#top > div.container')
    browser.find_element_by_id('column-left')
    browser.find_elements_by_partial_link_text('Product Compare')
    browser.find_element_by_class_name('input-group')
    browser.find_element_by_xpath('//*[@id="search"]/span/button')


def test_find_el_card_product(browser):
    browser.get(browser.url + '/index.php?route=product/product&path=57&product_id=49')
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(.,"Tweet")]')))
    browser.find_element_by_xpath('//h1[contains(.,"Samsung Galaxy Tab 10.1")]')
    browser.find_element_by_xpath('//*[@id="button-cart"]')
    browser.find_element_by_id('input-quantity')
    browser.find_element_by_link_text('Write a review')
    browser.find_element_by_id('tab-description')


def test_find_el_login(browser):
    browser.get(browser.url + '/index.php?route=account/login')
    browser.find_element_by_id('input-email')
    browser.find_element_by_link_text('Continue')
    browser.find_element_by_xpath('//*[@id="input-password"]')
    browser.find_element_by_link_text('Forgotten Password')
    browser.find_element_by_xpath('//*[@id="content"]//form/input')


def test_el_admin(browser):
    browser.get(browser.url + '/admin/')
    browser.find_element_by_xpath("//img[@alt='OpenCart']")
    browser.find_element_by_name('username')
    browser.find_element_by_xpath('//h1[contains(.," Please enter your login details.")]')
    browser.find_element_by_id('input-password')
    browser.find_element_by_xpath('//button[contains(.," Login")]')
