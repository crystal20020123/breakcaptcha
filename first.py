from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
import pyautogui
from time import sleep
from twocaptcha import TwoCaptcha
import re
from openpyxl import load_workbook
def Find_Element(driver : webdriver.Chrome, by, value : str) -> WebElement:
    while True:
        try:
            element = driver.find_element(by, value)
            break
        except:
            pass
        sleep(0.1)
    return element

def Find_Elements(driver : webdriver.Chrome, by, value : str) -> list[WebElement]:
    while True:
        try:
            elements = driver.find_elements(by, value)
            if len(elements) > 0:
                break
        except:
            pass
        sleep(0.1)
    return elements

def Send_Keys(element : WebElement, content : str):
    element.clear()
    for i in content:
        element.send_keys(i)
        sleep(0.1)
def solve_captcha(login_page_url):
    print('Solving the captcha (solve_captcha)')
    config = {
        'server': 'rucaptcha.com',
        'apiKey': 'faf260346d92130c5d2ba6b0bfa8a0cf',
    }
    solver = TwoCaptcha(**config)
    response = solver.recaptcha(sitekey='6LetzM8ZAAAAAJQX8ibI_mFF5FYlFahVluw4NEhE', url=login_page_url)
    code = response['code']
    # print(f"Successfully solved the captcha. Captcha token: {code}")
    return code


def submit_captcha(driver, code):
    script = '''
        function retrieveCallback(obj, visited = new Set()) {
            if (typeof obj === 'function') return obj;
            for (const key in obj) {
                if (!visited.has(obj[key])) {
                    visited.add(obj[key]);
                    if (typeof obj[key] === 'object' || typeof obj[key] === 'function') {
                        const value = retrieveCallback(obj[key], visited);
                        if (value) {
                            return value;
                        }
                    }
                    visited.delete(obj[key]);
                }
            }
        }
        const callback = retrieveCallback(window.___grecaptcha_cfg.clients[0]);
        if (typeof callback === 'function') {
            callback('%s');
        } else {
            throw new Error('Callback function not found.');
        }
    ''' % code
    driver.execute_script(script)
def main():
    username = '002.724.798-88' 
    password = 'Saulo2509?'
    process_number1 = "50012759320184036127"
    process_number2 = process_number1[-4:]


    service = Service(executable_path="C:/chromedriver-win64/chromedriver.exe")   
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9015")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://pje1g.trf3.jus.br/")

    iframe = Find_Element(driver, By.ID, 'ssoFrame')
    driver.switch_to.frame(iframe)

    input_username = driver.find_element(By.ID, 'username')
    input_username.clear()
    input_username.send_keys(username)
    sleep(1)
    input_password = driver.find_element(By.ID, "password")
    input_password.clear()
    input_password.send_keys(password)
    sleep(1)
    driver.find_element(By.ID, "kc-login").click()



    driver.switch_to.default_content()

    menu = Find_Element(driver, By.CLASS_NAME, 'botao-menu')
    menu.click()

    sleep(1)

    processo = Find_Element(driver, By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/a')
    processo.click()

    sleep(1)
    pesquisar = Find_Element(driver, By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/ul/li[4]/a')
    pesquisar.click()

    sleep(1)
    processo1 = Find_Element(driver,By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/ul/li[4]/div/ul/li/a')
    processo1.click()

    sleep(1)
    input_cpf = driver.find_element(By.ID, 'fPP:numeroProcesso:numeroSequencial')
    input_cpf.clear()
    input_cpf.send_keys(process_number1)


    input_cpf1 = driver.find_element(By.ID, 'fPP:numeroProcesso:NumeroOrgaoJustica')
    input_cpf1.clear()
    input_cpf1.send_keys(process_number2)


    sleep(1)
    processo2 = Find_Element(driver,By.ID, 'fPP:searchProcessos')
    processo2.click()
    
    sleep(1)
    processo2 = Find_Element(driver,By.ID, 'fPP:searchProcessos')
    processo2.click()

    sleep(1)
    processo_a = Find_Element(driver,By.ID, 'fPP:processosTable:402412:j_id418')
    processo_a.click()
    sleep(1)
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except:
        return
    driver.switch_to.default_content()
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[1])
   
    processo_b = Find_Element(driver,By.XPATH, '//*[@id="navbar"]/ul/li/a[1]')
    processo_b.click()

    span = Find_Element(driver,By.XPATH, '//*[@id="poloAtivo"]/table/tbody/tr/td/span/span')
 
    text = span.get_attribute('innerHTML')
   


    cpf_pattern = r"\d{3}\.\d{3}\.\d{3}-\d{2}"

    # Search for the CPF number in the text
    match = re.search(cpf_pattern, text)

    # Check if a match was found and print the result
    if match:
        cpf_number = match.group(0)
        print(f"CPF number found: {cpf_number}")
    else:
        print("CPF number not found.")


    login_page_url = "https://web.trf3.jus.br/consultas/Internet/ConsultaReqPag"

    driver.get(login_page_url)
    captcha_code = solve_captcha(login_page_url)
    submit_captcha(driver, captcha_code)

    token_textarea = Find_Element(driver,By.ID, "g-recaptcha-response")
    driver.execute_script("arguments[0].style.display = 'block';", token_textarea)
    token_textarea.send_keys(captcha_code)

    input_processo =  Find_Element(driver,By.XPATH, '//*[@id="ProcessoOrigem"]')
    input_processo.clear()
    input_processo.send_keys(process_number1)

    submit = Find_Element(driver,By.XPATH,'//*[@id="pesquisar"]').click()
    
    sleep(1)

    table = Find_Element(driver,By.XPATH,'//*[@id="conteudoPrincipal"]/table/tbody')
    rows = Find_Elements(table,By.TAG_NAME,'tr')
    len_rows = len(rows)
    information = []
    filepath = 'test.xlsx'
    workbook = load_workbook(filename = filepath)
    sheet = workbook.active
    for row in range(1,len_rows):
        table = Find_Element(driver,By.XPATH,'//*[@id="conteudoPrincipal"]/table/tbody')
        rows = Find_Elements(table,By.TAG_NAME,'tr')
        print(row)
        icon = Find_Element(rows[row], By.TAG_NAME,'img')
        icon.click()
        # sleep(1)
        tbody = Find_Element(driver,By.XPATH,'//*[@id="grid"]/tbody')
        tds = Find_Elements(tbody,By.CLASS_NAME,'celula')
        list = []
        list.append(cpf_number)

        for td in tds:
            list.append(td.text)

        information.append(list)

        new_list = ()
        for item in range(10,len(list)-7):
            new_list += (list[item],)
        str = ','.join(new_list)
        new_list =list[:10] + [str] + list[-7:]
       
        print(new_list)
        information.append(new_list)
        sheet.append(new_list)
        workbook.save(filename = filepath)

        driver.back()
        driver.refresh()
    

if __name__ == "__main__":
    main()