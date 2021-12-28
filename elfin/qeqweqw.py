from selenium import webdriver

# set chromodriver.exe path
driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
# launch URL
driver.get("https://the-internet.herokuapp.com/windows")
# identify element
l = driver.find_element_by_link_text("Click Here")
l.click()
# obtain window handle of browser in focus
p = driver.current_window_handle
# obtain parent window handle
parent = driver.window_handles[0]
# obtain browser tab window
chld = driver.window_handles[1]
# switch to browser tab
driver.switch_to.window(chld)
print("Page title for browser tab:")
print(driver.title)
# close browser tab window
driver.close()
# switch to parent window
driver.switch_to.window(parent)
print("Page title for parent window:")
print(driver.title)
# close browser parent window
