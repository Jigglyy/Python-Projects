from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time



class SauceDemo():
    def __init__(self, username, password):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.username = username
        self.password = password
        self.driver.get("https://www.saucedemo.com")
        self.driver.set_page_load_timeout(30)
        
    def login(self):
        login_user = self.driver.find_element(By.ID, "user-name")
        login_password = self.driver.find_element(By.ID, "password")

        login_user.click()
        login_user.send_keys(self.username)
        login_password.click()
        login_password.send_keys(self.password)

        login = self.driver.find_element(By.ID, "login-button")
        login.click()
        
        
    def addToCart(self):
        time.sleep(1)
        items = self.driver.find_elements(By.CSS_SELECTOR, ".btn_primary")
        for i in items:
            i.click()
        cart = self.driver.find_element(By.ID, "shopping_cart_container")
        cart.click()
        
        
    def getInformation(self):
        items_list = {}
        items_name = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        items_price = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")

        for name in items_name:
            for price in items_price:
                items_list[name.text] = price.text
                items_price.remove(price)
                break
        
        #a = dict(zip(items_list.values(), sorted(items_list.keys(), key=lambda x: float(x[1:]), reverse=True))) 
        #a = dict(zip(items_list.values(), sorted(items_list.keys(), key=lambda x: float(x[1:]), reverse=True)))
        #a = dict(zip(items_list.keys(), sorted(items_list.values(), key=lambda x: float(x[1:]), reverse=True)))
        a = dict( sorted(items_list.items(), key=lambda x: float(x[1][1:]), reverse=True))
        
        print(a)
        
    def closeDriver(self):
        self.driver.quit()
        return print("Finished")

    
bot = SauceDemo("standard_user", "secret_sauce")
bot.login()
bot.addToCart()
bot.getInformation()
bot.closeDriver()