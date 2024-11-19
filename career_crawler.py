from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
"""
CLASS_NAME = 'class name'
CSS_SELECTOR = 'css selector'
ID = 'id'
LINK_TEXT = 'link text'
NAME = 'name'
PARTIAL_LINK_TEXT = 'partial link text'
TAG_NAME = 'tag name'
XPATH = 'xpath'
"""

def scrape_career_links(url):
    # 使用 Chrome 浏览器，需要下载相应版本的 Chrome 驱动器，并将其路径传递给 webdriver.Chrome()
    # driver = webdriver.Chrome('/path/to/chromedriver')
    driver = webdriver.Edge()

    # 打开网页
    driver.get(url)
    card_elements = driver.find_element(by=By.CLASS_NAME, value="row positionsGroup careerCard")

    # 找到所有带有 career 关键字的链接
    #career_links = driver.find_elements_by_partial_link_text('Careers')
    career_links = driver.find_elements(By.PARTIAL_LINK_TEXT, 'Careers')
    print("career_links: ", career_links)

    # 点击每个链接并获取内容
    for link in career_links:
        # 点击链接
        #link.click()

        # 等待页面加载完成
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.TAG_NAME, 'body'))
        # )

        # 获取页面内容
        page_content = driver.page_source
        with open("page_content.txt", 'w', encoding='utf-8') as f:
            f.write(page_content)
        #print(page_content)  # 这里假设你想打印页面内容，你可以根据需要进行处理
        #time.sleep(5)

        # 返回到之前的页面，准备点击下一个链接
        driver.back()

    # 关闭浏览器
    #driver.quit()

# 调用函数并传入目标网站的 URL
scrape_career_links('https://www.comeet.com/jobs/tripleten/98.008')
