# -*- coding: UTF-8 -*- 

import os
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/snap/bin/chromium.chromedriver')

path = '/home/sheylong/Downloads/'
dirs = os.listdir(path)
print('Quantidade de arquivos: ',len(dirs))

def logar():
	driver.get("https://www4.receita.pb.gov.br/atf/")
	driver.set_window_size(1296, 704)
	driver.switch_to.frame(1)
	driver.find_element(By.ID, "login").send_keys('fra13582')
	driver.find_element(By.NAME, "edtDsSenha").click()
	driver.find_element(By.NAME, "edtDsSenha").send_keys('fiscal3336*')
	time.sleep(2)

	driver.find_element(By.NAME, "btnAvancar").click()
	time.sleep(5)

def listIds():
	Ids = []
	table_id = driver.find_element(By.CLASS_NAME, 'fontePadrao')
	rows = table_id.find_elements(By.TAG_NAME, "a") 
	for row in rows:
	    id_ = row.get_attribute('href').encode("utf-8")
	    if len(id_)>0:
		    ID = id_.split("'")
		    Ids.append(ID[1])
	return Ids

#logar()
#driver.get('https://www4.receita.pb.gov.br/atf/seg/SEGf_MinhasMensagens.do?limparSessao=true')
#Ids = sorted(set(listIds()))
#print('Quantidade de solicitações')
#print(len(Ids))