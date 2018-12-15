from dictionary.models import Word
from django.utils import timezone

Deskripsyon= "Arawout se yon plant vivas. Genyen 2 kalite ladan l. Youn genyen yon rizòm ki long, lòt la yon rizòm ki kout. Rizòm sa yo toujou an fòm yon flèch ki kouvri ak yon bann ti kal an fòm triyang. Plant sa a kapab fleri pandan plizyè ane youn dèyè lòt. Pati tij la ki anwo tè a pa twò di. Li kapab rive  jiska 2 mèt wotè lè fin grandi."
Fèy= "Fèy li yo gen yon koule vèt fonse avèk yon fòm alonje."
Flè= "Arawout fleri yon fwa pa ane. Flè yo gen yon koulè tou blan e yo pa gwo."
Fwi_ak_Grenn ="Fwi plant sa a grandi anba tè a. Yo gen fòm yon gous maskriti ak yon sentimèt dyamèt. Chal green yo vlope nan yon ti chè ki tou jòn."
Izaj= "Moun fè lanmidon ak farin avèk rezòm arawout. Yo itilize farin sa pou fè krèp, gato, labouyi, biskwit, elatriye.  Yo konn bay ti bebe labouyi arawout tou nan plas lèt manman. Moun bouyi fèy arawout pouf è yon tizann ki bon pou moun ki soufri mal gòj ak moun ki anwe. Yo sèvi ak li tou  nan endistri chokola, preparasyon potaj."
Devlopman= "Plan sa a pouse byen nan tè plenn ki imid ki gen enpe lonbray avèk nan mòn ki fre. Yo plante l nan tè lejè sablèz li kenbe ase imitdite."
Repwodiksyon= "Yo plante arawout menm jan avèk pòmdetè. Antere mòso rizòm yo,  oubyen grenn arawout la, ant 2 bit anviwon yon mèt apa."

arawout = Word(
    common_name = "arawout"
    name = "arawout"
    other_names = "mazonbèl"
    part_of_speech = "Noun"
    type = "plant"
    scientific_name = "Maranta arundinacea L"
    family = "Marantaceae"

    origin = "Plant sa a sòti an Amerik-di-Sid. Ou kapab jwenn li tou nan anpil lòt rejyon twopikal tankou zile Awayi yo, Afrik-di-Sid, Azi, ak Ostrali."

    tags = ["plant", "root"]

    short_description = "Arawout se yon plant vivas. Genyen 2 kalite ladan l. Youn genyen yon rizòm ki long, lòt la yon rizòm ki kout. Rizòm sa yo toujou an fòm yon flèch ki kouvri ak yon bann ti kal an fòm triyang. Plant sa a kapab fleri pandan plizyè ane youn dèyè lòt. Pati tij la ki anwo tè a pa twò di. Li kapab rive  jiska 2 mèt wotè lè fin grandi."
    description = [Deskripsyon, Fey, Fle, Fwi_ak_Grenn, Izaj, Devlopman, Repwodiksyon]
   
    define_date = timezone.now()

    is_visible = True
    )
    
    arawout.save()



