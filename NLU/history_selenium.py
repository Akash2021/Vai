from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import json
import os
<<<<<<< HEAD
from trainh import train
=======
>>>>>>> 12646d03f6d29b7dd7da8708a3ece5313ca24eb6
cwd = os.getcwd()
path = cwd+"/chromedriver"
driver = webdriver.Chrome(path)
driver.get(
    "https://accounts.google.com/o/oauth2/v2/auth/identifier?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow"
)
<<<<<<< HEAD
def history():
	try:
	    # link = WebDriverWait(driver, 10).until(
	    #     EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
	    # link.click()
	    email = WebDriverWait(driver, 10).until(
	        EC.element_to_be_clickable(
	            (By.CSS_SELECTOR, "input[name='identifier']")))
	    email.send_keys("akash.singh7337@gmail.com")
	    next = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.CLASS_NAME, "VfPpkd-RLmnJb")))
	    next.click()
	    time.sleep(2)
	    password = WebDriverWait(driver, 10).until(
	        EC.element_to_be_clickable(
	            (By.CSS_SELECTOR, "input[name='password']")))
	    password.send_keys("Testing!098")

	    next = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.CLASS_NAME, "VfPpkd-RLmnJb")))
	    next.click()
	    time.sleep(2)
	    driver.get("https://myactivity.google.com/myactivity?pli=1&product=19")
	    # time.sleep(1)
	    # filter = WebDriverWait(driver, 10).until(
	    #     EC.presence_of_element_located((By.CLASS_NAME, "VfPpkd-RLmnJb")))
	    # filter.click()
	    time.sleep(1)
	    # texts = [el.text for el in driver.find_elements_by_class_name("QTGV3c")]
	    # print(texts)
	    elements = driver.find_elements_by_css_selector("div.QTGV3c a")
	    s = "https://www.google.com/search"
	    parity = int(0)
	    global x, y
	    history = {}
	    for element in elements:
	        val = (element.get_attribute("href"))
	        x = (element.text)
	        if re.search(s, val):
	            if parity % 2 == 1:
	                history[x] = y
	                parity += 1
	        else:
	            if parity % 2 == 0:
	                y = val
	                parity += 1
	    with open('data.json', 'w') as fp:
	        json.dump(history, fp, indent=4)
	    driver.close()
	    train()

	except:
	    driver.close()
if __name__ == '__main__':
    history()
=======
try:
    # link = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
    # link.click()
    email = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input[name='identifier']")))
    email.send_keys("akash.singh7337@gmail.com")
    next = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "VfPpkd-RLmnJb")))
    next.click()
    time.sleep(2)
    password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input[name='password']")))
    password.send_keys("Testing!098")

    next = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "VfPpkd-RLmnJb")))
    next.click()
    time.sleep(2)
    driver.get("https://myactivity.google.com/myactivity?pli=1&product=19")
    # time.sleep(1)
    # filter = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, "VfPpkd-RLmnJb")))
    # filter.click()
    time.sleep(1)
    # texts = [el.text for el in driver.find_elements_by_class_name("QTGV3c")]
    # print(texts)
    elements = driver.find_elements_by_css_selector("div.QTGV3c a")
    s = "https://www.google.com/search"
    parity = int(0)
    global x, y
    history = {}
    for element in elements:
        val = (element.get_attribute("href"))
        x = (element.text)
        if re.search(s, val):
            if parity % 2 == 1:
                history[x] = y
                parity += 1
        else:
            if parity % 2 == 0:
                y = val
                parity += 1
    with open('data.json', 'w') as fp:
        json.dump(history, fp, indent=4)
    driver.close()

except:
    driver.close()
>>>>>>> 12646d03f6d29b7dd7da8708a3ece5313ca24eb6
