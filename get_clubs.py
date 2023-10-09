from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def main():
    # Установка пути до Chrome WebDriver
    webdriver_service = Service('chromedriver.exe')

    # Настройка параметров Chrome WebDriver
    options = Options()
    options.add_argument('--headless')  # Запуск в фоновом режиме, без открытия окна браузера

    # Инициализация Chrome WebDriver
    driver = webdriver.Chrome(service=webdriver_service, options=options)

    # Переход на страницу с данными
    driver.get('https://kcr.ttfr.ru/#/clubs')

    # Ждем, пока элементы будут загружены
    driver.implicitly_wait(10)

    # Находим таблицу с данными
    table = driver.find_element(By.CLASS_NAME, 'dNone-tablet')

    # Получаем все строки таблицы
    rows = table.find_elements(By.TAG_NAME, 'a')

    # Проходимся по каждой строке и получаем данные
    for row in rows:
        # Получаем данные
        link = row.get_attribute('href')
        row_container = row.find_element(By.CLASS_NAME, 'b-statistics__container')
        name = row_container.find_element(By.CLASS_NAME, 'textOswald-1.mb2').text
        town = row_container.find_element(By.CLASS_NAME, 'textXs.transparent.textUppercase.mr4').text
        coach = row_container.find_element(By.CLASS_NAME, 'textMd.transparent').text
        sum_rating = row_container.find_element(By.CLASS_NAME, 'b-statistics__rating').text

        with open('clubs_output.txt', 'a', encoding='utf-8') as file:
            file.write(';'.join([link, name, town, coach, sum_rating]) + '\n')

    # Закрываем браузер
    driver.quit()


if __name__ == '__main__':
    main()
