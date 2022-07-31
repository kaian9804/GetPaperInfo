# GetPaperInfo
This code is used to get the main paper information (title, abstract) of certain topic from IEEE Xplore. Hope this code can help everyone to get research papers easily.

## Pre-requisites
- Python + Web crawler
- HTML
- Prepare the browser driver

Note: Not really require very stong techniques, you can learn during the hand-on project.

If you do not know how to get the browser driver, you can reference my previous repository (https://github.com/kaian0414/health-code#environment-setting), I introduced the the process in the "Environment Setting" part. In here, I am using Google Chrome Driver.

## Coding and Demo
While running the code, you need to fill in some information. Please see the code for detail requirements and settings.
- What keyword you are going to search?
- Want to get the information from which year?
- Until which year?
- How many pages you are going to search?

Like the following figure, you need to input the mentioned information, then it will automatically search for you.

![InputSample](https://github.com/kaian0414/GetPaperInfo/blob/main/input_sample.PNG)

In here, I saved paper id, title and abstract. As some records may not contain the author information, I did not save it sample coding. But you can add it back if you need. The paper id can help you easily to find the full paper. The link of the full paper should be "https://ieeexplore.ieee.org/document/{id}". Finally, the information is saved in excel file, namely {input_keyword}_{from_year}to{to_year}_p{num_pages}.xlsx.

## Error Msg Update (31-July 2022)
Error Msg: ‘WebDriver’ object has no attribute 'find_element_by_xpath’

In latest version about WebDrive, it requires to use 'By' to find elements. For updated coding, it needs to import the package from selenium.webdriver.common.by import By and the coding is driver.find_element(By.XPATH, 'path').

The updated coding file: get_thesis_paper_220731.py

## Result
![SaveExcelSample](https://github.com/kaian0414/GetPaperInfo/blob/main/save_excel_sample.PNG)

## Special Statements
- This coding is just for learning, willing to assist students to find out the useful papers faster, please don't use it as other purpose.
- This coding is workable on 27-Jun-2022, if there is some changes on that website in the future, this coding may not fit.
- If you only want to get the information, actually, you can get it from JSON, this code is used to practise Python web crawler. 
