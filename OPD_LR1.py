from bs4 import BeautifulSoup
import requests
import pandas  # Также был установлен модуль openpyxl


def parsing():
    url = "https://www.chitai-gorod.ru/novelty"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    data = soup.findAll("article", class_="product-card product-card product")
    return data


def get_titles_list(data):
    titles_list = list()
    for datum in data:
        title = (datum.find("div", class_="product-title__head")).text.strip()
        titles_list.append(title)
    return titles_list


def get_authors_list(data):
    authors_list = list()
    for datum in data:
        author = (datum.find("div", class_="product-title__author")).text.strip()
        authors_list.append(author)
    return authors_list


def get_prices_list(data):
    prices_list = list()
    for datum in data:
        price = (datum.find("div", class_="product-price__value")).text.strip()
        prices_list.append(price)
    return prices_list


def excel_output(titles_list, authors_list, prices_list):
    database = pandas.DataFrame({"Название": titles_list, "Автор": authors_list, "Цена": prices_list})
    database.to_excel("LR1.xlsx", sheet_name="Перечень книг", index=False)


def main():
    data = parsing()
    titles_list = get_titles_list(data)
    authors_list = get_authors_list(data)
    prices_list = get_prices_list(data)
    excel_output(titles_list, authors_list, prices_list)


if __name__ == "__main__":
    main()
