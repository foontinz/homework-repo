import time

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    option = webdriver.ChromeOptions()

    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option('useAutomationExtension', False)
    option.add_argument("--disable-blink-features=AutomationControlled")

    option.add_argument('--disable-notifications')

    with open('gmails.txt') as fp:
        mails = fp.readlines()
    with open('bsc.txt') as fp:
        adresses = fp.readlines()

    mails = [mail.strip() for mail in mails]
    for i in range(len(mails)):
        time.sleep(1)
        browser = webdriver.Chrome(options=option)
        browser.get('https://swee.ps/uBCBDh_QGOxiVq')
        time.sleep(20)
        exit()




    exit()
    while True:
        for mail in mails:
            gmail = mail.strip()
            bsc = adress.strip()
            print(gmail,adress)
            exit()

