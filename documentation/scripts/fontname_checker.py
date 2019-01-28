from google import google
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

fontnames = ['Clendon', 'Rowan', 'Dobben', 'Catesby', 'Cantrip']
fnc_dict = {}

driver = webdriver.Firefox()

def checkGoogleResults(fontname):
    for n in fontname:
        url = 'https://www.google.co.in/#q=' + n
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        div1 = soup.find('div', {'id': "resultStats"})
        # print(div1.text)
        fnc_dict[n] = div1.text

# def checkExFontNames(fontname):

checkGoogleResults(fontnames)
driver.quit()
print(fnc_dict)