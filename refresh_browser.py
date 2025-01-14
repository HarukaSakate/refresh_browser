import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

url = "https://example.com"  # ここに更新したいページのURLを指定
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get(url)

try:
    # 5分ごとにページをリロードするループ
    while True:
        time.sleep(300) #ここでリロード間隔を設定 
        driver.refresh()  
        print("Page reloaded")
except KeyboardInterrupt:
    print("Exit script")
finally:
    driver.quit()
