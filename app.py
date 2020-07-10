# -*- coding: UTF-8 -*-
#!/usr/bin/python -tt

from flask import Flask, request, render_template, flash, redirect, url_for
from wtforms import Form,StringField,validators,SelectField
import csv
import requests
from bs4 import BeautifulSoup
import random 
from multiprocessing import Pool

#-----------initialisation---------------

app = Flask(__name__)
app.config['SECRET_KEY'] = "weareweebs"
#--------------FormClass-----------------

class RegisterForm(Form): #inheriting form
	animetitle = StringField('anime title 1', [validators.Length(min=2, max=25)])
	username = StringField('Username', [validators.Length(min=4, max=25)])
	animetitle2 = StringField('anime title 2', [validators.Length(min=2, max=25)])
	animetitle3 = StringField('anime title 3', [validators.Length(min=2, max=25)])
	maxin = SelectField('Enter number of animes to be recommended',choices=[(5,'5'),(10,'10')],coerce=int)


#--------------Class and funct definitions---------
class database:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file,encoding = "utf8")
        self.data = csv.reader(self.f, delimiter = ",")
        self.data = list(self.data)
        self.data.pop(0)

    def get_genre(self, anime):
        self.anime = anime
        for i in self.data:
            if i[1] == self.anime:
                return self.list_maker(i[3])

        return []

    def get_anime(self, genre):
        self.genre = genre
        self.anime_names = []
        for i in self.data:
            if self.genre in  self.list_maker(i[3]):
                self.anime_names.append(i[1])
                

        return self.anime_names

    def list_maker(self, lst):
        self.lst = lst.strip("['")
        self.lst = self.lst.strip("']")
        return self.lst.split("', '")

    def done(self):
        self.f.close()

def spellchecker(spell):
    url = "http://www.google.com/search?q=" + spell + " myanimelist"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    correct_spell = soup.find_all("h3")[0]
    correct_spell = correct_spell.get_text()
    if "(" not in correct_spell:
        return correct_spell.split(" - MyAnimeList.net").pop(0)
    else:
        return correct_spell.split(" (").pop(0)

def repeater(lst):
    once = []
    repeat = []
    for i in lst:
        if i not in once:
            once.append(i)
        else:
            if i not in repeat:
                repeat.append(i)

    return repeat
def gogo(aname):
	query = f"https://gogoanime.pro/search?keyword={aname}"
	page = requests.get(query)
	soup = BeautifulSoup(page.text, "html.parser")
	gogo = soup.find_all('ul',class_='items')[0].p.a['href']
	gogoimg = soup.find_all('ul',class_='items')[0].div.a.img['src']
	return gogoimg,f'https://gogoanime.pro{gogo}'
	
animes = database("database.csv")

#--------------route---------------------

@app.route('/', methods=['GET','POST'])
def form():
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		animetitle = form.animetitle.data
		animetitle2 = form.animetitle2.data
		animetitle3 = form.animetitle3.data
		user = form.username.data
		maxin = form.maxin.data
		flash("Your anime reccommendation is being generated",category="'success'")
		#-----------animeprog--------------------
		#--------logic-----------------------------------------
		names =[animetitle,animetitle2,animetitle3]
		input_anime = []
		genres = []
		anime_list = []
		for i in names:
			input_anime.append(spellchecker(i))		
		for i in input_anime:
			genres += animes.get_genre(i)
		for i in repeater(genres):
			anime_list += animes.get_anime(i)

		reco_anime = repeater(anime_list)

		for i in reco_anime:
			if i in input_anime:
				reco_anime.remove(i)
		
		emp,links,imgs = [],[],[]		
		
		if len(reco_anime) <= 5:
			return render_template("error.html")

		elif maxin == 5:
			for i in range(5):
				random_anime = random.choice(reco_anime)
				emp.append(random_anime)
				if __name__ == '__main__':
					with Pool(5) as p:
						imgs = [i[0] for i in p.map(gogo, emp)] 
						links = [i[1] for i in p.map(gogo, emp)]
			return render_template("reco5.html",r0=emp[0],r1=emp[1],r2=emp[2],r3=emp[3],r4=emp[4],l0=links[0],l1=links[1],l2=links[2],l3=links[3],l4=links[4],im0=imgs[0],im1=imgs[1],im2=imgs[2],im3=imgs[3],im4=imgs[4],user=user)
		
		else : 
			for i in range(10):
				emp.append(random.choice(reco_anime))
			return render_template("reco10.html",r0=emp[0],r1=emp[1],r2=emp[2],r3=emp[3],r4=emp[4],r5=emp[5],r6=emp[6],r7=emp[7],r8=emp[8],r9=emp[9],r10=emp[10],user=user)
	return render_template('home.html',form=form) 
	

#--------start-app-------------------------------------
if __name__ == '__main__':
	app.run(debug=True)
