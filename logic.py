# -*- coding: UTF-8 -*-
import csv
import requests
from bs4 import BeautifulSoup
import random 
import sys

#--------logic-----------------------------------------

genre1 = genre2 = genre3 = []

name1 = sys.argv[1]
name2 = sys.argv[2]
name3 = sys.argv[3]
names =[name1,name2,name3]
genres = [genre1, genre2, genre3]


for name in names:
    url = "http://www.google.com/search?q="+name+" myanimelist"

    page = requests.get(url)
    content = page.text
    soup = BeautifulSoup(content,"html.parser")
    links = []

    for link in soup.find_all('a'):
        links.append(link.get('href'))

    index = 0
    counter = 0

    while counter == 0:
        if links[index][:7] == "/url?q=":
            counter = -1
        else:
            index += 1

    url = links[index][7:]
    page = requests.get(url)
    content = page.text
    soup = BeautifulSoup(content,"html.parser")
    genre =[]

    for i in soup.find_all(itemprop ="genre"):
        genre.append(i.get_text())


#---------csv-data-------------------------------------
rani = []
with open('anidatalist.csv','r',encoding='utf-8') as f:
	f_reader = csv.reader(f) 
	next(f_reader)
	for i in genre:
		for j in f_reader:
			if i==j[2]:
				rani.append(j[1])
for i in range(10):
	print(random.choice(rani))
sys.stdout.flush()
