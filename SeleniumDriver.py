from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


def getDriver():
    options = Options()
    options.add_argument("--window-size=1920,1200")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')

    DRIVER_PATH = '/Users/vatsal/Documents/github-personal/rottentomatoes/chromedriver'
    s = Service(DRIVER_PATH)

    driver = webdriver.Chrome(options=options, service=s)
    return driver
