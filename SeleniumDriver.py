from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import os



def getDriver():
    options = Options()
    options.add_argument("--window-size=1920,1200")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')

    DRIVER_PATH = os.path.join(os.getcwd(), 'chromedriver')
    s = Service(DRIVER_PATH)

    driver = webdriver.Chrome(options=options, service=s)
    return driver
