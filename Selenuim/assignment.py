77% of storage used … If you run out of space, you can't save to Drive or back up Google Photos.
﻿from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#1a.
driver = webdriver.Chrome(executable_path="C:\\Users\dgotl\Desktop\chromedriver.exe")
driver.get("http://www.walla.co.il")
#1b.
driver = webdriver.Chrome(executable_path="C:\\Users\dgotl\Desktop\geckodriver.exe")
driver.get("http://www.ynet.co.il")

#2
title = driver.title
driver.refresh()
if title==driver.title:
    print("equal")

#3 yes - elements are the same regardless to the browser

#4
driver.get("https://translate.google.com/")
driver.find_element_by_id("source").send_keys("חתול")
driver.find_element_by_id("gt-submit").click()

#5
driver.get("https://www.youtube.com/")
driver.find_element_by_id("search").send_keys("guns and roses")
driver.find_element_by_id("search-icon-legacy").click()

#6
a = driver.find_element_by_id("gt-submit")
b = driver.find_element_by_class_name("jfk-button")
c = driver.find_element_by_xpath("//input[@type=‘submit']")
print(a)

#7
driver.get("https://www.facebook.com/")
driver.find_element_by_id("email").send_keys("a@a.com")
driver.find_element_by_id("pass").send_keys("Aa123456")
