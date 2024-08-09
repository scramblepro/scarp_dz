import requests
from bs4 import BeautifulSoup

## Определяем список ключевых слов
KEYWORDS = ['дизайн', 'фото', 'web', 'python'] #,'ведут'] - тест тестович

## Ваш код
url = 'https://habr.com/ru/all/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('article')

# print(f"Найдено {len(articles)} статей.")

for article in articles:

    title_tag = article.find('h2', class_='tm-title')
    title = title_tag.text.strip() if title_tag else "Без заголовка"

    date_tag = article.find('time')
    date = date_tag.text.strip() if date_tag else "Без даты"

    link_tag = title_tag.find('a')
    link = 'https://habr.com' + link_tag['href'] if link_tag else "Без ссылки"

    if any(keyword.lower() in title.lower() for keyword in KEYWORDS):
        print(f"{date} – {title} – {link}")
