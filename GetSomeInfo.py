import psutil
import os 
from retry import retry

import socket
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
from pyvirtualdisplay import Display
from selenium.common.exceptions import WebDriverException

import time

@retry(WebDriverException, tries=3, delay=0.3)
def click_element(element):
    if element.is_displayed():
        element.click()


def sport_IU():
    url = "https://sso.university.innopolis.ru/adfs/oauth2/authorize/?response_type=code&client_id=7d0eb0b9-ad73-4942-be55-284facc99a95&resource=7d0eb0b9-ad73-4942-be55-284facc99a95&redirect_uri=https%3A%2F%2Fsport.innopolis.university%2Foauth2%2Fcallback&state=cHJvZmlsZQ%3D%3D&scope=openid"
    
    browser = webdriver.Chrome()
    browser.get(url)
    
    login = browser.find_element(By.ID, "userNameInput").send_keys("s.ponomarev@innopolis.university")
    password = browser.find_element(By.ID, "passwordInput").send_keys("72882-green-inno")
    
    enter_button = browser.find_element(By.ID, "submitButton")
    click_element(enter_button)
    
    
    browser.quit

def sport_UI2():
    url = "https://sport.innopolis.university/profile/"

    data = {'key' : 'value'}
    response = requests.post(url, data=data)
    print(response.text)


def device_info():
    hostname = socket.gethostname()
    battery = psutil.sensors_battery()


    print(f"The hostname is: {hostname}")
    print(f"Battery Percentage: {battery.percent}%")
    print(f"Power Plugged: {battery.power_plugged}")

def main():
    flag = True
    commands = {
        "help": "will provide u the list of all commands",
        "device" : "will show the info about server",
        # "weather" : "will show u the weather in chosen town",
        "break" : "will finish the execution of program",
        "sport" : "will check in you to all sports in UI"
    }
    while (flag):
        command = str(input())
        
        if (command == "help"):
            for i in commands:
                output = i + " : " +  commands.get(i)
                print(output)
        elif (command == "weather"):
            # parse_weather()
            print("where is nothing to see(")
        elif (command == "device"):
            device_info()
        
        elif (command == "sport"):
            sport_UI2()
        elif (command == "close"):
            flag = False
        # else:
        #     print("None")
        
        print("\n")

if __name__ == "__main__":
    
    main()
