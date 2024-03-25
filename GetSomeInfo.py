import psutil
import os 

import socket
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image



def parse_weather():
    print("Please enter the name of town")
    town = str(input())
    
    src = "https://yandex.ru/pogoda/" + town
    req = requests.get(src)
    # print(req.status_code)
    driver = webdriver.Chrome()
    driver.get(src)
    weather = driver.find_element(By.CLASS_NAME, "temp__value_with-unit")
    
    directory_path = os.path.dirname(__file__)
    # print(directory_path)
    driver.save_screenshot(os.path.join(directory_path, 'wether.png'))
    # driver.quit()
    
    image = Image.open(os.path.join(directory_path, 'weather.png'))
    image = image.crop((25, 140, 600, 440))
    image.show()
    print(weather.text)
    print(f"Source: {src}")
    

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
        "weather" : "will show u the weather in chosen town",
        "break" : "will finish the execution of program"
    }
    while (flag):
        command = str(input())

        if (command == "weather"):
            parse_weather()
        elif (command == "device"):
            device_info()
        elif (command == "help"):
            for i in commands:
                output = i + " : " +  commands.get(i)
                print(output)
            
        elif (command == "close"):
            flag = False
        # else:
        #     print("None")
        
        print("\n")

if __name__ == "__main__":
    
    main()
