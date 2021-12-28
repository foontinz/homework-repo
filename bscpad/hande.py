import time
from selenium import webdriver

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import uuid


if __name__ == '__main__':

    with open('gmails.txt') as fp:
        mails = fp.readlines()
    with open('bsc.txt') as fp:
        adresses = fp.readlines()

    mails = [mail.strip() for mail in mails]
    adresses = [adress.strip() for adress in adresses]

    options = uc.ChromeOptions()

    #options.add_argument('--proxy-server=http://45.139.28.110:60427')

    for i in range(1):
        options.add_argument(f"user-agent=dwe2wd")
        browser = webdriver.Chrome(options=options)
        browser.get('https://swee.ps/uBCBDh_QGOxiVq')
        browser.implicitly_wait(10)
        browser.find_element(
            By.XPATH, '/html/body/div[2]/div[2]/div[5]/div[2]/form/div[3]/span/div/input').send_keys(mails[i])
        browser.find_element(
            By.XPATH, '/html/body/div[2]/div[2]/div[5]/div[2]/form/div[5]/span/div/input').send_keys(adresses[i])
        browser.find_element(
            By.XPATH, '/html/body/div[2]/div[2]/div[5]/div[2]/form/div[6]/span/div/input').send_keys(adresses[i])

        browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[5]/div[2]/form/div[7]/a').click()
        time.sleep(3)

    time.sleep(10)
