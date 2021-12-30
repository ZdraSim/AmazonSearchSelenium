from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time

driver: WebDriver = webdriver.Chrome(executable_path="C:\Program Files (x86)\selenium drivers/chromedriver.exe")

driver.get("https://www.amazon.com/Shopping/b?node=9408875011")

search = driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys("books")
driver.implicitly_wait(5)

btn = driver.find_element(By.ID, "nav-search-submit-button")
btn.click()

low = driver.find_element(By.ID, "low-price")
low.send_keys(15)

high = driver.find_element(By.ID, "high-price")
high.send_keys(100)

go = driver.find_element(By.CLASS_NAME, "a-button-input")
go.click()

sort = driver.find_element(By.ID, "a-autoid-0-announce")
sort.click()

lowtohigh = driver.find_element(By.ID, "s-result-sort-select_1")
lowtohigh.click()

time.sleep(5)
driver.quit()
