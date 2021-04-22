from selenium.webdriver import Firefox
from time import sleep


b = Firefox()

url = 'http://selenium.dunossauro.live/aula_06_a.html'

b.get(url)


# Usando o atributo type [attr=valor]
# nome = b.find_element_by_css_selector('[type="text"]')
# senha = b.find_element_by_css_selector('[type="password"]')
# btn = b.find_element_by_css_selector('[type="submit"]')


# Usando o atributo name [attr=valor]
# nome = b.find_element_by_css_selector('[name="nome"]')
# senha = b.find_element_by_css_selector('[name="senha"]')
# btn = b.find_element_by_css_selector('[name="l0c0"]')

# Usando o atributo * [attr*=valor]
# nome = b.find_element_by_css_selector('[name*="ome"]')
# senha = b.find_element_by_css_selector('[name*="nha"]')
# btn = b.find_element_by_css_selector('[name*="l0"]')

# Usando o atributo | [attr|=valor]
# nome = b.find_element_by_css_selector('[name|="nome"]')
# senha = b.find_element_by_css_selector('[name|="senha"]')
# btn = b.find_element_by_css_selector('[name|="l0c0"]')

# Usando o atributo ^ [attr^=valor]
nome = b.find_element_by_css_selector('[name^="n"]')
senha = b.find_element_by_css_selector('[name^="s"]')
btn = b.find_element_by_css_selector('[name^="l"]')



sleep(1)
nome.send_keys('Beatriz')
sleep(1)
senha.send_keys('b12345')
sleep(0.5)
btn.click()