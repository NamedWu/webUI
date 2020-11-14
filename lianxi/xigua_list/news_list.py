from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

url = "https://www.toutiao.com/"

driver.get(url)
def test_news_list():
    lists = driver.find_element_by_class_name('channel')
    print(lists.text)

def test_more_news():
    ele = driver.find_elements_by_class_name('channel-item')[12]
    ActionChains(driver).move_to_element(ele).perform()
    print("悬浮窗显示")
    driver.find_element_by_tag_name('军事').click()







