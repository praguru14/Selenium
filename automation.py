from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()
chrome_browser.get(
    'https://www.seleniumeasy.com/test/basic-first-form-demo.html')
print('Selenium Easy Demo' in chrome_browser.title)
btn = chrome_browser.find_element_by_class_name('btn-default')
print(btn.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user = chrome_browser.find_element_by_id('user-message')
user.clear()
user.send_keys('Cool')

btn.click()
disp = chrome_browser.find_element_by_id('display')

print(disp.get_attribute('innerHTML'))


chrome_browser.quit()
