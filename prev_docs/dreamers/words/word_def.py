from Application import db
# from .Application.dictionary.models import Dictionary
# from .Application.user.models import User
from Application.user.models import User
from Application.dictionary.models import Dictionary
from datetime import datetime

defined_user_id=1001
Sous = 'Plant ak Pyebwa tè d Ayiti'

Non = 'Kanèl'
Lot_Non = 'kannèl'
Tip = 'Plant'
Fanmi = 'Lauraceae'
Non_Syantifik = 'Cinnamomum zeylanicum'
Orijin = 'Plant sa a sòti an Srilanka avèk Lenn. Ou kapab jwenn li nan anpil peyi ki fè cho espesyalman peyi Oseyan Endyen yo.'
Deskripsyon = Orijin + 'Pye kanèl kapab grandi rive jiska 7 mèt wotè. '
Fey = 'Fey kanèl gen divès gwosè. Yo genyen at 3 a 5 gwo venn trè vizib sou yo. Jèn fèy yo gen yon koulè on jan wouj.'
Fle = 'Kanèl fè yon seri ti flè an grap ki blanch tire sou vèt. ' \
      'Fwi kanèl yo gen yon koulè mov fonse ki tire sou nwa. Chak fwi pote yon sèl grenn kanèl.  Grenn yo tou nwa e yo kapab mezire ant yon santimèt edmi a 3 santimèt longè. '
Izaj = 'Kòs pye kanèl la sèvi epis li ye.  Yo itilize epis sa a pou prepare anpil bagay tankou te, konfiti, kleren, wonm, dous, labouyi, chokola, elatriye. Yo fè remèd avèk li tou. Te kanèl bon pou pase vomisman, vant fè mal, endijesyon, elatriye.  Piga bay fanm ansent bwè te kanèl.'
Devlopman = 'Bon konsisyon pou grandi kanèl se chalè ak imidite. Kanèl pa ka sipòte sechrès twò lontan ni tè ki gen anpil wòch oubyen tè ki kenbe dlo ni tanperati ki varye twòp. Pyebwa sa a tou bezwen anpil lonbray sa ki fè yo plante li anba lòt  pi gwo pyebwa.  '
Repwodiksyon = 'Grenn kanèl yo sèvi pou fè plan. Yo fè plan avèk bouti pye kanèl  la tou. Yo kapab repwodwi kanèl tou ' \
               'pa makòtay. Grenn kanèl pouri vit. Li preferab pou simen grenn yo ant 3 a 4 jou aprè yo keyi epi seche anba lonbray. '
Lot_detay = 'Genyen plizyè lòt kalite pyebwa nan menm fanmi an ki bay kanèl tou.'

kannel = Dictionary(Non, "Noun", Deskripsyon, defined_user_id=defined_user_id )
kannel.sg_other_names = [Lot_Non]
kannel.source = 'http://www.tradewindsfruit.com/content/cinnamon.htm'
kannel.sub_category = Tip
kannel.sg_description = [Deskripsyon, Fey, Fle, Izaj, Devlopman, Repwodiksyon]
kannel.sg_scientific_name = Non_Syantifik
kannel.family = Fanmi
kannel.sg_other_info = [Lot_detay]
kannel.is_defined = True
kannel.define_date = datetime.now()
kannel.defined_user_id = defined_user_id

# =========  =========  =========  =========  =========  ========= #

Non = 'Kaswoz'
Lot_Non = 'kaswòz'
Tip = 'Plant'
Fanmi = 'Leguminosae-Cesalpiniaceae'
Non_Syantifik = 'Cassia javanica'
Orijin = 'Plant sa a sòti nan peyi Endonezi epesyalman zile Java.  Ou ap jwenn plant sa nan lòt peyi ki fè cho sou latè.  '
Deskripsyon = 'Kanpèch se yon pyebwa ak gwo fèy. Li kapab rive jiska 15 mèt wòte lè li fin grandi. Tij pyebwa sa a on jan tòdye epi kòs ki sou li a kale ki fè li sanble ke li genyen yon seri gwo plak sou li. '
Fey = 'Fey kaswoz yo se fèy konpoze. Chak fèy yo konpoze de 12 a 15 lòt ti fèy sou chak bò. Ti fèy say o tou won.'
Fle = 'Kaswoz fè flè an grap. Fle yo gen yon koulè woz e yo bay yon bon sant. Chak flè gen 5 petal. ' \
      'Pye kaswoz yo bay yon seri gous ki pandye. Gous sa yo long e yo won. Yo kapab mezire ant 30 a 60 santimèt longè. Nou jwenn grenn pye kaswoz anndan gous yo. Chak grenn gen konpatiman pa li. Grenn yo tou won avèk yon koulè mawon tire sou wouj. '
Izaj = 'Bwa koswoz se pa yon bwa ki di. Yo sèvi avèk li pou  fè poto, manch zouti, ak bwa pou boule. Yo sèvi ak li kòm' \
       ' brizvan nan travay  konsèvasyon anviwònmantal epi kòm parasòl pou plant ki pa ka pran anpil solèy. Kaswoz sèvi yon plant dekoratif tou pou bèl flè woz li fè lè li fleri. '
Devlopman = 'Pi bon kondisyon pou pye kanpèch se chalè avèk imidite. '
Repwodiksyon = 'Yo sèvi avèk grenn kaswoz pou fè plan pou plante.'

kaswoz = Dictionary(Non, "Noun", Deskripsyon, defined_user_id=defined_user_id )
kaswoz.sg_other_names = [Lot_Non]
kaswoz.sg_other_info = []
kaswoz.source = Sous
kaswoz.sub_category = Tip
kaswoz.sg_description = [Orijin, Deskripsyon, Fey, Fle, Izaj, Devlopman, Repwodiksyon]
kaswoz.sg_scientific_name = Non_Syantifik
kaswoz.family = Fanmi
kaswoz.is_defined = True
kaswoz.define_date = datetime.now()

# =========  =========  =========  =========  =========  ========= #

Non = 'Kasya'
Tip = 'Plant'
Fanmi = 'Leguminosea-Cesalpiniacea'
Non_Syantifik = 'Cassia siamea'
Orijin = 'Plant sa a sòti nan peyi sidès kontinan Azi . Ou kapab jwenn li nan lòt peyi tankou Lenn, Srilanka, Malezi ' \
         'avèk lòt peyi kote li fè cho.'
Deskripsyon = 'Kasya se yon plant ki te gen anpil enpòtans kòm espès foretyè.  Kounye a li plis sèvi kou plant dekoratif. Pye kasya kapab grandi rive 18 mèt wotè. Pyebwa sa a gen yon feyay toufe ki fè li yon bon lonbray. '
Fey = 'Fèy kanèl gen divès gwosè. Yo genyen at 3 a 5 gwo venn trè vizib sou yo. Jèn fèy yo gen yon koulè on jan wouj. '\
      'Kasya gen yon fèy konpoze. Chak fèy yo konpoze de 12 a 24 lòt ti fèy. '
Fle = 'Kasya fè yon seri grap flè jòn.  Fle sa yo mezire 3 santimèt dyamèt. ' \
      'Fwi pye kasya se yon gous  plat ki kapab mezire ant 5 a 25 santimèt longè.  Lè gous sa yo sèk, yo gen yon koulè mawon tire sou nwa.  Chak gous kapab genyen jiska 25 grenn anndan li. Grenn yo gen yon koulè mawon. '
Izaj = 'Moun sèvi avèk bwa kasya pou fè mèb, poto, chabon, men se yon bwa poudbwa pike anpil. Yo sèvi avèk li tou kòm ' \
       'brizvan. Kasya bay yon gwo lonbray, men fòk yo koupe tèt la lè li rive yon wotè pou li ka blayi lè li fin grandi. Moun fè siwo avèk flè kasya epi bèt manje fèy li yo.  '
Devlopman = 'Kasya pouse kote ki fè cho e ki pran anpil lapli. Se yon plant kapab sipòte sezon sechrès. Kasya pouse pi byen nan tè fon ki pa kenbe anpil dlo men li ap grandi nan nenpòt kalite tè asid, kalkè, ajil, oubyen ankò sab. '
Repwodiksyon = 'Yo sèvi avèk grenn nan pou plante pye kasya. Nou ka plante grenn yo direkteman nan tè kote nou vle yo grandi a oubyen fè pepinye avèk yo. '

kasya = Dictionary(Non, "Noun", Deskripsyon, defined_user_id=defined_user_id )
kasya.sg_other_info = []
kasya.source = Sous
kasya.sub_category = Tip
kasya.sg_description = [Orijin, Deskripsyon, Fey, Fle, Izaj, Devlopman, Repwodiksyon]
kasya.sg_scientific_name = Non_Syantifik
kasya.family = Fanmi
kasya.is_defined = True
kasya.define_date = datetime.now()

# =========  =========  =========  =========  =========  ========= #

Non = 'Kayimit'
Tip = 'Plant'
Fanmi = 'Sapotaceae'
Non_Syantifik = 'Chrysophyllum cainito'
Orijin = 'Plant sa a sòti nan peyi Amerik Santral avek zile Karayib yo.  Nou ap jwenn li tou nan peyi kontinan Afrik, Azi, ak Ostali.'
Deskripsyon = 'Genyen de kalite pye kayimit. Youn bay yon fwi vè pal ki dous anpil. Lòt la bay yon fwi mov ki santi bon anpil men ki pa twò dous. Pye yo kapab rive jiska 15 mèt wotè.'
Fey = 'Koulè fèy pye kayimit yo depan de ki bò fèy la bay. Bò fèy ki gade solèy la yo vèt fonse tandi ke bò ki gade tè a yo mawon dore.'
Fle = 'Kayimit fè flè an grap. Koulè? Gwosè? ' \
      'Fwi kayimit yo tou won e yo kapab genyen jiska 8 santimèt  dyamèt. Koulè po fwi yo vè pal ouswa mov. Konsa tou, chè fwi yo blanch ouswa mov depan de kiyès ant de kalite pye kayimit ki genyen yo. Po fwi  pako fin mi yo bay yon lèt tou blanch.' \
      'Nou jwenn grenn pye kayimit anndan fwi li yo. Chak fwi genyen 7 a 8 grenn ki (a)ranje an fòm yon etwal anndan fwi a. Sèlman 3 a 5 ladan yo ki ka leve lè yo plante yo.'
Izaj = 'Chè kayimit la bon pou manje konsa ounyen pou fè ji avèk patisri. Fwi kayimit yo bon pou fosfò, kalsyòm.'
Devlopman = 'Pi bon kondisyon pou pye kayimit se chalè avèk imidite. Kayimit bay pi bon donn nan tè ki fon e gra sinon li pa bezwen twò bon tè pou li develope men li pa tolere tè ki gen dlo chita.'
Repwodiksyon = 'Yo sèvi avèk grenn kayimit pou fè plan pou plante. Yo kapab grefe oubyen fè makòtay avèk li tou.'
Lot_detay = 'Genyen yon pye kayimit nan palè lakou Sansousi ki genyen anviron 200 an. Yo di Wa Henri Christophe te konn rann lajistis e pran repo anba pye l .'

kayimit = Dictionary(Non, "Noun", Deskripsyon, defined_user_id=defined_user_id )
kayimit.sg_other_names = [Lot_Non]
kayimit.source = Sous
kayimit.sub_category = Tip
kayimit.sg_description = [Orijin, Deskripsyon, Fey, Fle, Izaj, Devlopman, Repwodiksyon]
kayimit.sg_scientific_name = Non_Syantifik
kayimit.family = Fanmi
kayimit.sg_other_info = [Lot_detay]
kayimit.is_defined = True
kayimit.define_date = datetime.now()

# =========  =========  =========  =========  =========  ========= #

Non = 'Kenèp'
Tip = 'Plant'
Fanmi = 'Sapindaceae'
Non_Syantifik = 'Melicocca bijuga'
Orijin = 'Plant sa a sòti nan peyi Amerik Santral avèk peyi Karayib yo.  Nou jwenn li tou an Kolonbi avèk Venezyela. '
Deskripsyon = 'Kenèp se yon pyebwa ki kapab rive jiska 20 mèt wotè. ????'
Fey = 'Kenèp gen fèy konpoze ki vle di fèy yo fèt an fèy. Fey kenèp yo fèt avèk 4 lòt ti fèy. '
Fle = 'Kenèp fè flè an grap. Fle li yo piti anpil.  Koulè? Gwosè? Fle sa yo ka mal oubyen femèl. Fòk polèn flè mal ' \
      'yo polinize flè femèl yo pou pye kenèp la bay donn. Pye kenèp la kapab mal yon bò epi femèl lòt bò a. Lè pye ' \
      'kenèp an flè n ap jwenn anpil myèl sou flè mal yo. Fwi kenèp yo tou won e yo kapab mezire jiska 3 santimèt ' \
      'longè. Koulè po a  yo tou vèt. Chè fwi a gen yon koulè wòz ki ka tire sou jòn. Chak fwi genyen yon sèl grenn men li konn rive gen fwi ak de grenn tou.  Grenn sa yo gwo anpil pou gwòsè fwi a. '
Izaj = 'Chè  kenèp la bon pou manje konsa. Yo fè farin avèk nannan grenn kenèp ki sèk. Farin sa fè labouyi avèk lòt kalite patisri. Yo konn mete kenèp nan boutèy wonm oubyen kleren ak sik pou fè bwason. Kenèp gen anpil fè (0,93 miligram pa 100 gram) avèk fosfò (50,4 miligram pa 100 gram).'
Devlopman = 'Pi bon kondisyon pou leve kenèp se chalè. Li pa leve byen kote ki twò wo (kote ki depase 1000 mèt altitid).  Plant sa prefere tè tif oubyen tè wochez. '
Repwodiksyon = 'Kenèp pran pi byen si li grefe men yo sèvi avèk grenn yo pou fè pepinye tou. '
Lot_detay = 'Si yon moun manje twòp  kenèp, l ap sere l. '

kenep = Dictionary(Non, "Noun", Deskripsyon, defined_user_id=defined_user_id )
kenep.source = Sous
kenep.sub_category = Tip
kenep.sg_description = [Orijin, Deskripsyon, Fey, Fle, Izaj, Devlopman, Repwodiksyon]
kenep.sg_scientific_name = Non_Syantifik
kenep.family = Fanmi
kenep.sg_other_info = [Lot_detay]
kenep.is_defined = True
kenep.define_date = datetime.now()

# =========  =========  =========  =========  =========  ========= #

Non = 'Kiwi'
Tip = 'Plant'
Non_Syantifik = 'Actinidia sinensis'
Fanmi =	'Dileniaceae'
Orijin = 'Plant sa a sòti Lachin. Ou ap jwenn li nan lòt peyi tankou Japon, Nouvèl Zelann, avèk peyi kontinan ewòp yo.   '
Deskripsyon = 'Kiwi se yon lyann. Li popilè anpil nan peyi orijin li Lachin. Tij kiwi gen yon bann ti pwal dous ki kouvri tout kò li.  Fey avèk flè kiwi fè li yon plant atiran anpil. W ap jwenn plizyè diferan kalite. Chak nan kalite yo gen yon trè diferan. '
Fey = ' bay yon fwi ki alonje, fwi kalite sa a gen anpil vitamin C'
Fle = ' bay yon gwo fwi ki santi bon e li donnen pi lontan pase Abbot ak Bruno. Se plis kalite sa a tou yo vann nan.' \
      ' donnen plis pase lòt kalite yo. Kiwi fè yon bann gwo fèy vèt an fòm kè. Li fè gwo flè tout. Fle sa yo kapab gen yon koulè blanch ou jòn depan de si se yon pye mal oubyen femèl. Fle pye mal yo blanch avèk yon kè jòn a koz de polen flè mal yo pote tandi ke flè pye femèl kiwi yo tout blanch. Pye kiwi bay yon fwi alonje menm jan avèk ze poul. Po fwi sa yo gen yon koulè vèt fonse avèk yon bann ti pwal sou li.  Fwi yo gen yon chè ki kapab yon koulè vèt klè oubyen jòn. Kè kiwi pa fin menm koulè avèk chè a. Otou kè a nou jwenn yon bann ti grenn tou nwa. '
Izaj = 'Fey avèk flè pye kiwi fè li yon plant ki trè atiran ki fè yo itilize l kòm plant dekoratif.  Yo fè konsèv, konfiti, diven avèk fwi pye kiwi a an menm tan ke yo manje l. Kiwi gen anpil vitamin C, jiska 300 miligram pa 100 gram fwi. Anplis, li gen fòsfò, kalsyòm, ak fè tou. '
Devlopman = 'Pi bon kondisyon pou pye kiwi se fredi. Menm si fredi fè pyebwa sa a byen, twòp fredi ap touye l. Kiwi grandi pi byen nan tè fre e gra ki pa kenbe dlo. '
Repwodiksyon = 'Yo sèvi avèk grenn kiwi a pou fè plan pou plante. Lè se grenn kiwi a yo itilize pou plante li, nou pap konnen si se yon pyen mal oubyen femèl ke tout otan pye li pa ko fleri. Yo repwowi kiwi tou pa makòtay oubyen grèfay. Si makòtay la fèt sou yon pye mal, plant la nap vin yon pye mal epi menm jan si li fèt sou yon pye femèl plant ap vin yon femèl. Pye kiwi bay donn 3 a 4 ane aprè yo plante l, men li bay pi bon donn apre 7 a 8 an. '
Lot_detay = 'Kiwi pa yon plant moun byen konnen an Ayiti. W ap jwenn li nan zòn Kenskòf kote yo kòmanse kiltive li. '

kiwi = Dictionary(Non, "Noun", Deskripsyon, defined_user_id=defined_user_id )
kiwi.sg_other_names = [Lot_Non]
kiwi.sub_category = Tip
kiwi.sg_other_info = [Lot_detay]
kiwi.family = Fanmi
kiwi.sg_description = [Orijin, Deskripsyon, Fey, Fle, Izaj, Devlopman, Repwodiksyon]
kiwi.sg_scientific_name = Non_Syantifik
kiwi.source = 'http://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:60458895-2'
kiwi.is_defined = True
kiwi.define_date = datetime.now()

# =========  =========  =========  =========  =========  ========= #

Non = 'Karanbòl'
Tip = 'Plant'
Fanmi = 'Oxalidaceae'
Non_Syantifik = 'Averroha carambola'
Orijin = 'Plant sa a sòti an Malezi avèk Endonezi. Ou kapab jwenn li nan lòt peyo tankou Lenn, Srilanka, ak Lachin.  '
Deskripsyon = Orijin
Fey = 'Fey kanèl gen divès gwosè. Yo genyen at 3 a 5 gwo venn trè vizib sou yo. Jèn fèy yo gen yon koulè on jan wouj.'
Fle = 'Kanèl fè yon seri ti flè an grap ki blanch tire sou vèt. ' \
      'Fwi kanèl yo gen yon koulè mov fonse ki tire sou nwa. Chak fwi pote yon sèl grenn kanèl.  Grenn yo tou nwa e yo kapab mezire ant yon santimèt edmi a 3 santimèt longè. '
Izaj = 'Kòs pye kanèl la sèvi epis li ye.  Yo itilize epis sa a pou prepare anpil bagay tankou te, konfiti, kleren, wonm, dous, labouyi, chokola, elatriye. Yo fè remèd avèk li tou. Te kanèl bon pou pase vomisman, vant fè mal, endijesyon, elatriye.  Piga bay fanm ansent bwè te kanèl.'
Devlopman = 'Bon konsisyon pou grandi kanèl se chalè ak imidite. Kanèl pa ka sipòte sechrès twò lontan ni tè ki gen anpil wòch oubyen tè ki kenbe dlo ni tanperati ki varye twòp. Pyebwa sa a tou bezwen anpil lonbray sa ki fè yo plante li anba lòt  pi gwo pyebwa.  '
Repwodiksyon = 'Grenn kanèl yo sèvi pou fè plan. Yo fè plan avèk bouti pye kanèl  la tou. Yo kapab repwodwi kanèl tou ' \
               'pa makòtay. Grenn kanèl pouri vit. Li preferab pou simen grenn yo ant 3 a 4 jou aprè yo keyi epi seche anba lonbray. '
Lot_detay = 'Genyen plizyè lòt kalite pyebwa nan menm fanmi an ki bay kanèl tou.   '

karanbol = Dictionary(Non, "Noun", Deskripsyon, defined_user_id=defined_user_id )
karanbol.sub_category = Tip
karanbol.sg_scientific_name = Non_Syantifik
karanbol.family = Fanmi
karanbol.sg_description = [Deskripsyon, Fey, Fle, Izaj, Devlopman, Repwodiksyon]
karanbol.sg_other_info = [Lot_detay]
karanbol.source = 'http://www.tradewindsfruit.com/content/cinnamon.htm'
karanbol.is_defined = True
karanbol.define_date = datetime.now()

# =========  =========  =========  =========  =========  ========= #

Non =	"Koupye"
Tip =	"Plant"
Non_Syantifik =	"Portulaca oleracea L."
Fanmi= '  	Portulacaceae'
Orijin =	"Plant sa a sòti nan peyi kontinan Ewòp avèk Lachin. W ap jwenn li patou sou latè jounen jodi a."
Deskripsyon =	'Koupye se yon plant ebase. Fason plant sa devlope depan de ki kote yo plante li a.  Koupye gen yon tij mou ki kouri atè. Tij la bay yon ti dlo lè yo kraze l.'
Fey = ' Fey koupye grandi an pè, youn chak bò tij la. Pwent fèy to awondi. Fey yo mezire 2-a-3 santimèt lajè e ' \
            '3-a-5 santimèt longè. Koupye bay yon bann ti flè tou jòn nan pwent ti branch yo. Koupye fleri tout lane a men flè li yo pa dire plis pase yon jou.'
Fle	= 'Koupye fè yon seri ti fwi won avèk yon bann ti grenn nwa anndan yo. Fwi yo kapab mezire 4-a-8 santimèt longè. Grenn yo menm mezire anviwon 0,5 milimèt dyamèt.'
Izaj =	'Yo kiltive koupye kòm legim oubyen remèd. Li bon pou dijesyon. Chak 100 gram koupye genyen 420-a-700 miligram vitamin C.'
Devlopman =	'Pi bon kondisyon pou plant sa a se solèy ak chalè men l ap pouse nan tout kalite tè.'
Repwodiksyon =	'Yo sèvi avèk grenn oubyen plan koupye pou fè repwodiksyon.'
Lot_detay =	'Koupye ka aji tankou raje ki touye lòt plant.'

koupye = Dictionary(Non, "Noun", Deskripsyon, defined_user_id=defined_user_id )
koupye.sg_other_names = [Lot_Non]
koupye.sub_category = Tip
koupye.sg_scientific_name = Non_Syantifik
koupye.family = Fanmi
koupye.sg_description = [Orijin, Deskripsyon, Fey, Fle, Izaj, Devlopman, Repwodiksyon]
koupye.sg_other_info = [Lot_detay]
koupye.source = 'http://publish.plantnet-project.org/project/plantinvasivekruger/collection/collection/synthese/details/POROL'
koupye.is_defined = True
koupye.define_date = datetime.now()
# =========  =========  =========  =========  =========  ========= #
