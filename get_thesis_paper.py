import time
import math
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import xlsxwriter
from selenium.common.exceptions import NoSuchElementException
import selenium.webdriver.support.ui as ui

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
chrome = r'C://Program Files (x86)//Google//Chrome//Application//chromedriver.exe' # 本機chromedriver的位置, chromedriver需自行下載
driver = webdriver.Chrome(executable_path=chrome, options=option)

# input for your searching
input_keyword = input('Enter keyword: ')
from_year = input('from which year: ')
to_year = input('to which year: ')
num_pages = input('How many pages do you what to download: ') # In IEEE Xplore, each page shows 25 most relevant papers, you can decide how many pages you want
num_pages = int(num_pages)

# solve the issues on inputting the year incorrectly
if from_year > to_year:
    temp = from_year
    from_year = to_year
    to_year = temp
print(f'from {from_year} to {to_year}')

url = f'https://ieeexplore.ieee.org/search/searchresult.jsp?queryText={input_keyword}&highlight=true&returnFacets=ALL&returnType=SEARCH&matchPubs=true&ranges={from_year}_{to_year}_Year'
driver.get(url)

time.sleep(5)
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# dealing with number of pages issues
# 1. request less than 1
if num_pages < 1:
    num_pages = 1
# 2. request greater than the existing pages in IEEE Xplore
num_papers = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/main/div[1]/div[2]/xpl-search-dashboard/section/div/div[1]/span[1]/span[2]').text
num_papers = num_papers.replace(',', '')
num_papers = int(num_papers)
ieee_pages = math.ceil(num_papers / 25)
if num_pages > ieee_pages:
    num_pages = ieee_pages
    print(f'num_pages: {num_pages}')

# for saving the paper ids
id_list = []

def get_paper_id(current_page):
    print(f'current_page: {current_page}')
    div_in_this_page = driver.find_elements_by_class_name('List-results-items')
    for i in div_in_this_page:
        id = i.get_attribute('id')
        # check exist
        if (id in id_list):
            print('existed id')
        else:
            id_list.append(id)

    # go to next page
    next_class = f'stats-Pagination_arrow_next_{current_page + 1}'
    try:
        next_btn = driver.find_element_by_class_name(next_class)
        driver.execute_script('arguments[0].click();', next_btn)
        time.sleep(5)
    except NoSuchElementException:
        print('last page!')

# get paper id
for i in range(1, num_pages+1):
    current_page = i
    get_paper_id(current_page)

"""
# only save paper id to text file
text_file = open('links.txt', 'w')
for id in id_list:
    text_file.write(id + '\n')
text_file.close()
"""

# go through all paper webpages, and get the information
# what information will be selected depends on your needs, some papers have not provided the authors, so I will not take 'authors' into account in this sample
paper_info_list = []
for id in id_list:
    print(f'id: {id}')
    paper_link = f'https://ieeexplore.ieee.org/document/{id}'
    driver.get(paper_link)
    time.sleep(2)
    title = driver.find_element_by_class_name('document-title').text
    print(f'title: {title}')
    abstract = driver.find_element_by_class_name('abstract-text').text
    print(f'abstract: {abstract}')
    # authors = driver.find_element_by_class_name('authors-banner-row-middle').text
    # print(f'authors: {authors}')
    # paper_info_list.append([id, title, authors, abstract])
    paper_info_list.append([id, title, abstract])

# saving the paper information into excel file
excel_name = f'{input_keyword}_{from_year}to{to_year}_p{num_pages}.xlsx'
wb = xlsxwriter.Workbook(excel_name)
with xlsxwriter.Workbook(excel_name) as wb:
    ws = wb.add_worksheet()
    for r, d in enumerate(paper_info_list):
        ws.write_row(r, 0, d)