

from totoro.utils import get_current_resource
resource = get_current_resource()
instru_map = resource.instru_map
mus = resource.players_registry

Cecile_clarinette=mus["Cecile_clarinette_totoro_recadre"]
Amelie_clarinette_recadre=mus["Amélie_clarinette_recadre"]
Nelly_clarinette=mus["Nelly_clarinette_totoro"]
Natacha_clarinette=mus["Natacha_clarinette_totoro"]
Pierre_clarinette=mus["Pierre_clarinette_totoro_recadre"]
Ineke_clarinette=mus["Ineke_clarinette_totoro"]
Annesonia_clarinette=mus["Anne-sonia_clarinette_totoro"]
Stephane_clarinette=mus["Stephane_clarinette_totoro"]
PierreG_clarinette=mus["PierreG_clarinette_totoro"]
Violette_clarinette=mus["Violette_clarinette_totoro"]
Alain_flute=mus["Alain_flute_totoro"]
Laurence_flute=mus["Laurence_flute_totoro"]
Antoine_flute=mus["Antoine_flute_totoro"]
Gwenn_flute=mus["Gwenn_flute_totoro_recadre"]
Benoit_flute=mus["Benoit_flute_totoro2"]
Jawad_flute=mus["Jawad_flute_totoro"]
Aurelie_hautbois=mus["Aurélie_hautbois_totoro"]
Veronique_hautbois=mus["Veronique_hautbois_totoro"]
Francoise_saxophone=mus["Francoise_saxophone_totoro"]
Aurianne_saxophone=mus["Aurianne_saxophone_totoro"]
MarieClaude_saxophone=mus["Marie-Claude_saxophone_totoro"]
Franck_saxophone=mus["Franck_saxophone_totoro"]
Nadine_saxophone=mus["Nadine_saxophone_totoro"]
Nathalie_saxophone=mus["Nathalie_saxophone_totoro"]
Chloe_saxophone=mus["Chloe_saxophone_totoro_clown_recadre"]


class Saxophone(object) :
    def __init__(self):
        self.Aurianne_saxophone=Aurianne_saxophone
        self.Chloe_saxophone=Chloe_saxophone
        self.Franck_saxophone=Franck_saxophone
        self.Francoise_saxophone=Francoise_saxophone
        self.MarieClaude_saxophone=MarieClaude_saxophone
        self.Nadine_saxophone=Nadine_saxophone
        self.Nathalie_saxophone=Nathalie_saxophone
        self.all=[Aurianne_saxophone,Chloe_saxophone,Franck_saxophone,Francoise_saxophone,MarieClaude_saxophone,Nadine_saxophone,Nathalie_saxophone]
        return
sax=Saxophone()

class Clarinettes(object) :
    def __init__(self):
        self.Amelie_clarinette_recadre=Amelie_clarinette_recadre
        self.Annesonia_clarinette=Annesonia_clarinette
        self.Cecile_clarinette=Cecile_clarinette
        self.Ineke_clarinette=Ineke_clarinette
        self.Natacha_clarinette=Natacha_clarinette
        self.Nelly_clarinette=Nelly_clarinette
        self.PierreG_clarinette=PierreG_clarinette
        self.Pierre_clarinette=Pierre_clarinette
        self.Stephane_clarinette=Stephane_clarinette
        self.Violette_clarinette=Violette_clarinette
        self.all=[Amelie_clarinette_recadre,Annesonia_clarinette,Cecile_clarinette,Ineke_clarinette,Natacha_clarinette,Nelly_clarinette,PierreG_clarinette,Pierre_clarinette,Stephane_clarinette,Violette_clarinette]
        return
clar=Clarinettes()

class Cor(object) :
    def __init__(self):
        self.all=[]
        return
cor=Cor()

class Euphonium(object) :
    def __init__(self):
        self.all=[]
        return
eph=Euphonium()

class Flutes(object) :
    def __init__(self):
        self.Alain_flute=Alain_flute
        self.Antoine_flute=Antoine_flute
        self.Benoit_flute=Benoit_flute
        self.Gwenn_flute=Gwenn_flute
        self.Jawad_flute=Jawad_flute
        self.Laurence_flute=Laurence_flute
        self.all=[Alain_flute,Antoine_flute,Benoit_flute,Gwenn_flute,Jawad_flute,Laurence_flute]
        return
fl=Flutes()

class Hautbois(object) :
    def __init__(self):
        self.Aurelie_hautbois=Aurelie_hautbois
        self.Veronique_hautbois=Veronique_hautbois
        self.all=[Aurelie_hautbois,Veronique_hautbois]
        return
hb=Hautbois()

class Percussions(object) :
    def __init__(self):
        self.all=[]
        return
perc=Percussions()

class Trombone(object) :
    def __init__(self):
        self.all=[]
        return
trb=Trombone()

class Trompettesetcornets(object) :
    def __init__(self):
        self.all=[]
        return
trp=Trompettesetcornets()

class Tuba(object) :
    def __init__(self):
        self.all=[]
        return
tb=Tuba()