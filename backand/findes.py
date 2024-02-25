import asyncio
import random
from bson import ObjectId
from selenium.webdriver.common.by import By 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from database import collection_name
class Logs():

    @staticmethod
    async def log(item_id):
        browser = None
        try:
            print("Test Execution Started")
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-ssl-errors=yes')
            options.add_argument('--ignore-certificate-errors')
            browser = webdriver.Remote(
            command_executor='http://172.17.0.3:4444/wd/hub',
            options=options
            )
            browser.maximize_window()
            browser.get("https://www.olx.ua/uk/")
            browser.implicitly_wait(20)
                #await asyncio.sleep(random.randrange(7, 10))

            block_one = browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]')
            block_one.click()
            await asyncio.sleep(random.randrange(3, 7))

            input_search = browser.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/div[2]/div/div/form/div/div[1]/div/div/div/div/div/input')
            input_search.clear()
            items_search_data = collection_name.find_one({"_id": ObjectId(item_id)})

            input_search.send_keys(items_search_data['model'])

            search_button = browser.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/div[2]/div/div/form/div/div[3]/button')
            search_button.click()

            await asyncio.sleep(4)

            min_price = browser.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/form/div[3]/div[1]/div/div[2]/div/div[1]/div/div/div/input')
            min_price.send_keys(items_search_data['price_hight'])
            max_price = browser.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/form/div[3]/div[1]/div/div[2]/div/div[2]/div/div/div/input')
            max_price.send_keys(items_search_data['price_low'])
            await asyncio.sleep(3)
                            #max_price.send_keys(Keys.ENTER)

            input_city = browser.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/form/div[1]/div[2]/div/div/div/div/div/input')
            input_city.send_keys(items_search_data['city'])
            search_button1 = browser.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/form/div[1]/div[3]/button')
            search_button1.send_keys(Keys.ENTER)

            await asyncio.sleep(20)

            iphone_elements = browser.find_elements(By.CLASS_NAME, "css-rc5s2u")
            title = browser.find_elements(By.CLASS_NAME, "css-16v5mdi")
            description = browser.find_elements(By.CSS_SELECTOR, "[data-testid='location-date']")
            price = browser.find_elements(By.CSS_SELECTOR, "[data-testid='ad-price']")

            iphone_list = []
            for element, titl, descrip, pri in zip(iphone_elements, title, description, price):
                href = element.get_attribute("href")
                name_url = titl.text
                meet_url = descrip.text
                price_url = pri.text
                iphone_list.append({"url": href, "name_url": name_url, "price_url": price_url, "meet_url": meet_url, 'items_search_id': items_search_data['model']})
        
            return iphone_list
        finally:
            browser.quit()




    @staticmethod
    async def run():
        await asyncio.wait([Logs.log()])  # Use asyncio.gather for gathering multiple coroutines


#if __name__ == "__main__":
#    loop = asyncio.get_event_loop()
#    result = loop.run_until_complete(Logs.run())




    #teake from database method get()
    #base from id 
    # take price and model
    # after make analiz metrick!!!!!
