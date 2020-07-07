# -*- coding: UTF-8 -*-
#!/usr/bin/python -tt

from flask import Flask, request, render_template, flash, redirect, url_for
from wtforms import Form,StringField,validators,SelectField
import csv
import requests
from bs4 import BeautifulSoup
import random 

#-----------initialisation---------------

app = Flask(__name__)
app.config['SECRET_KEY'] = "weareweebs"
#--------------FormClass-----------------

class RegisterForm(Form): #inheriting form
	animetitle = StringField('anime title 1', [validators.Length(min=2, max=25)])
	username = StringField('Username', [validators.Length(min=4, max=25)])
	animetitle2 = StringField('anime title 2', [validators.Length(min=2, max=25)])
	animetitle3 = StringField('anime title 3', [validators.Length(min=2, max=25)])
	maxin = SelectField('Enter number of animes to be recommended',choices=[(5,'5'),(10,'10'),(50,'50'),(100,'100'),(200,'200'),(300,'300'),(400,'400')],coerce=int)


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
		flash("Your anime reccommendation has been generated",category="'success'")
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
		emp = []		
	
		if maxin == 5:
			for i in range(6):
				emp.append(random.choice(reco_anime))
			return render_template("reco5.html",r0=emp[0],r1=emp[1],r2=emp[2],r3=emp[3],r4=emp[4],r5=emp[5],user=user)
		
		elif maxin == 10: 
			for i in range(11):
				emp.append(random.choice(reco_anime))
			return render_template("reco10.html",r0=emp[0],r1=emp[1],r2=emp[2],r3=emp[3],r4=emp[4],r5=emp[5],r6=emp[6],r7=emp[7],r8=emp[8],r9=emp[9],r10=emp[10],user=user)
		
		elif maxin == 50:
			for i in range(51):
				emp.append(random.choice(reco_anime))
			return render_template("reco50.html",r0=emp[0],r1=emp[1],r2=emp[2],r3=emp[3],r4=emp[4],r5=emp[5],r6=emp[6],r7=emp[7],r8=emp[8],r9=emp[9],r10=emp[10],r11=emp[11],r12=emp[12],r13=emp[13],r14=emp[14],r15=emp[15],r16=emp[16],r17=emp[17],r18=emp[18],r19=emp[19],r20=emp[20],r21=emp[21],r22=emp[22],r23=emp[23],r24=emp[24],r25=emp[25],r26=emp[26],r27=emp[27],r28=emp[28],r29=emp[29],r30=emp[30],r31=emp[31],r32=emp[32],r33=emp[33],r34=emp[34],r35=emp[35],r36=emp[36],r37=emp[37],r38=emp[38],r39=emp[39],r40=emp[40],r41=emp[41],r42=emp[42],r43=emp[43],r44=emp[44],r45=emp[45],r46=emp[46],r47=emp[47],r48=emp[48],r49=emp[49],r50=emp[50],user=user)
		
		elif maxin == 100:
			for i in range(101):
				emp.append(random.choice(reco_anime))
			return render_template("reco100.html",r0=emp[0],r1=emp[1],r2=emp[2],r3=emp[3],r4=emp[4],r5=emp[5],r6=emp[6],r7=emp[7],r8=emp[8],r9=emp[9],r10=emp[10],r11=emp[11],r12=emp[12],r13=emp[13],r14=emp[14],r15=emp[15],r16=emp[16],r17=emp[17],r18=emp[18],r19=emp[19],r20=emp[20],r21=emp[21],r22=emp[22],r23=emp[23],r24=emp[24],r25=emp[25],r26=emp[26],r27=emp[27],r28=emp[28],r29=emp[29],r30=emp[30],r31=emp[31],r32=emp[32],r33=emp[33],r34=emp[34],r35=emp[35],r36=emp[36],r37=emp[37],r38=emp[38],r39=emp[39],r40=emp[40],r41=emp[41],r42=emp[42],r43=emp[43],r44=emp[44],r45=emp[45],r46=emp[46],r47=emp[47],r48=emp[48],r49=emp[49],r50=emp[50],r51=emp[51],r52=emp[52],r53=emp[53],r54=emp[54],r55=emp[55],r56=emp[56],r57=emp[57],r58=emp[58],r59=emp[59],r60=emp[60],r61=emp[61],r62=emp[62],r63=emp[63],r64=emp[64],r65=emp[65],r66=emp[66],r67=emp[67],r68=emp[68],r69=emp[69],r70=emp[70],r71=emp[71],r72=emp[72],r73=emp[73],r74=emp[74],r75=emp[75],r76=emp[76],r77=emp[77],r78=emp[78],r79=emp[79],r80=emp[80],r81=emp[81],r82=emp[82],r83=emp[83],r84=emp[84],r85=emp[85],r86=emp[86],r87=emp[87],r88=emp[88],r89=emp[89],r90=emp[90],r91=emp[91],r92=emp[92],r93=emp[93],r94=emp[94],r95=emp[95],r96=emp[96],r97=emp[97],r98=emp[98],r99=emp[99],r100=emp[100],user=user)
		
		elif maxin == 200:
			for i in range(201):
				emp.append(random.choice(reco_anime))
			return render_template("reco200.html",r0=emp[0],r1=emp[1],r2=emp[2],r3=emp[3],r4=emp[4],r5=emp[5],r6=emp[6],r7=emp[7],r8=emp[8],r9=emp[9],r10=emp[10],r11=emp[11],r12=emp[12],r13=emp[13],r14=emp[14],r15=emp[15],r16=emp[16],r17=emp[17],r18=emp[18],r19=emp[19],r20=emp[20],r21=emp[21],r22=emp[22],r23=emp[23],r24=emp[24],r25=emp[25],r26=emp[26],r27=emp[27],r28=emp[28],r29=emp[29],r30=emp[30],r31=emp[31],r32=emp[32],r33=emp[33],r34=emp[34],r35=emp[35],r36=emp[36],r37=emp[37],r38=emp[38],r39=emp[39],r40=emp[40],r41=emp[41],r42=emp[42],r43=emp[43],r44=emp[44],r45=emp[45],r46=emp[46],r47=emp[47],r48=emp[48],r49=emp[49],r50=emp[50],r51=emp[51],r52=emp[52],r53=emp[53],r54=emp[54],r55=emp[55],r56=emp[56],r57=emp[57],r58=emp[58],r59=emp[59],r60=emp[60],r61=emp[61],r62=emp[62],r63=emp[63],r64=emp[64],r65=emp[65],r66=emp[66],r67=emp[67],r68=emp[68],r69=emp[69],r70=emp[70],r71=emp[71],r72=emp[72],r73=emp[73],r74=emp[74],r75=emp[75],r76=emp[76],r77=emp[77],r78=emp[78],r79=emp[79],r80=emp[80],r81=emp[81],r82=emp[82],r83=emp[83],r84=emp[84],r85=emp[85],r86=emp[86],r87=emp[87],r88=emp[88],r89=emp[89],r90=emp[90],r91=emp[91],r92=emp[92],r93=emp[93],r94=emp[94],r95=emp[95],r96=emp[96],r97=emp[97],r98=emp[98],r99=emp[99],r100=emp[100],r101=emp[101],r102=emp[102],r103=emp[103],r104=emp[104],r105=emp[105],r106=emp[106],r107=emp[107],r108=emp[108],r109=emp[109],r110=emp[110],r111=emp[111],r112=emp[112],r113=emp[113],r114=emp[114],r115=emp[115],r116=emp[116],r117=emp[117],r118=emp[118],r119=emp[119],r120=emp[120],r121=emp[121],r122=emp[122],r123=emp[123],r124=emp[124],r125=emp[125],r126=emp[126],r127=emp[127],r128=emp[128],r129=emp[129],r130=emp[130],r131=emp[131],r132=emp[132],r133=emp[133],r134=emp[134],r135=emp[135],r136=emp[136],r137=emp[137],r138=emp[138],r139=emp[139],r140=emp[140],r141=emp[141],r142=emp[142],r143=emp[143],r144=emp[144],r145=emp[145],r146=emp[146],r147=emp[147],r148=emp[148],r149=emp[149],r150=emp[150],r151=emp[151],r152=emp[152],r153=emp[153],r154=emp[154],r155=emp[155],r156=emp[156],r157=emp[157],r158=emp[158],r159=emp[159],r160=emp[160],r161=emp[161],r162=emp[162],r163=emp[163],r164=emp[164],r165=emp[165],r166=emp[166],r167=emp[167],r168=emp[168],r169=emp[169],r170=emp[170],r171=emp[171],r172=emp[172],r173=emp[173],r174=emp[174],r175=emp[175],r176=emp[176],r177=emp[177],r178=emp[178],r179=emp[179],r180=emp[180],r181=emp[181],r182=emp[182],r183=emp[183],r184=emp[184],r185=emp[185],r186=emp[186],r187=emp[187],r188=emp[188],r189=emp[189],r190=emp[190],r191=emp[191],r192=emp[192],r193=emp[193],r194=emp[194],r195=emp[195],r196=emp[196],r197=emp[197],r198=emp[198],r199=emp[199],r200=emp[200],user=user)
		
		elif maxin == 300:
			for i in range(301):
				emp.append(random.choice(reco_anime))
			return render_template("reco300.html",r0=emp[0],r1=emp[1],r2=emp[2],r3=emp[3],r4=emp[4],r5=emp[5],r6=emp[6],r7=emp[7],r8=emp[8],r9=emp[9],r10=emp[10],r11=emp[11],r12=emp[12],r13=emp[13],r14=emp[14],r15=emp[15],r16=emp[16],r17=emp[17],r18=emp[18],r19=emp[19],r20=emp[20],r21=emp[21],r22=emp[22],r23=emp[23],r24=emp[24],r25=emp[25],r26=emp[26],r27=emp[27],r28=emp[28],r29=emp[29],r30=emp[30],r31=emp[31],r32=emp[32],r33=emp[33],r34=emp[34],r35=emp[35],r36=emp[36],r37=emp[37],r38=emp[38],r39=emp[39],r40=emp[40],r41=emp[41],r42=emp[42],r43=emp[43],r44=emp[44],r45=emp[45],r46=emp[46],r47=emp[47],r48=emp[48],r49=emp[49],r50=emp[50],r51=emp[51],r52=emp[52],r53=emp[53],r54=emp[54],r55=emp[55],r56=emp[56],r57=emp[57],r58=emp[58],r59=emp[59],r60=emp[60],r61=emp[61],r62=emp[62],r63=emp[63],r64=emp[64],r65=emp[65],r66=emp[66],r67=emp[67],r68=emp[68],r69=emp[69],r70=emp[70],r71=emp[71],r72=emp[72],r73=emp[73],r74=emp[74],r75=emp[75],r76=emp[76],r77=emp[77],r78=emp[78],r79=emp[79],r80=emp[80],r81=emp[81],r82=emp[82],r83=emp[83],r84=emp[84],r85=emp[85],r86=emp[86],r87=emp[87],r88=emp[88],r89=emp[89],r90=emp[90],r91=emp[91],r92=emp[92],r93=emp[93],r94=emp[94],r95=emp[95],r96=emp[96],r97=emp[97],r98=emp[98],r99=emp[99],r100=emp[100],r101=emp[101],r102=emp[102],r103=emp[103],r104=emp[104],r105=emp[105],r106=emp[106],r107=emp[107],r108=emp[108],r109=emp[109],r110=emp[110],r111=emp[111],r112=emp[112],r113=emp[113],r114=emp[114],r115=emp[115],r116=emp[116],r117=emp[117],r118=emp[118],r119=emp[119],r120=emp[120],r121=emp[121],r122=emp[122],r123=emp[123],r124=emp[124],r125=emp[125],r126=emp[126],r127=emp[127],r128=emp[128],r129=emp[129],r130=emp[130],r131=emp[131],r132=emp[132],r133=emp[133],r134=emp[134],r135=emp[135],r136=emp[136],r137=emp[137],r138=emp[138],r139=emp[139],r140=emp[140],r141=emp[141],r142=emp[142],r143=emp[143],r144=emp[144],r145=emp[145],r146=emp[146],r147=emp[147],r148=emp[148],r149=emp[149],r150=emp[150],r151=emp[151],r152=emp[152],r153=emp[153],r154=emp[154],r155=emp[155],r156=emp[156],r157=emp[157],r158=emp[158],r159=emp[159],r160=emp[160],r161=emp[161],r162=emp[162],r163=emp[163],r164=emp[164],r165=emp[165],r166=emp[166],r167=emp[167],r168=emp[168],r169=emp[169],r170=emp[170],r171=emp[171],r172=emp[172],r173=emp[173],r174=emp[174],r175=emp[175],r176=emp[176],r177=emp[177],r178=emp[178],r179=emp[179],r180=emp[180],r181=emp[181],r182=emp[182],r183=emp[183],r184=emp[184],r185=emp[185],r186=emp[186],r187=emp[187],r188=emp[188],r189=emp[189],r190=emp[190],r191=emp[191],r192=emp[192],r193=emp[193],r194=emp[194],r195=emp[195],r196=emp[196],r197=emp[197],r198=emp[198],r199=emp[199],r200=emp[200],r201=emp[201],r202=emp[202],r203=emp[203],r204=emp[204],r205=emp[205],r206=emp[206],r207=emp[207],r208=emp[208],r209=emp[209],r210=emp[210],r211=emp[211],r212=emp[212],r213=emp[213],r214=emp[214],r215=emp[215],r216=emp[216],r217=emp[217],r218=emp[218],r219=emp[219],r220=emp[220],r221=emp[221],r222=emp[222],r223=emp[223],r224=emp[224],r225=emp[225],r226=emp[226],r227=emp[227],r228=emp[228],r229=emp[229],r230=emp[230],r231=emp[231],r232=emp[232],r233=emp[233],r234=emp[234],r235=emp[235],r236=emp[236],r237=emp[237],r238=emp[238],r239=emp[239],r240=emp[240],r241=emp[241],r242=emp[242],r243=emp[243],r244=emp[244],r245=emp[245],r246=emp[246],r247=emp[247],r248=emp[248],r249=emp[249],r250=emp[250],r251=emp[251],r252=emp[252],r253=emp[253],r254=emp[254],r255=emp[255],r256=emp[256],r257=emp[257],r258=emp[258],r259=emp[259],r260=emp[260],r261=emp[261],r262=emp[262],r263=emp[263],r264=emp[264],r265=emp[265],r266=emp[266],r267=emp[267],r268=emp[268],r269=emp[269],r270=emp[270],r271=emp[271],r272=emp[272],r273=emp[273],r274=emp[274],r275=emp[275],r276=emp[276],r277=emp[277],r278=emp[278],r279=emp[279],r280=emp[280],r281=emp[281],r282=emp[282],r283=emp[283],r284=emp[284],r285=emp[285],r286=emp[286],r287=emp[287],r288=emp[288],r289=emp[289],r290=emp[290],r291=emp[291],r292=emp[292],r293=emp[293],r294=emp[294],r295=emp[295],r296=emp[296],r297=emp[297],r298=emp[298],r299=emp[299],r300=emp[300],user=user)
		
		else :
			return render_template("reco400.html",r0=emp[0],r1=emp[1],r2=emp[2],r3=emp[3],r4=emp[4],r5=emp[5],r6=emp[6],r7=emp[7],r8=emp[8],r9=emp[9],r10=emp[10],r11=emp[11],r12=emp[12],r13=emp[13],r14=emp[14],r15=emp[15],r16=emp[16],r17=emp[17],r18=emp[18],r19=emp[19],r20=emp[20],r21=emp[21],r22=emp[22],r23=emp[23],r24=emp[24],r25=emp[25],r26=emp[26],r27=emp[27],r28=emp[28],r29=emp[29],r30=emp[30],r31=emp[31],r32=emp[32],r33=emp[33],r34=emp[34],r35=emp[35],r36=emp[36],r37=emp[37],r38=emp[38],r39=emp[39],r40=emp[40],r41=emp[41],r42=emp[42],r43=emp[43],r44=emp[44],r45=emp[45],r46=emp[46],r47=emp[47],r48=emp[48],r49=emp[49],r50=emp[50],r51=emp[51],r52=emp[52],r53=emp[53],r54=emp[54],r55=emp[55],r56=emp[56],r57=emp[57],r58=emp[58],r59=emp[59],r60=emp[60],r61=emp[61],r62=emp[62],r63=emp[63],r64=emp[64],r65=emp[65],r66=emp[66],r67=emp[67],r68=emp[68],r69=emp[69],r70=emp[70],r71=emp[71],r72=emp[72],r73=emp[73],r74=emp[74],r75=emp[75],r76=emp[76],r77=emp[77],r78=emp[78],r79=emp[79],r80=emp[80],r81=emp[81],r82=emp[82],r83=emp[83],r84=emp[84],r85=emp[85],r86=emp[86],r87=emp[87],r88=emp[88],r89=emp[89],r90=emp[90],r91=emp[91],r92=emp[92],r93=emp[93],r94=emp[94],r95=emp[95],r96=emp[96],r97=emp[97],r98=emp[98],r99=emp[99],r100=emp[100],r101=emp[101],r102=emp[102],r103=emp[103],r104=emp[104],r105=emp[105],r106=emp[106],r107=emp[107],r108=emp[108],r109=emp[109],r110=emp[110],r111=emp[111],r112=emp[112],r113=emp[113],r114=emp[114],r115=emp[115],r116=emp[116],r117=emp[117],r118=emp[118],r119=emp[119],r120=emp[120],r121=emp[121],r122=emp[122],r123=emp[123],r124=emp[124],r125=emp[125],r126=emp[126],r127=emp[127],r128=emp[128],r129=emp[129],r130=emp[130],r131=emp[131],r132=emp[132],r133=emp[133],r134=emp[134],r135=emp[135],r136=emp[136],r137=emp[137],r138=emp[138],r139=emp[139],r140=emp[140],r141=emp[141],r142=emp[142],r143=emp[143],r144=emp[144],r145=emp[145],r146=emp[146],r147=emp[147],r148=emp[148],r149=emp[149],r150=emp[150],r151=emp[151],r152=emp[152],r153=emp[153],r154=emp[154],r155=emp[155],r156=emp[156],r157=emp[157],r158=emp[158],r159=emp[159],r160=emp[160],r161=emp[161],r162=emp[162],r163=emp[163],r164=emp[164],r165=emp[165],r166=emp[166],r167=emp[167],r168=emp[168],r169=emp[169],r170=emp[170],r171=emp[171],r172=emp[172],r173=emp[173],r174=emp[174],r175=emp[175],r176=emp[176],r177=emp[177],r178=emp[178],r179=emp[179],r180=emp[180],r181=emp[181],r182=emp[182],r183=emp[183],r184=emp[184],r185=emp[185],r186=emp[186],r187=emp[187],r188=emp[188],r189=emp[189],r190=emp[190],r191=emp[191],r192=emp[192],r193=emp[193],r194=emp[194],r195=emp[195],r196=emp[196],r197=emp[197],r198=emp[198],r199=emp[199],r200=emp[200],r201=emp[201],r202=emp[202],r203=emp[203],r204=emp[204],r205=emp[205],r206=emp[206],r207=emp[207],r208=emp[208],r209=emp[209],r210=emp[210],r211=emp[211],r212=emp[212],r213=emp[213],r214=emp[214],r215=emp[215],r216=emp[216],r217=emp[217],r218=emp[218],r219=emp[219],r220=emp[220],r221=emp[221],r222=emp[222],r223=emp[223],r224=emp[224],r225=emp[225],r226=emp[226],r227=emp[227],r228=emp[228],r229=emp[229],r230=emp[230],r231=emp[231],r232=emp[232],r233=emp[233],r234=emp[234],r235=emp[235],r236=emp[236],r237=emp[237],r238=emp[238],r239=emp[239],r240=emp[240],r241=emp[241],r242=emp[242],r243=emp[243],r244=emp[244],r245=emp[245],r246=emp[246],r247=emp[247],r248=emp[248],r249=emp[249],r250=emp[250],r251=emp[251],r252=emp[252],r253=emp[253],r254=emp[254],r255=emp[255],r256=emp[256],r257=emp[257],r258=emp[258],r259=emp[259],r260=emp[260],r261=emp[261],r262=emp[262],r263=emp[263],r264=emp[264],r265=emp[265],r266=emp[266],r267=emp[267],r268=emp[268],r269=emp[269],r270=emp[270],r271=emp[271],r272=emp[272],r273=emp[273],r274=emp[274],r275=emp[275],r276=emp[276],r277=emp[277],r278=emp[278],r279=emp[279],r280=emp[280],r281=emp[281],r282=emp[282],r283=emp[283],r284=emp[284],r285=emp[285],r286=emp[286],r287=emp[287],r288=emp[288],r289=emp[289],r290=emp[290],r291=emp[291],r292=emp[292],r293=emp[293],r294=emp[294],r295=emp[295],r296=emp[296],r297=emp[297],r298=emp[298],r299=emp[299],r300=emp[300],r301=emp[301],r302=emp[302],r303=emp[303],r304=emp[304],r305=emp[305],r306=emp[306],r307=emp[307],r308=emp[308],r309=emp[309],r310=emp[310],r311=emp[311],r312=emp[312],r313=emp[313],r314=emp[314],r315=emp[315],r316=emp[316],r317=emp[317],r318=emp[318],r319=emp[319],r320=emp[320],r321=emp[321],r322=emp[322],r323=emp[323],r324=emp[324],r325=emp[325],r326=emp[326],r327=emp[327],r328=emp[328],r329=emp[329],r330=emp[330],r331=emp[331],r332=emp[332],r333=emp[333],r334=emp[334],r335=emp[335],r336=emp[336],r337=emp[337],r338=emp[338],r339=emp[339],r340=emp[340],r341=emp[341],r342=emp[342],r343=emp[343],r344=emp[344],r345=emp[345],r346=emp[346],r347=emp[347],r348=emp[348],r349=emp[349],r350=emp[350],r351=emp[351],r352=emp[352],r353=emp[353],r354=emp[354],r355=emp[355],r356=emp[356],r357=emp[357],r358=emp[358],r359=emp[359],r360=emp[360],r361=emp[361],r362=emp[362],r363=emp[363],r364=emp[364],r365=emp[365],r366=emp[366],r367=emp[367],r368=emp[368],r369=emp[369],r370=emp[370],r371=emp[371],r372=emp[372],r373=emp[373],r374=emp[374],r375=emp[375],r376=emp[376],r377=emp[377],r378=emp[378],r379=emp[379],r380=emp[380],r381=emp[381],r382=emp[382],r383=emp[383],r384=emp[384],r385=emp[385],r386=emp[386],r387=emp[387],r388=emp[388],r389=emp[389],r390=emp[390],r391=emp[391],r392=emp[392],r393=emp[393],r394=emp[394],r395=emp[395],r396=emp[396],r397=emp[397],r398=emp[398],r399=emp[399],user=user)
	return render_template('home.html',form=form) 
	

#--------start-app-------------------------------------
if __name__ == '__main__':
	app.run()
