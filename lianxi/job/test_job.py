from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

url = "http://www.51job.com"

driver.get(url)

ele = driver.find_element_by_css_selector('#kwdselectid').send_keys('python')
driver.find_element_by_css_selector('#work_position_input').click()

def test_01():
    lists = driver.find_elements_by_id('#work_position_click_center_right_list_000000')
    print(lists)