from selenium.webdriver import Chrome

browser = Chrome()

browser.get('http://selenium.dunossauro.live/aula_04_a.html')


lista_n_ordenada = browser.find_elements_by_tag_name('ul') # 1

lis = lista_n_ordenada = browser.find_elements_by_tag_name('li') # 2

lis[0].find_element_by_tag_name('a').text # 3

"""
1. Buscamos ul
2. Buscamos todos li
3. No primeiro 'li', buscamos 'a' e pegamos seu texto
"""