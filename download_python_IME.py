#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
#
# feito por: Marcos Rodrigues de Carvalho
# Cidade: Itatiba
# Estado: SP

from bs4 import BeautifulSoup
from urllib.request import urlopen
import os

url = 'http://www.ime.eb.br/provas-anteriores-cfg.html'
resp = urlopen(url).read()

info = str(url).split('/')

print('''
=======================
= Informações obtidas =
=======================

Site: - - - - - - - - - - - - - - - {}
Pagina que o scrapping ira atuar: - {}

========================
= Arquivos encontrados =
========================
'''.format(info[2], info[3]))

soup = BeautifulSoup(resp, 'html.parser')
for link in soup.find_all('a'):
    if link.get('href')[-3:] in 'pdf':
        nome = (link.get('href').split('/')[-1])
        linkd = 'http://' + url.split('/')[2] + link.get('href')
        
        with open(nome, 'wb') as f:
            f.write(urlopen(linkd).read())  
            print(nome + ' --> ' + os.getcwd() + '/' + nome)
