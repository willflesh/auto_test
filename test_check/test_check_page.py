from ..letter.test_pages import CheckPages


def test_checkboxes(browser):
    link = 'https://the-internet.herokuapp.com/checkboxes'
    letter = CheckPages(browser, link)
    letter.open()
    letter.go_to_checkbox()
