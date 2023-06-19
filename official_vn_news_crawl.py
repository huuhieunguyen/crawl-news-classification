from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm.notebook import tqdm_notebook

import time
import csv
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

# Configure EdgeOptions for headless mode
edge_options = Options()
edge_options.headless = True

# Set the WebDriver executable path
webdriver_path = '/home/hieu/Desktop/edge_driver/'

# Create the WebDriver instance
driver = webdriver.Edge(service=Service(webdriver_path), options=edge_options)

# specify the URL of the website to crawl
url = "https://vnexpress.net/"

# maximize the browser window
driver.maximize_window()

# navigate to the URL
driver.get(url)

# wait for the page to load
time.sleep(2)

# Open the file and read the lines
# with open("../20_order_sub_cat.txt", "r") as file:
#     lines = file.readlines()
#     file.close()

# with open('py_20_news_links.txt', 'w') as f:
#     # Iterate over each line in the file
#     for url in tqdm_notebook(lines, desc="List all links", leave=True):
#         # Remove any leading or trailing whitespace
#         url = url.strip()
#         driver.get(url)
#         try:
#             articles_frame = driver.find_element(By.ID, 'automation_TV0')

#             all_articles_links = articles_frame.find_elements(By.CLASS_NAME, 'thumb-art')

#             for article_link in all_articles_links:
#                 links_in_a_tag = article_link.find_elements(By.TAG_NAME, 'a')
                
#                 for link_a in links_in_a_tag:
#                     href = link_a.get_attribute('href')
#                     if href and href.startswith('https://vnexpress.net/'):
#                         # article_urls.append(href)
#                         f.write(href + '\n')
#                         print(href)
#         except Exception as e:
#             print(url)
#             print(e)
#             pass

# Define the CSV file path
csv_file_path = 'official_1_data.csv'

field_names = ['Category', 'Sub Category', 'Title', 'Description', 'Content']

# Open the file and read the lines
with open("./official_1_news_urls.txt", "r") as file:
    lines = file.readlines()
    file.close()

# Create the CSV file and write the header row
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames = field_names)
    writer.writeheader()

    # Iterate over each line in the file
    for url in tqdm_notebook(lines, desc="List all links", leave=True):
        # Remove any leading or trailing whitespace
        url = url.strip()
        driver.get(url)
        time.sleep(1)
        print(driver.current_url)
        try:
            # Crawl the data
            article_category = driver.find_element(By.CSS_SELECTOR, '#dark_theme > section.section.page-detail.top-detail > div > div.sidebar-1 > div.header-content.width_common > ul > li:nth-child(1) > a')
            article_sub_category = driver.find_element(By.CSS_SELECTOR, '#dark_theme > section.section.page-detail.top-detail > div > div.sidebar-1 > div.header-content.width_common > ul > li:nth-child(2) > a')
            # article_time = driver.find_element(By.CSS_SELECTOR, '#dark_theme > section.section.page-detail.top-detail > div > div.sidebar-1 > div.header-content.width_common > span')
            article_title = driver.find_element(By.CSS_SELECTOR, '#dark_theme > section.section.page-detail.top-detail > div > div.sidebar-1 > h1')
            article_des = driver.find_element(By.CSS_SELECTOR, '#dark_theme > section.section.page-detail.top-detail > div > div.sidebar-1 > p')
            article_text = driver.find_element(By.CSS_SELECTOR,'#dark_theme > section.section.page-detail.top-detail > div > div.sidebar-1 > article')
            article_paragraphs = article_text.find_elements(By.CSS_SELECTOR,'p.Normal')
            content = '\n'.join([e.text for e in article_paragraphs])

            # Create a dictionary with the crawled data
            article_data = {
                'Category': article_category.text,
                'Sub Category': article_sub_category.text,
                'Title': article_title.text,
                'Description': article_des.text,
                'Content': content
            }

            # Append the data to the CSV file
            writer.writerow(article_data)

            # Print the data
            print(f"Cat: {article_category.text}")
            print(f"Sub Cat: {article_sub_category.text}")
            print(f"Title: {article_title.text}")
            print(f"Des: {article_des.text}")
            print(f"Content: {content}")

        except Exception as e:
            print(f"Error URL is: {url}")
            print(e)
            pass
    
    file.close()

print(f"Data has been exported to '{csv_file_path}'.")

# Close the browser
driver.quit()
