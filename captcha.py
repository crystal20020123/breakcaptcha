from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from twocaptcha import TwoCaptcha

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# chrome_options = Options()
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('window-size=1920x1080')
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome()

process_number1 = "50012759320184036127"

login_page_url = "https://web.trf3.jus.br/consultas/Internet/ConsultaReqPag"


driver.get(login_page_url)

sleep(3)
# //*[@id="ProcessoOrigem"]
driver.find_element(By.ID,'ProcessoOrigem').send_keys(process_number1)

def solve_captcha(login_page_url):
    print('Solving the captcha (solve_captcha)')
    config = {
        'server': 'rucaptcha.com',
        'apiKey': 'faf260346d92130c5d2ba6b0bfa8a0cf',
    }
    solver = TwoCaptcha(**config)
    response = solver.recaptcha(sitekey='6LetzM8ZAAAAAJQX8ibI_mFF5FYlFahVluw4NEhE', url=login_page_url)
    code = response['code']
    print(f"Successfully solved the captcha. Captcha token: {code}")
    return code


iframe = driver.find_element(By.XPATH,'//*[@id="html_element"]/div/div/iframe')
driver.switch_to.frame(iframe)
# driver.switch_to.default_content()
sleep(3)
print("1----------------")
driver.find_element(By.ID,"rc-anchor-container").click()
sleep(1)
driver.switch_to.default_content()

captcha_code = solve_captcha(login_page_url)

# script = 'document.getElementById("g-recaptcha-response").innerHTML = "%s"' % captcha_code
# print(script)
# driver.execute_script(script)
print('----------- inputting the code into textarea -------------')
token_textarea = driver.find_element(By.ID, "g-recaptcha-response")
driver.execute_script("arguments[0].style.display = 'block';", token_textarea)
token_textarea.send_keys(captcha_code)

print('----------- done inputting the code into textarea -------------')


# //*[@id="html_element"]/div/div/iframe
# driver.switch_to.default_content()
# //*[@id="rc-anchor-container"]
# driver.find_element(By.ID,'pesquisar').click()

print("2----------------")

sleep(900)