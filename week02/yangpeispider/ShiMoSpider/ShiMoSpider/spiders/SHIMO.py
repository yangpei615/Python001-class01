import scrapy
from selenium import webdriver
import time

class ShimoSpider(scrapy.Spider):
    
    try:
        name = 'SHIMO'
        allowed_domains = ['shimo.im']
        start_urls = ['http://shimo.im/']
        browser = webdriver.Chrome(f"D:\soft\python\chromedriver")
        # 需要安装chrome driver, 和浏览器版本保持一致
        # http://chromedriver.storage.googleapis.com/index.html
        
        browser.get('https://shimo.im/login?from=home')
        time.sleep(1)

        browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('123456789@qq.com')
        browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('test123456789')
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()

        cookies = browser.get_cookies() # 获取cookies
        print(cookies)
        time.sleep(3)

    except Exception as shimoEx:
        print(shimoEx)

    def parse(self, response):
        pass
