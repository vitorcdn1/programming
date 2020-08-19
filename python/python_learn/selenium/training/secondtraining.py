from selenium import webdriver

path = "/opt/chromedriver"
driver = webdriver.Chrome(path)

driver.get("https://translate.google.com")


