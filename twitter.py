from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME=   # YOUR EMAIL ADDRESS
PASSWORD =  # YOUR PASSWORD
MOBILE =    # YOUR MOBILE PHONE 

def tweet_func(text):
    driver = webdriver.Firefox(executable_path='geckodriver.exe')
    driver.get("https://twitter.com/home")
    driver.maximize_window()
    try:
        username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[contains(@autocomplete, 'username')]"))
    )
        username.click()
        username.send_keys(USERNAME)
        username.send_keys(Keys.ENTER)

    except Exception as e:
        print(e)

    try:
        phone = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[contains(@autocomplete, 'on')]"))
    )
        phone.click()
        phone.send_keys(MOBILE)
        phone.send_keys(Keys.ENTER)
    except Exception as e:
        print(e)

    try:
        passw = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[contains(@autocomplete,  'current-password')]"))
        )

        passw.click()
        passw.send_keys(PASSWORD)
        passw.send_keys(Keys.ENTER)
    except Exception as e:
        print(e)

    try:
        field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='notranslate public-DraftEditor-content']"))
    )    
        field.click()
        field.send_keys(text)
        tweet = driver.find_elements(By.XPATH, "//span[contains(text(), 'Twitt')]/../..")[1]
        tweet.click()
    except Exception as e:
        print(e)
    
    finally:
        time.sleep(5)
        driver.quit()


if __name__="__main__":
    tweet_func("Hello!!!! Wooorld!!!")