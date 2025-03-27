from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup


def selenium():

    service = Service(executable_path="C:\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    time.sleep(2)
    driver.get("https://www.zooplus.fr/")
    time.sleep(2)
    button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    button.click()
    time.sleep(2)
    search_box = driver.find_element(By.XPATH, '//*[@id="search_query_field_mobile"]')
    search_box.send_keys("paté pour chat")
    search_box.submit()
    time.sleep(2)


    button_chat = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/main/div[1]/div/div/ul/li[1]/span/label')
    button_chat.click()
    time.sleep(2)

    button_prixdecroiss = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/main/div[2]/div/div/div[2]/select/option[4]')
    button_prixdecroiss.click()
    time.sleep(2)
    
    button_add_one = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/main/div[6]/div[1]/div/div/div[3]/div[2]/div/div[1]/form/div[1]/div/button[2]')
    button_add_one.click()
    time.sleep(2)
    button_add_one.click()
    time.sleep(2)

    panier = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/main/div[6]/div[1]/div/div/div[3]/div[2]/div/div[1]/form/div[2]/button')
    panier.click()
    time.sleep(3)

    go_to_panier = driver.find_element(By.XPATH,'//*[@id="header-cart-nav-anchor"]')
    go_to_panier.click()
    time.sleep(10)

def scrap_to_page():

    url = "https://developer.mozilla.org/fr/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    visited_links = set()

    for a in soup.find_all('a', href=True):
        link = a['href']
        if link.startswith("/"):
            link = "https://developer.mozilla.org" + link

        if link.startswith("https://developer.mozilla.org/fr/") and link not in visited_links:
            visited_links.add(link)
            sub_response = requests.get(link)
            sub_soup = BeautifulSoup(sub_response.text, "html.parser")
            print(sub_soup.title.text.strip())

