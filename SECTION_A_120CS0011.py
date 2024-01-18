from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SeleniumProjectTest:
    def __init__(self):
        
        self.driver = webdriver.Chrome()


    def launch_browser(self):
        self.driver.get("https://www.makemytrip.com/railways/")
        
        # Print the URL and Title of the Page
        title = self.driver.title
        print("Title of the page is:", title)
        url = self.driver.current_url
        print("URL of the page is:", url)
        self.driver.maximize_window()

        # Selecting Source
        self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div/div/div[2]/div/div[1]/label/span").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div/div/div/input").send_keys("Delhi")
        time.sleep(2)
        

        # Selecting the source from the suggestion list
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div/div/div/div/div/ul/li[1]/div").click()
       

        # Selecting Destination
        self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div/div/div[2]/div/div[2]/label/span").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/input").send_keys("Lucknow")
        time.sleep(2)

        # Selecting the destination from the suggestion list
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div/ul/li[1]/div").click()
       

        # Selecting Date
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div/div/div[2]/div/div[3]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div/div/div/div[2]/div/div[1]/span[2]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div/div/div/div[2]/div/div[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div/div/div/div[2]/div/div[1]/span[2]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div[3]/div[3]/div[6]").click()

        # Selecting Class
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div/div/div[2]/div/div[4]").click()
        time.sleep(1)
        class_list = self.driver.find_elements(By.CSS_SELECTOR, "ul.travelForPopup > li")
        for element in class_list:
            if element.text == "Third AC":
                element.click()
                break

        # Clicking Search button
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div/div/div[2]/p/a").click()
        time.sleep(2)
        self.driver.close()

if __name__ == "__main__":
    obj = SeleniumProjectTest()
    obj.launch_browser()
