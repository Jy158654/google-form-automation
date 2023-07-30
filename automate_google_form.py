from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation'])
# option.add_argument("--headless")

# change to your path directory where chromedriver is stored
driver_path = r"C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe"

# change to your own google form url
google_form_path = "https://docs.google.com/forms/d/e/1FAIpQLSdAIpbK2b7IUFBPFIlGS5p6PtMfMScuGqzLMBJ8jmVR3y_sxA/viewform"

def automation(num_of_times):
    for i in range(num_of_times):

        service = Service(executable_path = driver_path)
        browser = webdriver.Chrome(options=option, service=service)

        browser.get(google_form_path)

        # change the following XPath according to your own google form
        q_num_1 = browser.find_elements(by=By.XPATH, value="//input[@type='text']")             #textbox
        q_num_2 = browser.find_element(by=By.XPATH, value="//div[@class='vd3tt']")              #button
        q_num_3 = browser.find_element(by=By.XPATH, value="//div[@class='uHMk6b fsHoPb']")      #checkbox
 
        
        submit_button = browser.find_element(by=By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")      #submit button
        
        q_num_1[0].send_keys("Lee Jun Yong")
        q_num_2.click()
        q_num_3.click()

        submit_button.click()

        browser.close()

if __name__ == "__main__":
    automation(1)