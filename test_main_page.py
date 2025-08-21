from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

    # для перехода на страницу логина  - добавляй после page.open()
    # login_page = page.go_to_login_page()
    # login_page.should_be_login_page()
    # или
    # так же
    # page.go_to_login_page()
    # login_page = LoginPage(browser, browser.current_url)
    # login_page.should_be_login_page()

# Файл test_main_page.py - тут мы выполняем сами тесты по префиксу "test_"  для PyTest. Т
# ут вызванные функции будут запускаться
