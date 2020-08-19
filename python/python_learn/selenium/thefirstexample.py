from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

path = "/home/vitor/Documents/github/python/python_learn/selenium/chromedriver"
driver = webdriver.Chrome(path)

driver.get("https://techwithtim.net")

mywebsite = driver.find_element_by_name("s")
mywebsite.send_keys("test")
mywebsite.send_keys(Keys.RETURN)


try:
	main = WebDriverWait(driver, 10).until(
			EC.presence_of_element_locate((By.ID, "main"))
		)
except:
	driver.quit()


print(main.text)

driver.quit()