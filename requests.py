import requests

# API ключи
WEATHER_API_KEY = '5d8053838fa13b55729661bf6ea6d5d9'
NEWS_API_KEY = 'bcdee06c1cb948d09250e6de0c0a7e10'

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={'Tashkent'}&appid={'5d8053838fa13b55729661bf6ea6d5d9'}&units=metric'
    response = requests.get(url)
    data = response.json()
    if data['cod'] != 200:
        return "Город не найден."
    weather_desc = data['weather'][0]['description']
    temp = data['main']['temp']
    return f"Погода в {city}: {weather_desc}, температура: {temp}°C"

def get_news():
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={'bcdee06c1cb948d09250e6de0c0a7e10'}'
    response = requests.get(url)
    data = response.json()
    if data['status'] != 'ok':
        return "Ошибка при получении новостей."
    articles = data['articles'][:5]
    news_list = [f"{article['title']} - {article['source']['name']}" for article in articles]
    return "\n\n".join(news_list)
