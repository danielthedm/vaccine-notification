import requests
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


path = "C:\\Users\\Dan\\Downloads\\chromedriver\\chromedriver.exe"
driver = webdriver.Chrome(path)

while(True):
    resp = requests.get('https://www.walmart.com/pharmacy/v2/storefinder/stores/138f0920-7aa0-431f-b073-d9ee377c3068?searchString=23113&serviceType=covid_immunizations&filterDistance=100')
    print(resp)
    if resp.status_code != 200:
        print('got 400')
    else:
        r = requests.post('https://notify.run/c3bqfzlkGfLrjHww', data='VACCINE GET THE FUCK ONLINE - WALMART 23113')

    item = resp.json()
    if(item['message'] == 'No stores available for this location. Please try another location'):
        print('Vaccine not available')
    else:
        print('VACCINE TIME')
        r = requests.post('https://notify.run/c3bqfzlkGfLrjHww', data='VACCINE GET THE FUCK ONLINE - WALMART 23113')




    resp = requests.get('https://www.walmart.com/pharmacy/v2/storefinder/stores/138f0920-7aa0-431f-b073-d9ee377c3068?searchString=20124&serviceType=covid_immunizations&filterDistance=100')
    print(resp)
    if resp.status_code != 200:
        print('got 400')
    else:
        r = requests.post('https://notify.run/c3bqfzlkGfLrjHww', data='VACCINE GET THE FUCK ONLINE - WALMART 20124')

    item = resp.json()
    if(item['message'] == 'No stores available for this location. Please try another location'):
        print('Vaccine not available')
    else:
        print('VACCINE TIME')
        r = requests.post('https://notify.run/c3bqfzlkGfLrjHww', data='VACCINE GET THE FUCK ONLINE - WALMART 20124')

    driver.get("https://www.cvs.com/immunizations/covid-19-vaccine")
    time.sleep(5)
    select = Select(driver.find_element_by_id('ddlStates'))
    select.select_by_visible_text('Virginia')
    time.sleep(10)
    button = driver.find_element_by_css_selector('#Submit')
    button.click()
    time.sleep(10)
    if("The COVID-19 vaccine is not yet available at CVS Pharmacy in Virginia." in driver.page_source):
        print("No vaccine")
    else:
        r = requests.post('https://notify.run/c3bqfzlkGfLrjHww', data='VACCINE GET THE FUCK ONLINE - CVS')
        print('VACCINE GET THE FUCK ONLINE - CVS')
    driver.close()

    time.sleep(60)