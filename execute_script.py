from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support.select import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)



    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)


    robot = browser.find_element(By.ID, "robotCheckbox")
    robot.click()

    radiobutton = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    button = browser.find_element(By.CLASS_NAME, "btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()