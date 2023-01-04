import requests

url = 'https://www.selenium.dev/images/sponsors/browserstack.png'
response = requests.get(url=url) #скачиваем файл через апи GET
content = response.content

# file = open('selenium_image.png', 'wb')
# file.write(content)
# file.close()
# file.write(b's')

with open('selenium_image.png', 'wb') as file: #открываем файл
    file.write(content)

import os
size = os.path.getsize('selenium_image.png')  #по пути определяет размер файла
assert size == 23783


