from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button_add_to_cart(browser):
    browser.get(link)
    elem = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert elem != None, "Element not found!"