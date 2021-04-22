from selenium.webdriver import Firefox
from time import sleep

url = 'http://selenium.dunossauro.live/aula_05_c.html'

firefox = Firefox()

firefox.get(url)


def melhor_filme(browser, filme, email, telefone):
    sleep(1)
    browser.find_element_by_name('filme').send_keys(filme)
    sleep(1)
    browser.find_element_by_name('email').send_keys(email)
    sleep(1)
    browser.find_element_by_name('telefone').send_keys(telefone)
    sleep(1)
    browser.find_element_by_name('enviar').click()


melhor_filme(
    firefox,
    'Um filme',
    'bea@bea.com',
    '(045)999628373'
)
