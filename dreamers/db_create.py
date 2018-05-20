#! /Users/jodth07/Env/dreamers/bin/python

from Application import db
# from .Application.dictionary.models import Dictionary
# from .Application.user.models import User
from Application.user.models import User
from Application.dictionary.models import Dictionary
from datetime import datetime


db.drop_all()
# def setup_db():
# create the database and the database table
db.create_all()


kabrit = Dictionary("kabrit", "Noun", 'A four legged animal', defined_user_id=1001)
kabrit.is_defined = True
kabrit.define_date =  datetime.now()
new_word = Dictionary('bèf', 'Noun', 'Another four legged animal', defined_user_id=1001)
new_word.is_defined = True
new_word.define_date =  datetime.now()
new_word2 = Dictionary('bèl', 'Adjective', 'a way to flirt with girls', defined_user_id=1001)
new_word2.is_defined = True
new_word2.define_date =  datetime.now()
new_word3 = Dictionary('pale', 'Verb', 'talking to people to annoy them', defined_user_id=1001)
new_word3.is_defined = True
new_word3.define_date =  datetime.now()


akwatik = Dictionary('akwatik', 'Adjective', 'Ki genyen relasyon avèk dlo', defined_user_id=1001 )
akwatik.antonyms = ['ayeryen']
akwatik.is_defined = True
akwatik.define_date =  datetime.now()

definitions = []
definitions.append('Ki genyen relasyon avèk dlo')
definitions.append('Ki viv, oswa devlope nan dlo')
definitions.append('Yon jwèt ki fèt nan dlo')


akwatik.definitions = definitions


areyen = Dictionary('areyen', 'Noun', 'yon atwopòd ki nan klas araknid la', defined_user_id=1001)
areyen.set_tags = ['animal', 'mamal', 'vivan']
areyen.scientific_name = "Araneae"
areyen.family = "Arachnida"
areyen.description=[
    'yon atwopòd ki nan klas araknid la ki genyen sis (6) pye. Gwoup sa a genyen anviwon 46 mil diferan espès dekri '
]
areyen.is_defined = True
areyen.define_date =  datetime.now()


adatoda = Dictionary('adatoda', 'Noun', 'Yon plant ki soti nan peyi Lenn ', defined_user_id=1001)
adatoda.scientific_name = 'Adhatoda vasica'
adatoda.set_tags = ['plant', 'pye bwa', 'vivan']
adatoda.family = 'Acanthaceae'
adatoda.other_names = ['Justicia adhatoda', 'Other Names']
adatoda.description = [
    'Yon plant ki soti nan peyi Lenn ak lòt peyi nan vwazinaj sa a.',
    'Yon plant ki pa wo di tou lè li fin grandi. Li ka rive jiska 7 pye edmi (2 mèt 50) wotè. Kèk fwa, yo kapab grandi rive jiska 6 mèt.',
    'Moun Itilize yo pou fè dekorasyon ak kloti.',
    'Fèy Adatoda kapab ede konbat anpil maladi ki konn atake plant ki ap pouse.',
    'Fèy yo kapab ede konsève fwi ak fèy yo mi pi vit san ensèk ak malady pa atake',
    'Fèy plant sa a long. Lè moun pile yo, fèy yo bay yon move san.',
    'Plant sa a bay yon flè ki tou blanch',
    'Fwi plan sa a genyen 2 santimèt longè. Chap fwi genyen 4 green ladan li.',
    'Plant sa a pouse kote ki fè cho ak kote ki fè fret. Moun kapab plante li soti bò lanmè rive jiska 1300 mèt. Plant sa a kapab pouse nan tè ki pòv, ki sèk, e ki onjan sale.'
]
adatoda.source = 'Plant ak Pyebwa tè d Ayiti'
adatoda.is_defined = True
adatoda.define_date =  datetime.now()


akajou_peyi = Dictionary('akajou peyi', 'Noun', 'Plant sa a soti nan karayib la.', defined_user_id=1001)
akajou_peyi.scientific_name = 'Swietania mahogani'
akajou_peyi.set_tags = ['plant', 'pye bwa', 'vivan']
akajou_peyi.family = 'Meliaceae'
akajou_peyi.other_names.append('akajou sendomeng')
akajou_peyi.other_names.append('Akajou')

akajou_peyi.description.append('Plant sa a soti nan karayib la. Kote ki pa ni twò cho, ni twò frèt.')
akajou_peyi.description.append('Yon gwo pyebwa ki ka rive jiska (60 pye) 20 mèt wotè lè li fin grandi.')
akajou_peyi.description.append('Bwa pye sa a se youn nan bwa ki pi bon pou fè mèb. Bwa sa di anpil, epi li dire. '
                               'Ou kapab itilize li tou pou fè dekorasyon, oswa pou fè  kèk konstriksyon ki bezwen bwa ki lou.')
akajou_peyi.description.append('Twon li pa twò long.')
akajou_peyi.description.append('Feyay li won, epi fèy yo vèt. Fèy pye sa a konpoze, yo chak genyen an 4 a 10 ti lòt fèy.'
                               ' Nan fen sezon sèch, tout ti fèy yo tonbe pou bay plas pou nouvo fèy reparèt nan sezon lapli a.')
akajou_peyi.description.append('Flè akajou a se flè nasyonal Repiblik Dominiken an.')
akajou_peyi.description.append('Fwi pyebwa sa a gen fòm kabòs. Chap fwi mezire anviwon 10 a 12 santimèt longè, epi yo '
                               'genyen anpil ti grenn mawon fonse ladan yo. Chak grenn sa yo, ki genyen yon ti zèl tou plat kole youn sou lòt')
akajou_peyi.description.append('Pye bwa sa a bezwen ant 800 e 1250 milimèt dlo pandan ane a, avèk yon sezon sèk. Li '
                               'prefere tè kalkè, tè ki gen wòch epi ki sèk.')
akajou_peyi.description.append('Pyebwa sa a grandi nan elevasyon ki pi ba pase 500 mèt, epi ki genyen anpil solèy.')

akajou_peyi.source = 'Plant ak Pyebwa peyi d’Ayiti'
akajou_peyi.is_defined = True
akajou_peyi.define_date =  datetime.now()


anana = Dictionary('anana', 'Noun', 'Yon plant ki soti an Amerik di sid, espesyalman', defined_user_id=1001)
anana.scientific_name = 'nanas comosus'
anana.family = 'Bromeliaceae'
anana.set_tags = ['plant', 'pye bwa', 'vivan']
anana.other_names = [
    'zanana'
]
anana.description = [
    'Yon plant ki soti an Amerik di sid, espesyalman, Brezil avèk Ajantin. Endyen ki te viv ann Amerik di sid yo te mennem plant sa a ann amerik santral la pou devlope li la.',
    'Yon plant èbase ki rete anpil nan tè a. Li genyen ti rasin ki pa antre twò fon nan tè a. Tij plant sa a kout, epi yo genyen anpil  ne ki kole youn ak lòt.',
    'Chè anana a santi bon anpil. Moun manje li, fè anpil pwodwi avèk li, tankou pafen, bagay pou manje oswa bwè. ',
    'Fwi anana a genyen ladan li yon pwodwi ki rele bwomelin ki ede dijesyon, oswa ki kapab ede fè anti enflamatwa.',
    'Fèy plant sa a sou tij yo. Fèy yo pwès, yo gen fòm goutyè avèk anpil ti dan sou kote yo. Fèy sa yo kapab mezire 1 mèt 50 nan longè avèk 5 santimèt nan lajè. Ansanm, yo fè yon touf. Epi nan mitan touf sa a fwi anana a soti. ',
    'Flè	Nou ka wè flè plant sa a sou po fwi anana a, yo sanble avèk yon plak (ki anviwon 100 a 200 sou chak fwi).',
    'Fwi pye sa a se yon reyinyon divès flè plant femèl la kote ògan femèl la pa kwaze avèk ògan mal yo. ',
    'Pye sa a devlope byen nan zòn ki cho, avèk nan zòn twopikal yo. Pou li byen leve, plant sa a bezwen tè ki lejè, ki enpe asid, epi ki pa kenbe dlo. Li bezwen anpil azòt ak potas. Li bezwen anviwon 1200 a 1500 milimèt dlo pandan ane a,  avèk anpil limyè solèy.',
    'Pye sa a nòmalman pa bay grenn. Alò anpil moun prepare rejè plant sa a epi replante yo, oswa plante kouwòn fwi anana a. Men pou li pouse byen, fòk moun nan kite yon bon mòso anana anba kouwòn nan.',
]
anana.source = 'Plant ak Pyebwa tè d Ayiti'
anana.is_defined = True
anana.define_date =  datetime.now()

jd = User('Olson', 'Dimanche', 'jodth09@gmail.com', 'Jd25390725', 'jodth07', 7000)
jd.email_confirmed = True
jd.email_confirmation_sent_date = datetime.now()
jd.email_confirmed_date = datetime.now()
jd.authenticated=True
jd.has_nick = True
#
db.session.add(jd)
db.session.add(areyen)
db.session.add(adatoda)
db.session.add(akajou_peyi)
db.session.add(akwatik)
db.session.add(anana)
db.session.add(kabrit)
db.session.add(new_word)
db.session.add(new_word2)
db.session.add(new_word3)


db.session.commit()

x_word = Dictionary.query.get(100001)
x_word.common_name = 'OJD'

# db.session.update(x_word)
db.session.commit()
    # return db


# ####### ######### ####### ####### ######### #### NOT WORK?
# DON'T FORGET TO ALTER                          #
# SEQUENCE ID'S OF USERS TO 1001                 #
# ALTER SEQUENCE users_id_seq RESTART WITH 1001; #
# AND WORDS TO  100001                           #
# ALTER SEQUENCE words_id_seq RESTART WITH 100001; #
# ####### ######### ####### ####### ######### ####
# UPDATE users SET _role='admin', _cleared=True, nick_name='jodth07',
# _has_nick = True, _clearance=7000 WHERE id=1001;
