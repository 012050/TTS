
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import os
import time
a = 0


try:
    path1 = os.getcwd() + "\chromedriver.exe"
    chrome = webdriver.Chrome(path1)
    chrome.set_window_size(984, 700)
    chrome.set_window_position(2000,100)
    # chrome.minimize_window()

except:
    print("크롬드라이버의 버전을 확인해주세요.")

chrome.get("https://papago.naver.com/?sk=ko&tk=en")
chrome.implicitly_wait(60)
text_box = chrome.find_elements(By.CLASS_NAME, "edit_box___1KtZ3")
sound_bnt = chrome.find_elements(By.CLASS_NAME, "btn_sound___2H-0Z")

while True:
    a = input(": ")
    text_box[0].send_keys(Keys.CONTROL, "a", Keys.DELETE)
    if a == "":
        sound_bnt[0].click()
        continue
    chrome.implicitly_wait(60)
    text_box[0].send_keys(a, Keys.RETURN)
    time.sleep(1)
    sound_bnt[0].click()


    if a == "ㅁ" or a == "a" or a == "stop" or a == "exit" or a == "ㄴ" or a == "s":
        chrome.close()
        break




