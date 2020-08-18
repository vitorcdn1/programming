from selenium import webdriver
from selenium.webdriver.common.keys import Keys


path = "/home/vitor/Documents/github/python/python_learn/selenium/chromedriver"

driver = webdriver.Chrome(path)

driver.get("https://duckduckgo.com")

search = driver.find_element_by_name("q")
search.send_keys("vitor nascimento")
search.send_keys(Keys.RETURN)

result = driver.find_elements_by_class_name("result results_links_deep highlight_d result--url-above-snippet")


print(result.text)