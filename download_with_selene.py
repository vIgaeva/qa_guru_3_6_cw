import time

import selene
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
prefs = {
    'download.default_directory': '/Users/User/PycharmProjects/qa_guru_3_8_cw/tmp', #словарь с настройками
    'download.prompt_for_download': False #чтобы не спhрашивало подтверждение
}

options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.config.driver = driver

# открывваем браузер и кликаем на кнопку скаччивание, чтобы браузер успел скачать ставим таймер
browser.open('https://demoqa.com/upload-download')
browser.element('#downloadButton').click()
time.sleep(1)