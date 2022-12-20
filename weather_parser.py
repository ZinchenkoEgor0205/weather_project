import requests
from bs4 import BeautifulSoup


class WeatherBase:

    def yandex_weather_parser(self):
        yandex_url = 'https://yandex.by/pogoda/details/10-day-weather'
        response = requests.get(yandex_url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('span', class_='a11y-hidden')
        yandex_weather_report = {}
        days = []
        for quote in quotes:
            if quote.text.split(',')[0] in ['сегодня', 'завтра', 'понедельник', 'вторник', 'среда', 'четверг',
                                            'пятница', 'суббота', 'воскресенье']:
                day = quote.text.split(',')[0]
                days.append(day)
            elif quote.text.split(',')[0] in ['днём', ]:
                yandex_weather_report[day] = quote.text.split(',')[1]
        return yandex_weather_report, days

    def yandex_weather_data_cleaner(self, raw_data):
        cleaned_data = {}
        for key, value in raw_data.items():
            value_split = value.split(' ')
            if len(value_split) > 2:
                value_new = (int(value_split[-3]) + int(value_split[-1][:-1])) // 2
            else:
                value_new = int(value_split[-1])
            cleaned_data[key] = value_new
        return cleaned_data

    def mailru_weather_parser(self, days):
        mailru_url = 'https://pogoda.mail.ru'
        response = requests.get(mailru_url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('div', class_='information__content__temperature')
        mailru_weather_report_cleaned = {days[0]: int(quotes[0].text.strip()[:-1])}
        quotes = soup.find_all('div', class_='day__temperature')
        for i in range(len(days) - 1):
            mailru_weather_report_cleaned[days[i + 1]] = int(quotes[i].text.split()[0][:-1])
        return mailru_weather_report_cleaned

    def weather_mediator(self, days, yandex_weather_report_cleaned, mailru_weather_report_cleaned):
        medium_weather = {}
        for day in days:
            medium_weather[day] = (yandex_weather_report_cleaned[day] + mailru_weather_report_cleaned[day]) // 2
        return medium_weather
