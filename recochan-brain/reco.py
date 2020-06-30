import requests
from bs4 import BeautifulSoup

name1 = name2 = name3 =''
genre1 = genre2 = genre3 = []

names = [name1, name2, name3]
genres = [genre1, genre2, genre3]

print("----------------------- ENTER NAMES OF YOUR 3 FAVOURITE ANIMES -------------------------------")

for i in range(1,4):
    names[i-1] = input(str(i) + '. Name of anime ::')

def genre_finder(name):

    url = "http://www.google.com/search?q="+name+" myanimelist"

    page = requests.get(url)
    content = page.text
    soup = BeautifulSoup(content,"html.parser")
    links = []

    for link in soup.find_all('a'):
        links.append(link.get('href'))

    url = links[16][7:]
    page = requests.get(url)
    content = page.text
    soup = BeautifulSoup(content,"html.parser")
    genre =[]

    for i in soup.find_all(itemprop ="genre"):
        genre.append(i.get_text())

    return genre

for i in range(3):
    genres[i] = genre_finder(names[i])

genre = []

for j in genres[0]:
    if j in genres[1] or genres[2]:
        genre.append(j)

for j in genres[1]:
    if j in genres[2] or genres[0]:
        if j not in genre:
            genre.append(j)

for j in genres[2]:
    if j in genres[0] or genres[1]:
        if j not in genre:
            genre.append(j)

dict = {'Action':1, 'Adventure':2, 'Cars':3, 'Comedy':4, 'Dementia':5, 'Demons':6, 'Drama':8, 'Ecchi':9, 'Fantasy':10, 'Game':11, 'Harem':35, 'Hentai':12, 'Historical':13, 'Horror':14, 'Josei':43, 'Kids':15, 'Magic':16, 'Martial Arts':17, 'Mecha':18, 'Military':38, 'Music':19, 'Mystery':7, 'Parody':20, 'Police':39, 'Psychological':40, 'Romance':22, 'Samurai':21, 'School':23, 'Sci-Fi':24, 'Seinen':42, 'Shoujo':25, 'Shoujo Ai':26, 'Shounen':27, 'Shounen Ai':28, 'Slice of Life':36, 'Space':29, 'Sports':30, 'Super Power':31, 'Supernatural':37, 'Thriller':41, 'Vampire':32, 'Yaoi':33, 'Yuri':34}
search = "https://myanimelist.net/anime/genre/"

def listmaker(n,l):
    s = ''
    c = 0
    for i in n:
        if c == 2:
            break

        else:
            if i == '\n':
                c+=1
            else:
                s+=i

    l.append(s)

animelist = []

for i in genre:
    url = search + str(dict[i])
    page = requests.get(url)
    content = page.text

    soup = BeautifulSoup(content,"html.parser")
    textfile = soup.get_text()
    list = textfile.split("Watch Video")
    list.pop(0)

    for i in range (21):
        listmaker(list[i],animelist)

print('')
num = int(input("Number of animes to be recommended (MAX is 20)::"))

def populor(l):
    counter = 0
    anime = l[0]

    for i in l:
        curr_frequency = l.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            anime = i

    return anime

def word_matcher(word1,word2):
    s = 0

    if len(word1) < len(word2):
        lenght = (len(word1))

    else:
        lenght = (len(word2))

    for i in range(lenght):
        if word1[i].lower() ==  word2[i].lower():
            s+=1

    return (s/(len(word1)))*100

animelist2 = []
for i in animelist:
    if i not in animelist2:
        animelist2.append(i)

    else:
        continue

for i in range (len(animelist2)):
    for j in range (3):
        if word_matcher(animelist2[i],names[j]) >= 50:
            for k in range(animelist.count(animelist2[i])):
                animelist.remove(animelist2[i])
recommendation = []

for i in range (num):
    anime = populor(animelist)
    recommendation.append(anime)

    for j in range(animelist.count(anime)):
        animelist.remove(anime)

print("\n==============ANIME RECOMMENDED FOR YOU=================\n")

for i in range(len(recommendation)):
    print(i+1,". ",recommendation[i])
