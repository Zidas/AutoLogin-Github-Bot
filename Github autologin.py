from selenium import webdriver
import time



navegador = webdriver.Chrome()
navegador.get("https://github.com/login")

navegador.find_element_by_xpath('//*[@id="login_field"]').send_keys("Seu Email")

time.sleep(1)

navegador.find_element_by_xpath('//*[@id="password"]').send_keys("Sua Senha")

navegador.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]').click()