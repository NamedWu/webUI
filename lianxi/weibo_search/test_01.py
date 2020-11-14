# from time import sleep
#
# from selenium import webdriver
#

class Test_weibo:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://m.weibo.cn/')

    def test_01(self):
        ele = self.driver.find_element_by_class_name('m-search')
        print("111111")
        ele.click()

    def test_02(self):
        ele = self.driver.find_element_by_class_name("card-main").find_elements_by_class_name("m-item-box")[-1]
        ele.click()
        sleep(10)

    # def test_03(self):
    #     lists = self.driver.find_element_by_class_name("card11").find_element_by_class_name(
    #         "card-list").find_elements_by_class_name("card4")
    #     print(lists)
    #
    # def teardown(self):
    #     self.driver.quit()


from time import sleep

from selenium import webdriver

# 需要将驱动路径改成自己的路径哦
driver = webdriver.Chrome()

url = "https://m.weibo.cn/"

driver.get(url)

# 点击搜索框
driver.find_element_by_class_name("m-search").click()

sleep(2)

# 点击【微博实时搜索】
driver.find_element_by_class_name("card-main").find_elements_by_class_name("m-item-box")[-1].click()

sleep(2)

# 查找list
def test_01():
    lists = driver.find_element_by_class_name("card11").find_element_by_class_name("card-list").find_elements_by_class_name("card4")
    print(lists)
    for i in lists:
        text = i.find_element_by_class_name('main-text').text
        span = i.find_element_by_class_name('m-link-icon')
        if span:
            src = span[0].find_element_by_tag_name("img").get_attribute("src")
            if "hot" in src:
                print(f"{text} 是 很热的头条")
            elif "new" in src:
                print(f"{text} 是 新的头条")
            elif "fei" in src:
                print(f"{text} 是 沸腾的头条")
            elif "recom" in src:
                print(f"{text} 是 推荐的头条")
            else:
                print(f"{text} 是 普通的头条")
