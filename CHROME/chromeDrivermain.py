from selenium import webdriver
from selenium.webdriver.common.by import by
import time


url = "https://www.instagram.com/"
driver = webdriver.Chrome(executable_path="C://Users//user//PycharmProjects//SELENIUM//CHROME//chromeDrivermain.py")


try:
    driver.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()



