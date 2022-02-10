# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 13:41:34 2022

@author: Eduardo
"""


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd

navegador = webdriver.Chrome()
navegador.get('https://zenodo.org/communities/covid-19/search?page=1&size=1943')


sleep(2)

page_content = navegador.page_source

site = BeautifulSoup(page_content, 'html.parser')
#print(site.prettify())

lista_trabalhos = []

dateList = site.findAll('span', {'class': 'label label-info ng-scope ng-binding'})
tipoList = site.findAll('span', {'class': 'label label-default ng-binding'})
acessoList = site.findAll('span', {'class': 'label label-success titlecase'})
titles = site.find_all(['h4'])
upload = site.findAll('small', {'class': 'text-muted hidden-xs ng-binding'})
rodape = site.findAll('i', {'class': 'ng-binding'})
resumo = site.findAll('p', {'class': 'hidden-xs'})

print(len(dateList))
print(len(tipoList))
print(len(acessoList))
print(len(titles))
print(len(upload))
print(len(rodape))
print(len(resumo))

i = 0;
while i < len (titles):
    print(dateList[i].get_text())
    print(tipoList[i].get_text())
    print(acessoList[i].get_text())
    print(titles[i].get_text())
    print(resumo[i].get_text())
    #print(upload[i].get_text())
    #print(rodape[i].get_text())
    print()


#adicionando cada artigo(lista de informações) na lista de trabalhos que serão incluídos no dataframe


i = 0;
while i <= len (titles):  
    lista_trabalhos.append(
            [dateList[i].get_text(), tipoList[i].get_text(), acessoList[i].get_text(), titles[i].get_text(), resumo[i].get_text()])
    i+=1       
    if i > 1943:
        break
    
   

#Criando o dataFrame e especificiando o título das colunas no arquivo que será exportado
df = pd.DataFrame(lista_trabalhos, columns=['Data Publicação', 'Tipo', 'Acesso', 'Título', 'Resumo'])

#o index=False é para não exibir os indices do dataFrame na tabela.
df.to_excel('artigos_zenodo1.xlsx', index=False)

