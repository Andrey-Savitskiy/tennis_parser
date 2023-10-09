# Парсеры информации о клубах и команде с сайта https://kcr.ttfr.ru/

Перед началом работы необходимо:
1. Установить пакеты за файла requirements.txt командой `pip install requirements.txt`
2. Узанать версию вашего Chrome браузера
3. Скачать chromedriver [с официального сайта](https://chromedriver.chromium.org/downloads) **ТАКОЙ ЖЕ ВЕРСИИ**, что и версия браузера
   (например, версия браузера 117.0.5938.150, значит драйвер тоже нужно взять 117 версии).
4. Распаковать скачаный архив с драйвером в папку проекта.
5. Запустив файл get_clubs.py можно собрать данные со страницы https://kcr.ttfr.ru/#/clubs
6. Запустив файл get_team.py можно собрать данные со страницы https://kcr.ttfr.ru/#/team/219/structure
