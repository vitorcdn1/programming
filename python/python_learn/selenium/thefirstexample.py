from selenium import webdriver

path = "/home/vitor/Documents/github/python/python_learn/selenium/chromedriver"
driver = webdriver.Chrome(path)

driver.get("https://google.com")
