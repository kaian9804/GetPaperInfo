# GetPaperInfo
This code is used to get the main paper information (title, abstract) of certain topic from IEEE Xplore. Hope this code can help everyone to get research papers easily.

## Pre-requisites
- Python + Web crawler
- HTML
- Prepare the browser driver

Note: Not really require very stong techniques, you can learn during the hand-on project.

If you do not know how to get the browser driver, you can reference my previous repository (https://github.com/kaian0414/health-code), I introduced the the process in the "Environment Setting" part. In here, I used Google Chrome Driver.

## Coding, Demo and Result
While running the code, you need to fill in some information. Please see the code for detail requirement and setting.
- What keyword you are going to search?
- Want to get the information from which year?
- Until which year?
- How many pages you are going to search?

Like the following figure, you need to input the mentioned information, then it will automatically search for you.

![InputSample](https://github.com/kaian0414/GetPaperInfo/blob/main/input_sample.PNG)

In here, I saved paper id, title and abstract. As some records may not contain the author information, I did not save it sample coding. But you can add it back if you need. The paper id can help you easily to find the full paper. The link of the full paper should be "https://ieeexplore.ieee.org/document/{id}". Finally, the information is saved in excel file, namely {input_keyword}_{from_year}to{to_year}_p{num_pages}.xlsx.

![SaveExcelSample](https://github.com/kaian0414/GetPaperInfo/blob/main/save_excel_sample.PNG)
