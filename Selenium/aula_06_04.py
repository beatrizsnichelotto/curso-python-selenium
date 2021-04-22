from selenium.webdriver import Firefox

b = Firefox()

url = 'http://selenium.dunossauro.live/aula_06.html'

b.get(url)

# preencher nome form automaticametne 
b.find_element_by_css_selector('.form-l1c1 input[name="nome"]').send_keys('beatrix')
b.find_element_by_css_selector('.form-l1c0 input[name="nome"]').send_keys('beatrix')
b.find_element_by_css_selector('.form-l0c1 input[name="nome"]').send_keys('beatrix')
b.find_element_by_css_selector('.form-l0c0 input[name="nome"]').send_keys('beatrix')