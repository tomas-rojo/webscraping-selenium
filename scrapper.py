from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random_word
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
url = "https://ar.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck="


def search():
    available = ''
    print("\n"+"Buscando dominio...")
    app = random_word.random_word()
    driver.get(url + app + ".com")

    try:
        available = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/"
                                                 "div[1]")
        available = available.text
    except: pass

    if "no" in available:
        print(app + ".com", "no está disponible!""\n")
        search()
    else:
        print(app + ".com", "está disponible!""\n")
        print("----------MENU----------")
        print("1. Ir a GODADDY.COM para mas información")
        print("2. Seguir buscando")
        print("3. Salir")
        user_input = float(input("Ingrese una opción para continuar: "))
        if user_input == 1:
            new_driver = webdriver.Chrome()
            new_driver.get(url + app + ".com")
            time.sleep(10)
        elif user_input == 2:
            search()
        else:
            pass


search()
