from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

path = "/home/vitor/Documents/github/python/python_learn/selenium/chromedriver"
driver = webdriver.Chrome(path)

driver.get("https://google.com")

mywebsite = driver.find_element_by_name("q")
mywebsite.send_keys("vitor nascimento")
mywebsite.send_keys(Keys.RETURN)


sleep(5)

mywebsite = driver.find_element_by_name("q")
mywebsite.send_keys("Another test")
mywebsite.send_keys(Keys.RETURN)

#search = driver.find_element_by_name("s")
#search.send_keys("vitor nascimento")
#search.send_keys(Keys.RETURN)