from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse
from json import loads

url = 'http://selenium.dunossauro.live/aula_05.html'

firefox = Firefox()

firefox.get(url)

# nome, email, senha, telefone, btn


def preenche_form(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()


sleep(1)

estrutura = {
    'nome': 'Beatriz',
    'email': 'bea@bea.com',
    'senha': 'b12345',
    'telefone': '999628373'
}

preenche_form(firefox, **estrutura)

url_parseada = urlparse(firefox.current_url)

sleep(3)

texto_resultado = firefox.find_element_by_id('result').text
resultado_arrumado = texto_resultado.replace('\'', "\"")

dic_result = loads(resultado_arrumado)


assert dic_result == estrutura

# firefox.quit()