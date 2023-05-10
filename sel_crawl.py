from selenium import webdriver
from selenium.webdriver.common.by import By
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
from bs4 import BeautifulSoup
import time

# specify the URL of the website to crawl
url = "https://vnexpress.net/"

# create a new Edge browser instance
driver = webdriver.Edge()

# maximize the browser window
driver.maximize_window()

# navigate to the URL
driver.get(url)

# wait for the page to load
time.sleep(2)

################################################################################

nav_bar = driver.find_element(By.CSS_SELECTOR, '#wrap-main-nav > nav')

elements_removed_list = ["Video", "Podcasts", "Tất cả"]

new_navbar_list = []

for title in nav_bar.find_elements(By.TAG_NAME, 'li'):
    if title.text not in elements_removed_list:
        new_navbar_list.append(title.text)

# Remove blank elements from the new_nav_list
new_navbar_list = [x for x in new_navbar_list if x]

# Print the list without blank elements
# print(new_navbar_list)

sub = []

for menu_title in new_navbar_list:
    title = nav_bar.find_element(By.LINK_TEXT, f'{menu_title}')

    # create action chain object and move to the element
    action = ActionChains(driver)
    action.move_to_element(title)
    # click the item "Kinh doanh" and perform the operation
    action.perform()

    sub_categories_ul = driver.find_elements(By.CSS_SELECTOR, 'ul.sub')
    
    for sub_category_ul in sub_categories_ul:
        sub_categories_li = sub_category_ul.find_elements(By.TAG_NAME, 'li')
        for sub_category_li in sub_categories_li:
            sub.append(sub_category_li.text)

# Remove blank elements from the sub
sub = [x for x in sub if x]
print(sub)
    # # click the sub-item and perform the operation
    # sub_item = nav_bar.find_element(By.LINK_TEXT, "")
    # action.move_to_element(sub_item)
    # action.click(on_element=sub_item)
    # action.perform()
    # print(driver.current_url)