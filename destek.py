import requests
from bs4 import BeautifulSoup

def googlefinance(birim):
    url = "https://www.google.com/finance/quote/"+str(birim)+"-TRY?hl=tr"

    try:
        page = requests.get(url)
        htmlPage = BeautifulSoup(page.content, "html.parser")
        actualduzenle = htmlPage.find("div", class_="YMlKec fxKbKc").getText()
        actualvalue = round(float(actualduzenle.replace(".", "").replace(",", ".")), 2)
    except Exception as e:
        print("An error occurred: ", e)
        return "error"
    return actualvalue


