from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    pass

# main_page.py - тут мы храним методы по конкретной странице,
# завернутые в класс этой странице. Класс этот - условный MainPage -
# наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py
