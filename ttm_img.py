from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import time
import os

PATH = '/usr/bin/chromedriver'
wd = webdriver.Chrome(executable_path=PATH)

img_url = 'http://grandanes.mx/_images/box/Gran-Danes-Cachorro-Mexico.jpg'

def get_images_from_google(webdriver, delay, max_images):
    def scroll(wd):
        wd.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(delay)
    url = 'https://www.google.com/search?q=cachorritos&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjRqcG63fPzAhVhlWoFHUPNAxQQ_AUoAXoECAEQAw&biw=1920&bih=973&dpr=1'
    wd.get(url)
    img_urls = set()
    skips = 0
    while len(img_urls) < max_images:
        scroll(wd)
        thumbnails = wd.find_elements(By.CLASS_NAME, 'Q4LuWd')
        for img in thumbnails[len(img_urls): max_images]: # [1:23] slicing
            try:
                img.click()
                time.sleep(delay)
            except: continue

        images = wd.find_elements(By.CLASS_NAME, 'n3VNCb')
        for image in images:
            if image.get_attribute('src') in img_urls:
                max_images += 1
                skips += 1
            if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                img_urls.add(image.get_attribute('src'))
                print(f'Found {len(img_urls)}')
    
    return img_urls

def download_image(download_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + file_name

        with open(file_path, 'wb') as f:
            image.save(f, 'JPEG')

        print('SUCCESS')
    except Exception as e:
        print('FAILED -', e)

directory = 'imgs'
parent_dir = '/home/bdsw3207/Code/Python/Selenium'
path_dir = os.path.join(parent_dir, directory)
os.mkdir(path_dir)

urls = get_images_from_google(wd, 1, 2)
for i, url in enumerate(urls):
    download_image('imgs/', url, str(i) + '.jpg')
wd.quit()
