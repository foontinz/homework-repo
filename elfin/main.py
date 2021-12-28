import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def options_setup():
    option = webdriver.ChromeOptions()
    option.add_extension('metamask.crx')
    option.add_argument('--disable-notifications')

    return option


def click_xy(x, y):
    ac.move_by_offset(x, y).click().perform()
    ac.move_by_offset(-x, -y).perform()


def game_auth():
    time.sleep(1)
    elem = browser.find_element(By.ID, 'GameCanvas')
    ac.move_to_element_with_offset(elem, 748, 660).click().perform()
    time.sleep(1)
    ac.move_to_element_with_offset(elem, elem.size['width']/2, elem.size['height']/2 ).click().perform()
    time.sleep(2)

    swith_window(0)
    browser.refresh()
    browser.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div[4]/div[2]/button[2]').click()
    browser.implicitly_wait(1)
    browser.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
    time.sleep(0.5)
    try:
        browser.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[3]/footer/button[2]').click()
    except:
        pass
    swith_window(1)
    browser.find_element(By.XPATH,'/html/body/div[1]/input').click.send_keys('nigger')
    browser.find_element(By.XPATH,'/html/body/div[1]/input').send_keys('nigger')

    print(len(browser.window_handles))



def metamask_auth():
    password = '7shebeirfb1Ebeh'
    with open('seed.txt') as fp:
        seed = fp.read()
    print('Importing metamask')
    swith_window(0)
    browser.implicitly_wait(1)
    browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/button').click()
    browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button').click()
    browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]').click()
    browser.implicitly_wait(3)
    browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/form/div[4]/div[1]/div/input').send_keys(seed)
    browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/form/div[5]/div/input').send_keys(password)
    browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/form/div[6]/div/input').send_keys(password)
    browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/form/div[7]/div').click()

    browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/form/button').click()
    print('Waiting for importing metamask')
    browser.implicitly_wait(10)
    try:
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/button').click()
    except:
        print('Couldn`t import metamask')

    browser.find_element(By.XPATH, '/html/body/div[2]/div/div/section/header/div/button').click()
    browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[1]/div/span').click()
    browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/button').click()
    browser.find_element(By.XPATH,
                         '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/label/input').send_keys(
        'BSC')
    browser.find_element(By.XPATH,
                         '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/label/input').send_keys(
        'https://bsc-dataseed.binance.org/')
    browser.find_element(By.XPATH,
                         '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/label/input').send_keys(
        '56')
    browser.find_element(By.XPATH,
                         '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/label/input').send_keys(
        'BNB')
    browser.find_element(By.XPATH,
                         '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]/button[2]').click()


def swith_window(i):
    # 1 - game
    # 0 - meta
    browser.switch_to.window(browser.window_handles[i])


if __name__ == '__main__':
    option = options_setup()
    browser = webdriver.Chrome(options=option)
    ac = ActionChains(browser)

    browser.get('https://game.elfinkingdom.com/')
    browser.maximize_window()

    metamask_auth()
    swith_window(1)
    time.sleep(3)
    game_auth()

    exit()
    xpath = '/html/body/div[1]/nav/div[3]/div[1]/button'
    browser.find_element(By.XPATH, xpath).click()

    # print(browser.title)
