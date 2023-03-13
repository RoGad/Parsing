import requests
from bs4 import BeautifulSoup

url = "https://auto.drom.ru/"  # URL сайта для парсинга

# Отправляем GET-запрос на сайт
padge = requests.get(url)

# Инициализируем объект BeautifulSoup и передаем ответ сервера в качестве параметра
soup = BeautifulSoup(padge.text, "html.parser")

# Ищем все элементы с классом "css-xb5nz8 e1huvdhj1" и записываем содержимое в список
block = soup.findAll('a', class_='css-xb5nz8 e1huvdhj1')

# Открываем файл для записи
with open("drom.txt", "w", encoding="utf-8") as f:
    # Записываем каждый элемент списка block в файл построчно
    for result in block:
        description = result.text.strip().replace('\xa0', '')
        f.write(description + "\n")