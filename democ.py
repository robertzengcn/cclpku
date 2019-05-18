# coding = utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import pickle



class Demo():

    def __init__(self):
        browser = webdriver.Chrome()


    def chrome_settings(self):
        #browser = webdriver.Chrome()
        chromeOptions = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0}
        chromeOptions.add_experimental_option("prefs", prefs)
        self.browser = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options = chromeOptions)
        self.browser.maximize_window()

    def open_url(self, url):
        self.browser.get(url)

    def do_search(self):
        time.sleep(2)
        element = self.browser.find_element_by_id("kw")
        element.send_keys("selenium")
        time.sleep(2)
        self.browser.find_element_by_id("su").click()

    def click_sign_in_button(self):
        element_sign_in = self.browser.find_element_by_xpath('//*[@id="common-header"]/div/div/div[1]/div/div/div[2]/ul/li[2]/a/span[1]')
        element_sign_in.click()

    def sign_in_DYN365(self):
        ele = self.browser.find_element_by_xpath('//*[@id="mectrl_main_trigger"]/div/div[1]')
        #print(ele)
        ele.click()

    def send_email(self,email):
        #ele = self.browser.find_element_by_xpath('//*[@id="i0116"]')
        ele = self.browser.find_element_by_xpath('//*[@id="i0116"]')
        ele.send_keys(email)

    def click_next(self):
        ele = self.browser.find_element_by_xpath('//*[@id="idSIButton9"]')
        ele.click()

    def chose_sign_in_option(self):
        ActionChains(self.browser).move_by_offset(-100, -170).click().perform()

    def send_password(self):
        eles = self.browser.find_elements_by_tag_name('input')
        for ele in eles:
            name = ele.get_attribute('name')
            if name == 'passwd':
                ele.send_keys('Foxit@87654321')
            #print(ele.get_attribute('name'))

    def click_login_button(self):
        ele = self.browser.find_element_by_id('idSIButton9')
        ele.click()



    def exit_browser(self):
        self.browser.close()
        self.browser.quit()

    def goto_orderpage(self):
            html = self.browser.execute_script("return document.documentElement.innerHTML;")
            print(html)
            element = WebDriverWait(self.browser, 40).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/form/div/div[2]/div[1]/div/div/nav/div[1]/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div[2]/div/div[3]/div/div/button/div[2]/span/span[contains(text(), 'Sales')]")))
            element.click()
            orderelement = WebDriverWait(self.browser, 40).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/form/div/div[2]/nav/div/div/nav/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div[2]/div/div[2]/div[2]/div/button/span/span")))
            orderelement.click()










testDemo = Demo()
testDemo.chrome_settings()
testDemo.open_url("https://businesscentral.dynamics.com/")
time.sleep(5)
testDemo.sign_in_DYN365()
time.sleep(3)
testDemo.send_email('candy_li@foxitsoftware.com')
testDemo.click_next()
time.sleep(3)
testDemo.chose_sign_in_option()
time.sleep(5)
testDemo.send_password()
time.sleep(3)
testDemo.click_login_button()
time.sleep(3)
testDemo.click_login_button()
#jump to homepage
testDemo.open_url("https://businesscentral.dynamics.com/10333be4-6a7e-41e3-a272-c2a11625f23e/")
testDemo.goto_orderpage()

# testDemo.exit_browser()


