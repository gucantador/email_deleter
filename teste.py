from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 


def transformer(text):

    transforming = text
    suming = transforming[3] + transforming[5:8]

    suming = int(suming)

    return suming
email = input("Digite seu email: ")
password = input("Digite sua senha: ")


driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://email.uolhost.com.br')
driver.find_element_by_name("login").send_keys(email)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_name("password").send_keys(Keys.RETURN)
time.sleep(30)
print("passou 30 segundos")

email_min = driver.find_element_by_xpath("/html/body/div[3]/div/section[2]/div/div[2]/div/div[2]/section[1]/div/div[7]/div/div/div[2]/span")
email_min_text = email_min.text
page = transformer(email_min_text)
driver.find_element_by_xpath("/html/body/div[3]/div/section[2]/div/div[2]/div/div[2]/section[1]/div/div[7]/div/div/div[3]/a[2]/menu").click()
time.sleep(6)
print("MARCADOR")
contador = 0
while page > 1000:

    
    driver.find_element_by_xpath("/html/body/div[3]/div/section[2]/div/div[2]/div/div[2]/section[1]/div/div[1]/label").click()
    time.sleep(6)
    driver.find_element_by_xpath("/html/body/div[3]/div/section[2]/div/div[2]/div/div[1]/div[1]/span/ul/li[2]/span").click()
    time.sleep(6)
    driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/span[1]").click()
    time.sleep(6)
    email_min = driver.find_element_by_xpath("/html/body/div[3]/div/section[2]/div/div[2]/div/div[2]/section[1]/div/div[7]/div/div/div[2]/span")
    email_min_text = email_min.text
    page = transformer(email_min_text)
    contador = contador + 1
    print('Programa executado {} vezes.'.format(contador))
    time.sleep(6)

print("."*10)
print('Vamos deletar da lixeira agora')
print("."*10)

driver.find_element_by_xpath('//*[@id="fc-collapsable-sidebar"]/div[3]/div[2]/div/div[1]/ul/li[4]').click()
time.sleep(6)
email_min2 = driver.find_element_by_xpath("/html/body/div[3]/div/section[2]/div/div[2]/div/div[2]/section[1]/div/div[8]/div/div/div[2]/span")
email_min_text2 = email_min2.text
page2 = transformer(email_min_text2)
driver.find_element_by_xpath("/html/body/div[3]/div/section[2]/div/div[2]/div/div[2]/section[1]/div/div[8]/div/div/div[3]/a[2]/menu/spam").click()
time.sleep(6)



while page2 > 0:

    
    driver.find_element_by_xpath("/html/body/div[3]/div/section[2]/div/div[2]/div/div[2]/section[1]/div/div[1]/label").click()
    time.sleep(6)
    driver.find_element_by_xpath("/html/body/div[3]/div/section[2]/div/div[2]/div/div[1]/div[1]/span/ul/li[2]/span/span").click()
    time.sleep(6)
    driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/span[1]").click()
    time.sleep(6)
    email_min2 = driver.find_element_by_xpath("/html/body/div[3]/div/section[2]/div/div[2]/div/div[2]/section[1]/div/div[8]/div/div/div[2]/span")
    email_min_text2 = email_min2.text
    page2 = transformer(email_min_text2)
    driver.find_element_by_xpath("/html/body/div[3]/div/section[2]/div/div[2]/div/div[2]/section[1]/div/div[8]/div/div/div[3]/a[2]/menu/spam").click()
    contador = contador + 1
    print('Programa executado {} vezes.'.format(contador))
    time.sleep(6)


print('chegou ao final')