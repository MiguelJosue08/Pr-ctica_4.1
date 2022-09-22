
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time



driver=webdriver.Chrome("/Users/dev/Practicas/chromedriver")
action=ActionChains(driver)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

print("Test starts")


box1=driver.find_element_by_xpath("//*[@id='box1']")
CountryBox1=driver.find_element_by_xpath("//*[@id='box101']")
action.drag_and_drop(box1,CountryBox1).perform()

box2=driver.find_element_by_xpath("//*[@id='box2']")
CountryBox2=driver.find_element_by_xpath("//*[@id='box102']")
action.drag_and_drop(box2,CountryBox2).perform()

box3=driver.find_element_by_xpath("//*[@id='box3']")
CountryBox2=driver.find_element_by_xpath("//*[@id='box103']")
action.drag_and_drop(box3,CountryBox2).perform()

box4=driver.find_element_by_xpath("//*[@id='box4']")
CountryBox4=driver.find_element_by_xpath("//*[@id='box104']")
action.drag_and_drop(box4,CountryBox4).perform()

box5=driver.find_element_by_xpath("//*[@id='box5']")
CountryBox5=driver.find_element_by_xpath("//*[@id='box105']")
action.drag_and_drop(box5,CountryBox5).perform()

box6=driver.find_element_by_xpath("//*[@id='box6']")
CountryBox6=driver.find_element_by_xpath("//*[@id='box106']")
action.drag_and_drop(box6,CountryBox6).perform()

box7=driver.find_element_by_xpath("//*[@id='box7']")
CountryBox7=driver.find_element_by_xpath("//*[@id='box107']")
action.drag_and_drop(box7,CountryBox7).perform()

print("finish")






