#! /Users/jodth07/Env/dreamers/bin/python

from Application import db
# from .Application.dictionary.models import Dictionary
# from .Application.user.models import User
from Application.user.models import User
from Application.dictionary.models import Dictionary
from Application.blog.models import Blog
from Application.article.models import Article
from datetime import datetime

defined_user_id = 1001
Sous = 'Plant ak Pyebwa tè d Ayiti'

db.drop_all()
# def setup_db():
# create the database and the database table
db.create_all()

Non= "Arawout"
Lot_Non= "Mazonbèl"
Tip= "Plant"
Fanmi= "Marantaceae"
Non_Syantifik= "Maranta arundinacea L"
Orijin= "Plant sa a sòti an Amerik-di-Sid. Ou kapab jwenn li tou nan anpil lòt rejyon twopikal tankou zile Awayi yo, " \
        "Afrik-di-Sid, Azi, ak Ostrali."
Deskripsyon= "Arawout se yon plant vivas. Genyen 2 kalite ladan l. Youn genyen yon rizòm ki long, lòt la yon rizòm " \
             "ki kout. Rizòm sa yo toujou an fòm yon flèch ki kouvri ak yon bann ti kal an fòm triyang. Plant sa a " \
             "kapab fleri pandan plizyè ane youn dèyè lòt. Pati tij la ki anwo tè a pa twò di. Li kapab rive  jiska 2 "\
             "mèt wotè lè fin grandi."
Fey= "Fèy li yo gen yon koule vèt fonse avèk yon fòm alonje."
Fle= "Arawout fleri yon fwa pa ane. Flè yo gen yon koulè tou blan e yo pa gwo. " \
     "Fwi ak Grenn	Fwi plant sa a grandi anba tè a. Yo gen fòm yon gous maskriti ak yon sentimèt dyamèt. Chal green " \
     "yo vlope nan yon ti chè ki tou jòn."
Izaj= "Moun fè lanmidon ak farin avèk rezòm arawout. Yo itilize farin sa pou fè krèp, gato, labouyi, biskwit, " \
      "elatriye.  Yo konn bay ti bebe labouyi arawout tou nan plas lèt manman. Moun bouyi fèy arawout pouf è yon " \
      "tizann ki bon pou moun ki soufri mal gòj ak moun ki anwe. Yo sèvi ak li tou  nan endistri chokola, " \
      "preparasyon potaj."
Devlopman= "Plan sa a pouse byen nan tè plenn ki imid ki gen enpe lonbray avèk nan mòn ki fre. Yo plante l nan tè " \
           "lejè sablèz li kenbe ase imitdite."
Repwodiksyon= "Yo plante arawout menm jan avèk pòmdetè. Antere mòso rizòm yo,  oubyen grenn arawout la, ant 2 " \
              "bit anviwon yon mèt apa."


arawout = Dictionary(Non, "Noun", Deskripsyon, defined_user_id=defined_user_id )
arawout.sg_other_names = [Lot_Non]
arawout.sg_other_info = []
arawout.source = Sous
arawout.sub_category = Tip
arawout.sg_description = [Orijin, Deskripsyon, Fey, Fle, Izaj, Devlopman, Repwodiksyon]
arawout.sg_scientific_name = Non_Syantifik
arawout.family = Fanmi
arawout.is_defined = True
arawout.define_date = datetime.now()
arawout.defined_user_id = defined_user_id

db.session.add(arawout)
# =========  =========  =========  =========  =========  ========= #

Non='Ave'
# Lot_Non='??'
Tip='plant'
Fanmi='Phytolacaceae'
Non_Syantifik='Petiveria alliacea L.'
Orijin='Plant sa sòti an Amerik-Santral avèk zile Karayib yo. Ou kapab jwenn li tou nan anpil lòt rejyon twopikal tankou Amerik-di-Sid, Afrik, ak Azi.'
Deskripsyon='Ave se yon plant èbase. Li kapab fleri 60 jou aprè yo plante li. Plant lan genyen yon tij principal ki' \
            ' fè anpil ti branch trè fen men pati tij la ki pre avèk tè a di anpil e li kapab grandi rive  jiska 1 mèt wotè. Li pwodwi yon lwil esansyèl ki fè li santi fò anpil. Gras a sistèm rasin plant sa a, li kapab repouse fasilman si yo koupe pye a. Yo konsidere plant sa tankou yon plant nwizib anpil kote a koz de sa.'
Fey='Fèy li yo gen yon koule vèt fonse avèk yon fòm alonje.'
Fle='Ave fleri how many times per year? Li bay yon bann ti flè blanch nan pwent branch li yo ki genyen yon longè ant ' \
    '10 a 40 santimèt. Fwi ak Grenn	Fwi plant sa a rive 8 milimèt longè. Lè fwi yo sèk, yo kapab genyen ant 1 a 6 kwòk nan pwent yo ki pèmèt yo kole sou rad moun.'
Izaj='Nan tan lontan, Endyen peyi Brezil yo te konn itilize ave pou prepare yon pwazon yo rele kira pou pase nan pwent flèch yo lè yo pral nan lagè, lachas, ak lapèch. Kira se yon anestezi. Moun konsidere ave tankou yon plant mistik. Yo fè beny avèk fèy li yo pou kwape? move espri sou moun. Yo konn lave objè, tankou bato, avèk li tou. Moun fè anpil remèd avèk fèy ak rasin ave. Remèd pou maldan, maltèt, lafyèv, sinizit, lagal, rimatis elatriye. Ji fèy ave a kapab sèvi antiseptik pou maleng e li bay yon pwodwi chimik ki rele nitrat potasyòm ki bon pou moun ki gen difikilte pou pipi. Atansyon, te fèy oubyen rasin ave kapab fè fanm ansent avòte.'
Devlopman='Plant sa a gen yon sistèm rasin ki pèmèt li pran trè byen nan divès kondisyon.'
Repwodiksyon='Itilize grenn nan pou prepare pepinyè ave oubyen yon ti bout branch ak ne ki pa di epi plante plan.'


ave = Dictionary(Non, "Noun", Deskripsyon, defined_user_id=defined_user_id )
# ave.sg_other_names = [Lot_Non]
ave.sg_other_info = []
ave.source = Sous
ave.sub_category = Tip
ave.sg_description = [Orijin, Deskripsyon, Fey, Fle, Izaj, Devlopman, Repwodiksyon]
ave.sg_scientific_name = Non_Syantifik
ave.family = Fanmi
ave.is_defined = True
ave.define_date = datetime.now()
ave.defined_user_id = defined_user_id

db.session.add(ave)
# =========  =========  =========  =========  =========  ========= #

Non= 'Bayawonn'
# Lot_Non= ''
Tip= 'Plant'
Fanmi= 'Leguminosae-Mimosaceae'
Non_Syantifik= 'Prosopis juliflora'
Orijin= 'Plant sa a sòti Meksik, Amerik-di-Sid, ak Karayib la. Ou kapab jwenn li tou nan wès peyi Etazini, Azi, Afrik ak Ostrali.'
Deskripsyon= 'Bayawonn se yon pyebwa ki di anpil avèk pikan byen long sou tout kò li. Kounye a, yo devlope kèk kalite '\
             'bayawonn ki pa genyen pikan ditou. Pyebwa sa a gen yon twon ki tòdye avèk yon kè tou nwa. Li kapab rive'\
             ' jiska 12 mèt wotè lè li fin grandi.'
Fey= 'Sou gwo branch pye bayawonn nan, genyen yon seri lòt ti branch tou kout. Nou jwenn fèy pyebwa a sou ti branch sa'\
     ' yo. Fèy li yo se fèy konpoze ki kapab mezire jiska 7,5 santimèt longè. Chak gwo fèy sa yo konpoze de 12 a 58 lòt'\
     ' ti fèy pi piti.  Yo genyen yon koule vèt klè avèk yon fòm ki yon tijan oval.'
Fle= 'Flè bayawonn sanble avèk zepi. Yo genyen yon koulè jòn. ' \
     'Fwi ak Grenn	Bayawonn bay yon fwi ki long e ki pa ouvri lè li sèk. Fwi yo kapab mezire ant ant 8 a 25 santimèt' \
     ' longè.  Fwi sa yo se yon gous ki genyen anpil to grenn ladan yo. Grenn yo vini vlope nan yon ti chè jòn annda fwi a. Chè a genyen yon bon sant bon ak yon ti gou dous.'
Izaj= 'Bwa bayawonn nan di anpil e li pa pouri fasil. Yo sèvi avèk li pou batiman kay, ray tren, chabon, travay chapant ak ebenis.  Fèy ak gous bayawonn lan sèvi kòm manje bèt. Moun moulen grenn bayawonn nan pou fè yon farin ki genyen jiska 65 pousan pwoteyin. Yo sèvi ak farin sa pou bonbon, gato, elatriye. Flè bayawonn nan li menm bay siwo. ' \
      'Yo sèvi avèk plant sa a tout pou sekouri tè ravaje ak lawozyon sitou nan zòn ki sèch.'
Devlopman= 'Bayawonn pouse kote ki fè cho, ki sèk, e ki resevwa ant 150 a 750 milimèt lapli pa an. Li pouse byen nan tè woche, sable, ou ankò sale.'
Repwodiksyon= 'Grenn bayawonn nan sèvi pou fè pepinyè.'

bayawonn = Dictionary(Non, "Noun", Deskripsyon, defined_user_id=defined_user_id )
# bayawonn.sg_other_names = [Lot_Non]
bayawonn.sg_other_info = []
bayawonn.source = Sous
bayawonn.sub_category = Tip
bayawonn.sg_description = [Orijin, Deskripsyon, Fey, Fle, Izaj, Devlopman, Repwodiksyon]
bayawonn.sg_scientific_name = Non_Syantifik
bayawonn.family = Fanmi
bayawonn.is_defined = True
bayawonn.define_date = datetime.now()
bayawonn.defined_user_id = defined_user_id

db.session.add(bayawonn)
# =========  =========  =========  =========  =========  ========= #

Non='Bazilik'
# Lot_Non=''
Tip='Plant'
Fanmi='Lamiaceae'
Non_Syantifik='Ocimum basilicum L.'
Orijin='Plant sa a sòti an Lenn. Ou kapab jwenn li nan tout peyi ki fè cho espesyalman peyi kontinan Afrik yo.'
Deskripsyon='Bazilik se yon plant èbase. Genyen de kalite bazilik. Youn rele Ocimum basilicum L. Lòt la rele Ocimum ' \
            'minimum L. Yo rele kalite sa a tou ti bazilik paske fèy li yo pi piti. Fèy plant sa a podwi yon lwil esansyèl ki rele estragòl. Tij ak branch yo onjan pi di nan baz plant lan. Li kapab rive jiska 60 santimèt wotè lè li fin grandi.'
Fey='Genyen de kalite bazilik. Youn rele Ocimum basilicum L. Fèy kalite sa a long. Yo mezire ant 2 a 5 santimèt longè. Lòt la rele Ocimum minimum L. Yo rele kalite sa a tou ti bazilik paske fèy li yo pi piti. Yo mezire ant 1 a 2 santimèt longè. Fèy kalite sa a pa santi bon menm jan ak lòt kalite bazilik la.'
Fle='Flè yo parèt nan pwent branch bazilik la e yo tou blanch.  Flè li yo èmafwodit, sa ki vle di, nan menm flè a, ' \
    'genyen ògàn mal ak  ògàn femèl. Fwi ak Grenn	*Information missing'
Izaj='Bazilik se yon plant awomatik. Li santi bon nan tout kò li. Moun sèvi avèk li pou fè te ak remèd. Yo fè epis, salad, chanpou  avèk li tou.'
Devlopman='*Information missing.'
Repwodiksyon="Grenn bazilik yo sèvi pou fè pepinyè (plantil). Yo fè plantil avèk ti bout branch ki pa twò di yo tou.'Plan' is commonly used to describe the early seedling stage  to be planted"
Lot_detay='Bazilik se yon plant mistik an Ayiti. Anpil moun netwaye kay yo pral abite pou la premyè fwa avèk dlo fèy bazilik. Yo konn fè beny avèk li tou.'

bazilik = Dictionary(Non, "Noun", Deskripsyon, defined_user_id=defined_user_id )
# bazilik.sg_other_names = [Lot_Non]
bazilik.sg_other_info = []
bazilik.source = Sous
bazilik.sub_category = Tip
bazilik.sg_description = [Orijin, Deskripsyon, Fey, Fle, Izaj, Devlopman, Repwodiksyon]
bazilik.sg_scientific_name = Non_Syantifik
bazilik.family = Fanmi
bazilik.sg_other_info = [Lot_detay]
bazilik.is_defined = True
bazilik.define_date = datetime.now()
bazilik.defined_user_id = defined_user_id

db.session.add(bazilik)
# =========  =========  =========  =========  =========  ========= #

Non='choublak'
Lot_Non='ibiskis'
Tip='plant'
Fanmi='Malvaceae'
Non_Syantifik='Hibiscus rosu-sinensis'
Orijin='Yon plant ki soti nan kontinan azi. Li popilè anpil nan zòn ki fè cho. Genyen anpil diferan kalite choublak. Plis pase 5000 nan peyi Awayi, avèk plis pase 200 kalite nan karayib yo.'
Deskripsyon='Yon plant ki pa twò wo, li pa depase plis pase de (4) mèt wotè. Epi an Ayiti, ki fè flè pandan tout ane a, oswa nan prentan, nan anpil lòt zòn. '
Fey='Fèy plant sa a gen yon fòm oval, avèk anpil ti dan sou kote li. Fèy yo devlope swa nan zesèl lòt fèy, oswa nan pwent branch bwa pyebwa a. '
Fle='Flè plant sa a kapab senp, oswa doub. Flè yo kapab genyen plizyè koulè diferan, tankou blan, jòn, woz, wouj, somon. Nan mitan flè sa yo, gen anpil etamin (ògan mal flè a) tou jòn.'
Izaj='Moun itilize fèy plant sa a kòm manje pou bèt. Yo itilize pyebwa a pou konbat ewozyon. Lè ou tranpe flè (oswa/ak fèy) nan dlo, li bay yon dlo glise moun itilize tankou champou pou lave cheve.' \
     'Flè choublak ki wouj la genyen ladan li anpil vitamin C. Nou sèvi avèk li lè nou ap fè tizann pou grip ak tous. '
Devlopman='Plant sa a kapab devlope soti bò lanme rive nan mòn jiska anviwo 700 mèt altitid. E gen kote li kapab grandi nan altitid ki 1000 mèt.'
Repwodiksyon='Pou ou fè li grandi, moun bezwen jis blante bouti ki prepare ak branch yo pou plant ki genyen fèy senp yo. Pou plant ki genyen fèy doub yo, ou kapab itilize grefay anplis boutiray la. '
Lot_detay='Flè nasyonal il Awayi, peyi Malezi avèk Lachin'

choublak = Dictionary(Non, "Noun", Deskripsyon, defined_user_id=defined_user_id )
choublak.sg_other_names = [Lot_Non]
choublak.sg_other_info = []
choublak.source = Sous
choublak.sub_category = Tip
choublak.sg_description = [Orijin, Deskripsyon, Fey, Fle, Izaj, Devlopman, Repwodiksyon]
choublak.sg_scientific_name = Non_Syantifik
choublak.family = Fanmi
choublak.sg_other_info = [Lot_detay]
choublak.is_defined = True
choublak.define_date = datetime.now()
choublak.defined_user_id = defined_user_id

db.session.add(choublak)
# =========  =========  =========  =========  =========  ========= #

Non = 'Kalbas'
Tip = 'Plant'
Fanmi = 'biynoniaceae'
Non_Syantifik = 'Crescentia cujete L.'
Orijin = 'Plant sa a sòti Meksik, Brezil, Ajantin, avèk Etazini. Ou kapab jwenn li tou nan peyi kontinan Afrik ak Azi.  '
Deskripsyon = 'Kalbas se yon pyebwa ki pa gen anpil branch. Li bay yon fwi ki kapab gen plizyè fòm selon kalite pye ' \
              'kalbas la. Pye kalbas la kapab rive jiska 10 mèt wotè lè li fin grandi.  '
Fey = 'Kalbas gen yon feyay ouvè e byen laj.  Yo genyen yon koulè vèt klè. Fèy ki grandi sou ti branch pye kalbas yo pa gen petyòl. '
Fle = 'Kalbas fleri tout lane a. Flè li yo grandi sou kò pye bwa a avèk gwo branch li yo e yo kapab mezire ant 5 a 6 ' \
      'santimèt lajè. Yo gen fòm yon klòch ak yon koulè jòn ki tire sou vèt. Fwi ak Grenn	Fwi pye kalbas grandi sou ' \
      'kò pye kalbas la. Yo gen yon po ki di e ki fen e yo kapab genyen  diferan fòm. Sèten kalite bay yon fwi tou won ki kapab mezire jiska 40 santimèt dyamèt. Sèten lòt, tankou kalbas Matinik, bay yon fwi alonje tankou ze poul. Gen sèten kalite kalbas mawon tou ki bay yon fwi ki tou piti. Anndan fwi pye kalbas la genyen yon chè tou blanch (kaka kalbas) kote nou jwenn yon bann ti grenn nwa tou plat ki kapab mezeri jiska 6 milimèt longè.'
Izaj = 'Fwi pye kalbas yo gen anpil itilite. Po fwi kalbas la sèvi po, kwi, ak rezèv dlo lè yo retire kaka kalbas la epi seche po a.  Yo pentire li fè dekorasyon, valiz, elatriye. Yo sèvi ak bwa kalbas la pou fè manch zouti. Yo sèvi ak kalbas pou fè remèd pou plizyè maladi tankou dyare, tètfèmal, idwopizi, doulè, et latriye.  '
Devlopman = 'Pi bon kondisyon pou kalbas se kote ki bay anpil lapli, ki pa twò imid ni twò sèk. Kalbas pouse prèske nan nenpòt kalite tè men li pa tolere tè jele.'
Repwodiksyon = 'Yo sèvi ak ni grenn kalbas ni bouti kalbas pou fè plan pou plante. '
Lot_detay = 'Kalbas se yon plant mistik an Ayiti. Anpil moun netwaye kay yo pral abite pou la premyè fwa avèk dlo fèy bazilik. Yo konn fè beny avèk li tou.'

kalbas = Dictionary(Non, "Noun", Deskripsyon, defined_user_id=defined_user_id )
# kalbas.sg_other_names = [Lot_Non]
kalbas.sg_other_info = []
kalbas.source = Sous
kalbas.sub_category = Tip
kalbas.sg_description = [Orijin, Deskripsyon, Fey, Fle, Izaj, Devlopman, Repwodiksyon]
kalbas.sg_scientific_name = Non_Syantifik
kalbas.family = Fanmi
kalbas.sg_other_info = [Lot_detay]
kalbas.is_defined = True
kalbas.define_date = datetime.now()
kalbas.defined_user_id = defined_user_id

db.session.add(kalbas)
# =========  =========  =========  =========  =========  ========= #

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

db.session.add(kannel)
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

db.session.add(kaswoz)
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

db.session.add(kasya)
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

db.session.add(kayimit)
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

db.session.add(kenep)
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

db.session.add(kiwi)
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

db.session.add(karanbol)
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

db.session.add(koupye)
# =========  =========  =========  =========  =========  ========= #


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
akwatik.sg_antonyms = ['ayeryen']
akwatik.is_defined = True
akwatik.define_date =  datetime.now()
akwatik.sg_definitions = ['Ki genyen relasyon avèk dlo','Ki viv, oswa devlope nan dlo','Yon jwèt ki fèt nan dlo']
# =========  =========  =========  =========  =========  ========= #


areyen = Dictionary('areyen', 'Noun', 'yon atwopòd ki nan klas araknid la', defined_user_id=1001)
areyen.sg_tags = ['animal', 'mamal', 'vivan']
areyen.scientific_name = "Araneae"
areyen.family = "Arachnida"
areyen.sg_description=[
    'yon atwopòd ki nan klas araknid la ki genyen sis (6) pye. Gwoup sa a genyen anviwon 46 mil diferan espès dekri '
]
areyen.is_defined = True
areyen.define_date =  datetime.now()


adatoda = Dictionary('adatoda', 'Noun', 'Yon plant ki soti nan peyi Lenn ', defined_user_id=1001)
adatoda.scientific_name = 'Adhatoda vasica'
adatoda.sg_tags = ['plant', 'pye bwa', 'vivan']
adatoda.family = 'Acanthaceae'
adatoda.sg_other_names = ['Justicia adhatoda', 'Other Names']
adatoda.sg_description = [
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
akajou_peyi.sg_tags = ['plant', 'pye bwa', 'vivan']
akajou_peyi.family = 'Meliaceae'
akajou_peyi.sg_other_names = ['akajou sendomeng', 'Akajou']
akajou_peyi.sg_description = ['Plant sa a soti nan karayib la. Kote ki pa ni twò cho, ni twò frèt.', 
                              'Yon gwo pyebwa ki ka rive jiska (60 pye) 20 mèt wotè lè li fin grandi.',
                              'Bwa pye sa a se youn nan bwa ki pi bon pou fè mèb. Bwa sa di anpil, epi li dire. '
                               'Ou kapab itilize li tou pou fè dekorasyon, oswa pou fè  kèk konstriksyon ki bezwen bwa ki lou.',
                              'Twon li pa twò long.',
                              'Feyay li won, epi fèy yo vèt. Fèy pye sa a konpoze, yo chak genyen an 4 a 10 ti lòt fèy.'
                               ' Nan fen sezon sèch, tout ti fèy yo tonbe pou bay plas pou nouvo fèy reparèt nan sezon lapli a.',
                              'Flè akajou a se flè nasyonal Repiblik Dominiken an.',
                              'Fwi pyebwa sa a gen fòm kabòs. Chap fwi mezire anviwon 10 a 12 santimèt longè, epi yo '
                               'genyen anpil ti grenn mawon fonse ladan yo. Chak grenn sa yo, ki genyen yon ti zèl tou plat kole youn sou lòt',
                              'Pye bwa sa a bezwen ant 800 e 1250 milimèt dlo pandan ane a, avèk yon sezon sèk. Li '
                               'prefere tè kalkè, tè ki gen wòch epi ki sèk.',
                              'Pyebwa sa a grandi nan elevasyon ki pi ba pase 500 mèt, epi ki genyen anpil solèy.']

akajou_peyi.source = 'Plant ak Pyebwa peyi d’Ayiti'
akajou_peyi.is_defined = True
akajou_peyi.define_date =  datetime.now()


anana = Dictionary('anana', 'Noun', 'Yon plant ki soti an Amerik di sid, espesyalman', defined_user_id=1001)
anana.scientific_name = 'nanas comosus'
anana.family = 'Bromeliaceae'
anana.sg_tags = ['plant', 'pye bwa', 'vivan']
anana.sg_other_names = [
    'zanana'
]
anana.sg_description = [
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
anana.define_date = datetime.now()
# =========  =========  =========  =========  =========  ========= #


article_1 = Article("Dreaming of land and oil palms", "Now in almost every available spot with soil and good light a "
                                                      "tree is growing. All except some locations too close to the "
                                                      "school or church where group activities need open space.", 1001)
article_1.author = "John Davis"
article_1.define_date = datetime.now()
article_1.is_defined=True
article_1.description = [ "In two weeks we will celebrate 5 years of living here in Fauche. Cory started planting trees"
                          " and plants as soon as he considered our moving here, months before we actually moved North.",
                          "Now in almost every available spot with soil and good light a tree is growing. All except "
                          "some locations too close to the school or church where group activities need open space.",
                          "So now where to plant. My very generous husband continues to give away trees throughout Haiti.",
                           "The bare hillside to the North of our house looks like an ideal place for him to plant. He would like to get permission from an owner to plant a demonstration garden and trees up on this hillside currently used for pasture.",
                          "It would be high enough for folks to notice from the road and see what a difference planting trees can make rather than root crops that lead to soil erosion or overgrazed pasture, both of which lead to severe soil erosion with our 100+ inches of rain each year.",
                          "He would be able to keep an eye on the field from our house. And it would not be a far hike to visit and work in the field.",
                          "To start would probably be high quality cut-and-carry pasture plants like elephant grass, mulberry and tree marigold.",
                          "Fruit, bamboo and lumber trees can also be planted for longer term production. It seems like sugar cane would produce in sunny locations and would hold the soil."
                        ]
