from flask import Flask , render_template, request, flash
from wtforms import Form,StringField,validators
import csv
import requests
from bs4 import BeautifulSoup
import random 


#-----------initialisation---------------

app = Flask(__name__)

app.config['SECRET_KEY'] = "weareweebs"
#--------------FormClass-----------------

class RegisterForm(Form): #inheriting form
	animetitle = StringField('anime title', [validators.Length(min=2, max=25)])
	username = StringField('Username', [validators.Length(min=4, max=25)])
	animetitle2 = StringField('anime title 2', [validators.Length(min=2, max=25)])
	animetitle3 = StringField('anime title 3', [validators.Length(min=2, max=25)])
#--------------route---------------------

@app.route('/',methods=['GET','POST'])
def index():
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		animetitle = form.animetitle.data
		animetitle2 = form.animetitle2.data
		animetitle3 = form.animetitle3.data
		user = form.username.data
		flash("Your anime reccommendation is being generated")
		#-----------animeprog--------------------
		#--------logic-----------------------------------------

		genre1 = genre2 = genre3 = []
		names =[animetitle,animetitle2,animetitle3]
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
		anilist = []				
		for i in range(10):
			anilist.append((random.choice(rani)))
		return render_template("reco.html",r1=anilist[0],r2=anilist[1],r3=anilist[2],r4=anilist[3],r5=anilist[4],r6=anilist[5],r7=anilist[6],r8=anilist[7],r9=anilist[8],r10=anilist[9],user=user)	
	return render_template('home.html',form=form)

if __name__=="__main__":
	 app.run(debug=True, use_reloader=True,port=1200)
