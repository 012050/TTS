
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

link1 = "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea"
link2 = "VfPpkd-Bz112c-LgbsSe VfPpkd-Bz112c-LgbsSe-OWXEXe-e5LLRc-SxQuSe fzRBVc tmJved SSgGrd m0Qfkd"
link3 = "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/div[4]/div[2]/div/div[2]/div/span/button/div[3]"
link3 = "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/div[4]/div[2]/div/div[2]/div/span/button"

try:
    site = input("select google or naver\n\n")
    a = 1
    path1 = os.getcwd() + "\chromedriver.exe"
    
    chrome = webdriver.Chrome(path1)
    if site == "naver" or site == "네이버" or site == "n" or site == "ㄴ" or site == "n" or site == "ㅜ":
        chrome.get("https://papago.naver.com/?sk=ko&tk=en")
        chrome.implicitly_wait(15)
        word = chrome.find_element_by_id("txtSource")
        print("\n\n standby")
        while a == 1:
            t = input("입력하세요.\n")
            word.send_keys(Keys.CONTROL, "a")
            word.send_keys(Keys.BACKSPACE)
            if t == "stop":
                a = 0
                break
            word.send_keys(t)
            sound = chrome.find_elements_by_class_name("btn_sound___2H-0Z")
            sound[0].click()
            
    if site == "google"  or site == "구글" or site == "g" or site == "ㅎ":
        chrome.get("https://translate.google.com/?sl=ko&tl=ko&op=translate")
        chrome.implicitly_wait(15)
        word = chrome.find_element_by_xpath(link1)
        print("\n\nread\n")
        while a == 1:
            t = input("\n")
            word.send_keys(Keys.CONTROL, "a")
            word.send_keys(Keys.BACKSPACE)
            if t == "stop":
                a = 0
                break
            word.send_keys(t)
            chrome.implicitly_wait(5)
            sound = chrome.find_element_by_xpath(link3)
            sound.click()

    if site == "t" or site == "ㅅ":
        chrome.get("https://translate.google.com/?sl=ko&tl=ko&op=translate")
        chrome.implicitly_wait(15)
        print("\n\nread\n")
        while a == 1:
            t = input("\n")
            chrome.get("https://translate.google.com/?sl=auto&tl=ko&text=" + t +"&op=translate")
            chrome.implicitly_wait(15)
            if t == "stop" or t == "멈춤" or t == "정지":
                a = 0
                break
            sound = chrome.find_element_by_xpath(link3)
            sound.click()

except KeyboardInterrupt:
    chrome.close()