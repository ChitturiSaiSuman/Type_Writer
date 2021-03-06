#!/usr/bin/env python3

import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def start_typing(url: str, xpath_to_text_field: str, message: str, type_speed: int) -> None:

    """
    Start typing a message in a given url.
    """
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    
    time.sleep(1)

    waiting_time = 1 / type_speed
    text_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_to_text_field))
    )

    for character in message:
        text_field.send_keys(character)
        time.sleep(waiting_time)

    time.sleep(2)
    text_field.send_keys(Keys.ENTER)

    time.sleep(2)
    driver.close()



if __name__ == '__main__':

    message = input("Enter the text you want to type: ")

    # Type Speed in Characters per second
    type_speed = 30

    url = 'https://www.google.com/'
    xpath_to_text_field = '/html[1]/body[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[2]/div[2]/input[1]'

    start_typing(url, xpath_to_text_field, message, type_speed)
