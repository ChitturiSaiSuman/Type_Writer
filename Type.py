#!/usr/bin/env python3

import time
import subprocess

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Recorder:
    def __init__(self, width = 1920, height = 1080, frame_rate = 60, offset_x = 0, offset_y = 0, output_file = 'Output.mkv'):
        self.width = width
        self.height = height
        self.frame_rate = frame_rate
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.output_file = output_file

    def start(self):
        resolution = str(self.width) + 'x' + str(self.height)
        frame_rate = str(self.frame_rate)
        offset_x = str(self.offset_x)
        offset_y = str(self.offset_y)
        output_file = self.output_file

        self.proc = subprocess.Popen(['ffmpeg', '-video_size', resolution, '-framerate', frame_rate, '-f', 'x11grab', '-i', ':0.0', output_file])

    def stop(self):
        self.proc.kill()




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

    time.sleep(0.5)
    text_field.send_keys(Keys.ENTER)

    time.sleep(7.5)
    driver.close()



if __name__ == '__main__':

    recorder = Recorder(width = 1440, height = 810)
    recorder.start()

    message = input("Enter the text you want to type: ")

    # Type Speed in Characters per second
    type_speed = 30

    url = 'https://www.google.com/'
    xpath_to_text_field = '/html[1]/body[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[2]/div[2]/input[1]'

    start_typing(url, xpath_to_text_field, message, type_speed)
    recorder.stop()