# 크롬 드라이버는 111.0.5563.64 버전을 사용했습니다.
# Selenium 예제 코드를 참고하였습니다. 감사합니다 :)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.147 Safari/537.36')]
urllib.request.install_opener(opener)

driver = webdriver.Chrome(options=options)
driver.get("https://www.google.co.kr/imghp?hl=ko&authuser=0&ogbl") # 크롬 드라이버로 괄호 안에 있는 URL을 실행합니다.
elem = driver.find_element(By.NAME, "q")
elem.send_keys("Pokemon") # Pokemon을 검색창에 입력함
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1.3 # 1.3초 마다 스크롤

# 스크롤 높이를 last_height 변수에 저장합니다.
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # 맨 아래로 스크롤 합니다.
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # 페이지가 로드 될때까지 기다립니다.
    time.sleep(SCROLL_PAUSE_TIME)
    # 새로운 스크롤 높이를 계산하고 마지막 스크롤 높이와 비교합니다.
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd")[0].click() # 제일 처음에 나오는 이미지부터 클릭합니다.
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    try:
        image.click()
        time.sleep(3)
        imgUrl = driver.find_element_by_css_selector(".r48jcc.pT0Scc.iPVvYb").get_attribute("src")
        print(imgUrl)
        print("카운트:", count)
        urllib.request.urlretrieve(imgUrl, "Images\\" + str(count) + ".jpg")
        count = count + 1
    except:
        pass

driver.close()