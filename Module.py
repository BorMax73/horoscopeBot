import config
from bs4 import BeautifulSoup
import requests
import re


class Parser:
    link = config.link  # baseLink
    signs = [
        'aries',
        'taurus',
        'gemini',
        'cancer',
        'leo',
        'virgo',
        'libra',
        'scorpio',
        'sagittarius'
        'capricorn',
        'Aquarius',
        'pisces',
        'null'

    ]

    def __Signs(self, sign):  # private parse method
        r = requests.get(f"{self.link}{sign}/today.html")  # request to page
        if r.status_code == 200:  # check
            soup = BeautifulSoup(r.text, 'html.parser')
            result = re.sub(r'\s+', ' ', soup.find("p", {"class": ""}).text)  # find Element
            return f"Ваш гороскоп на сегодня:\n{result}"  # base form of horoscope
        else:
            print('error')

    def ParseHoroscope(self, num):
        result = self.__Signs(self.signs[num])
        return result
