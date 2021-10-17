from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

"""Page"""
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://gestorsigeci-hml.gcba.gob.ar/gestorcitas/app/#!/operario/')

"""Login"""
correo = driver.find_element_by_id('username')
correo.send_keys('20353428323')
passwd = driver.find_element_by_id('password')
passwd.send_keys('Troquel1')
passwd.send_keys(Keys.ENTER)

time.sleep(1)

"""Create"""
for i in range(1,100): # Operadores de X a Y
    driver.find_element_by_css_selector('.btn.btn-primary.btn-lg').click()
    time.sleep(.5)
    Sede = Select(driver.find_element_by_tag_name('select'))
    Sede.select_by_visible_text('Parque Avellaneda') # Nombre de la sede
    nombre = driver.find_element_by_name('nombre') 
    nombre.send_keys(f'Castraciones GATAS - Op{i}') # Nombre del operador
    # time.sleep(.5)
    nombre.send_keys(Keys.ENTER)
    time.sleep(.5)
    driver.refresh()
    time.sleep(1)

"""Close"""
time.sleep(10)
driver.close()