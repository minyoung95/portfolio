# import os
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup

# # 브라우저 인스턴스를 전역으로 관리
# browser = None  # 브라우저 인스턴스를 전역 변수로 설정

# def get_browser_instance():
#     """
#     단일 Chrome 브라우저 인스턴스를 반환합니다.
#     이미 브라우저가 실행 중이면 기존 브라우저를 반환하고,
#     실행 중이지 않다면 새 브라우저 인스턴스를 생성합니다.
#     """
#     global browser
#     if browser is None:
#         print("새로운 브라우저 인스턴스를 생성합니다...")
#         options = webdriver.ChromeOptions()
#         options.add_argument("--disable-dev-shm-usage")
#         options.add_argument("--window-size=1920x1080")
#         # options.add_argument("--headless")  # 필요에 따라 주석 해제
#         options.add_argument("--disable-blink-features=AutomationControlled")
#         browser = webdriver.Chrome(options=options)
#     else:
#         print("기존 브라우저 인스턴스를 재사용합니다...")
#     return browser

# def scrape_hotel_data(city_name, check_in, check_out, rooms, adults, children):
#     """
#     특정 도시의 호텔 데이터를 스크래핑하는 함수입니다.
#     """
#     chrome_options = Options()
#     chrome_options.add_argument("--disable-dev-shm-usage")  
#     chrome_options.add_argument("--window-size=1920x1080")  

#     url = f"https://www.agoda.com/ko-kr/search?city={city_name}&checkIn={check_in}&los=2&rooms={rooms}&adults={adults}&children={children}&checkOut={check_out}"
#     browser = webdriver.Chrome(options=chrome_options)
#     browser.get(url)

#     WebDriverWait(browser, 20).until(lambda x: x.find_element(By.ID, 'searchPageRightColumn'))

#     prev_height = browser.execute_script("return document.body.scrollHeight")
#     time.sleep(3)
#     while True:
#         browser.execute_script("""
#         window.scrollTo({
#             top: document.body.scrollHeight - 300,
#             behavior: 'smooth'
#         });
#         """)
#         time.sleep(5)
#         curr_height = browser.execute_script("return document.body.scrollHeight")
#         if prev_height == curr_height:
#             print(f"추가 콘텐츠 없음. 스크롤 중지. 최종 높이: {curr_height}px")
#             break
#         prev_height = curr_height

#     soup = BeautifulSoup(browser.page_source, 'lxml')
#     browser.quit()

#     data = soup.select_one("div#searchPageRightColumn")
#     items = data.select("li.PropertyCard.PropertyCardItem")
    
#     hotel_data = []
    
#     for idx, item in enumerate(items):
#         try:
#             # name = item.select_one("h3.sc-jrAGrp.sc-kEjbxe.eDlaBj.dscgss").text.strip()
#             # cost = item.select_one("ul > li:nth-child(3) > div > div > div > span.PropertyCardPrice__Value").text.strip().replace(",", "")
#             # # cost = item.select_one("ul > li:nth-child(3) > div > div > div > div > span").find_next_sibling().text.strip()
#             # hlink_element = item.select_one("button.ab069-box img")
#             # # hlink_element = item.select_one("button.ab069-box.ab069-bg-base-transparent.ab069-fill-inherit.ab069-text-inherit.ab069-w-full.ab069-cursor-pointer > img")
#             # hlink = hlink_element['src']
            
#             # hd = item.select_one("li:nth-child(1) > div > div > a")
#             # hdirect = hd['src']

#             name = item.select_one("h3.sc-jrAGrp.sc-kEjbxe.eDlaBj.dscgss").text.strip()
#             cost = int(item.select_one("ul > li:nth-child(3) > div > div > div > span.PropertyCardPrice__Value")
#                         .text.strip().replace(",", ""))
#             hlink_element = item.select_one("button.ab069-box img")
#             hlink = hlink_element['src']
#             # href = hlink['src'] if hlink else "https://i.pinimg.com/736x/d0/14/73/d01473fbb3094de59b2402ea88672ef2.jpg"

#             # print("----------------")
#             # print(name)
#             # print(cost)
#             # print(hlink)
#             # print(hlink)
#             # print("----------------")


#             if not all([name, cost, hlink]):
#                 continue
            
#             hotel_data.append({'name': name, 'cost': cost, 'hlink': hlink, 'hdirect': hlink})
            
#         except Exception as e:
#             print(f"정보 추출 실패: {e}")
#             continue

#     return hotel_data