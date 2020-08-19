from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = "/home/vitor/Documents/github/python/python_learn/selenium/chromedriver"

driver = webdriver.Chrome(path)

driver.get("https://techwithtim.net")