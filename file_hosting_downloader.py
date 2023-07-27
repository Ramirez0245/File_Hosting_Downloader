from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Add your URL links to URL_LIST
URL_LIST = ['https://thdisc-my.sharepoint.com/:f:/g/personal/example']
#Add website substring to check for comparison  and xpath to click on to download
FILE_HOSTING_LIST = [ 
        {'url_list': "mega.nz", 'xpath': '/html/body/div[6]/div[2]/div[2]/section/div[1]/div/div[4]/div[3]/div[2]/div[1]/button'},
        {'url_list': 'my.sharepoint', 'xpath': '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/div/button/span/span/span'} 
    ]
#click by xpath
def driverclick_byxpath(xpath, driver):
    driver.find_element(By.XPATH, xpath).click()
    
#import list of url and list of file hosting
def file_hosting_downloader(URL_LIST, FILE_HOSTING_LIST):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)

    if isinstance(URL_LIST, list) & isinstance(FILE_HOSTING_LIST, list):
        for url in URL_LIST:
            for item in FILE_HOSTING_LIST:
                if item["url_list"] in url:
                    driver.get(url)
                    time.sleep(3)
                    driverclick_byxpath(item['xpath'], driver)
                    time.sleep(180)

# __name__ special variables
if __name__ == '__main__':
    file_hosting_downloader(URL_LIST, FILE_HOSTING_LIST)

