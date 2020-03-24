import urllib.request

from lxml import etree
#
response = urllib.request.urlopen("https://kyfw.12306.cn/otn/login/init")
page_source = response.read().decode('utf-8')
selector = etree.HTML(page_source)
print(page_source)
url = selector.xpath('//*[@id="loginForm"]/ul[2]/li[4]/div/div')
# print(url)
import os
from selenium import webdriver
# import time
# from PIL import Image
# from YDMHTTP import identify
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# chromedriver = "D:\Anaconda3\chromedriver.exe"
# os.environ["webdriver.chrome.driver"] = chromedriver
# driver = webdriver.Chrome(chromedriver)

#不启动浏览器，提高效率
#chrome_options = Options()
#chrome_options.add_argument("--headless")       # define headless
#driver = webdriver.Chrome(chrome_options=chrome_options)

#driver.maximize_window()  最大化窗口

# driver.get("http://kyfw.12306.cn/otn/login/init")
#
# if "登录" in driver.title:
#     username = driver.find_element_by_id("username")
#     password = driver.find_element_by_id("password")
#     username.send_keys("xwdlyx@qq.com")
#     password.send_keys("dkd231320")
#
#     time.sleep(5)
#     driver.save_screenshot("login.png")
#     loginSub = driver.find_element_by_id("loginSub")
#     img = driver.find_element_by_xpath('//*[@id="loginForm"]/div/ul[2]/li[4]/div/div')
#     #//*[@id="loginForm"]/div/ul[2]/li[4]/div/div/div[3]/img
#     x = int(img.location["x"]) + 60
#     y = int(img.location["y"]) + 50
#     im = Image.open("login.png")
#     im.crop((x,y,x + 415,y + 256)).save("vcode.png")
#     count = 0
#     while True:
#         cid, numbers = identify("vcode.png")
#         if count > 3:
#             break
#         if numbers.isdigit():
#             break
#         if numbers == "看不清" or numbers.isdigit() == False:
#             count = count + 1
#             continue
#         else:
#             break
#
#     if numbers.isdigit():
#         code_xy = [[60, 80], [120, 80], [180, 80], [270, 80], [60, 150], [120, 150], [180, 150], [270, 150]]
#         arr = list(numbers)
#         for number in arr:
#             index = int(number) - 1
#             xy = code_xy[index]
#             offset_x = xy[0]
#             offset_y = xy[1]
#             ActionChains(driver).move_to_element_with_offset(img, offset_x, offset_y).click().perform()
#
#         loginSub = driver.find_element_by_id("loginSub")
#         loginSub.click()
#         time.sleep(2)
#         driver.get("http://kyfw.12306.cn/otn/leftTicket/init")
#         time.sleep(2)
#
#         fromStationText = driver.find_element_by_id("fromStationText")
#         fromStationText.click()
#         fromStationText.send_keys("武汉")
#         fromStationText.send_keys(Keys.ENTER)
#         time.sleep(1)
#
#         toStationText = driver.find_element_by_id("toStationText")
#         toStationText.click()
#         toStationText.send_keys("苏州")
#         toStationText.send_keys(Keys.ENTER)
#         time.sleep(1)
#
#         train_date = driver.find_element_by_id("train_date")
#         train_date.click()
#         datediv = driver.find_element_by_xpath("/html/body/div[30]/div[1]/div[2]")
#         ActionChains(driver).move_to_element_with_offset(datediv,238,79).click().perform()
#
#
#         time.sleep(1)
#         query_ticket = driver.find_element_by_id("query_ticket")
#         query_ticket.click()
#
#         driver.save_screenshot("index.png")