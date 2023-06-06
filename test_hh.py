import time

import pytest
from selenium.webdriver.common.by import By


base_url = 'https://hh.ru/'


@pytest.mark.parametrize("name", [
    ("Тестировщик ПО")
])
@pytest.mark.hh_test
def test_hh_search(browser, name):
    browser.get(base_url)
    browser.find_element(By.ID, "a11y-search-input").send_keys(name)
    browser.implicitly_wait(3)
    browser.find_element(By.CLASS_NAME, "supernova-search-submit-text").click()
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, "div:nth-of-type(7) > .novafilters-group-wrapper > .novafilters-group__items > li:nth-of-type(2)  .bloko-radio__text > span:nth-of-type(1)").click()
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, "div:nth-of-type(15) > .novafilters-group-wrapper  .novafilters-list > li:nth-of-type(1)  .bloko-checkbox__text > span:nth-of-type(1)").click()
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, "[data-qa] .nova-control--GtG8Kpo7kAMGijnRbxtY:nth-of-type(19) [data-qa='serp__novafilter-item']:nth-of-type(1) [data-qa='serp__novafilter-title']").click()
    time.sleep(2)
    browser.find_element(By.CLASS_NAME, "bloko-custom-select__select").click()
    browser.find_element(By.CSS_SELECTOR, ".bloko-custom-select__option-list > div:nth-of-type(3)").click()
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, ".supernova-logo-wrapper > .supernova-logo.supernova-logo_hh-ru.supernova-logo_inversed").click()
    time.sleep(2)
    browser.refresh()