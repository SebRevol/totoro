

from totoro.utils import get_current_resource
resource = get_current_resource()
instru_map = resource.instru_map
mus = resource.players_registry

all_players = list(resource.players_registry.values())

JeanJacques_percu=mus["Jean-Jacques_percu_totoro"]
JeanJacques_chef_lacheprise=mus["Jean-Jacques_chef_laché prise"]
Alizee_piano=mus["Alizee_piano_totoro"]
Bidou_euphonium=mus["Bidou_euphonium_totoro"]
Serge_euphonium=mus["Serge_euphonium_totoro"]
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
Andre_cor=mus["André_cor_totoro"]
Myrtille_cor=mus["Myrtille_cor_totoro"]
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
Camille_trombone=mus["Camille_trombone_totoro"]
daniel_trombone=mus["daniel_trombone_totoro"]
Cecile_trombone=mus["Cecile_trombone_totoro"]
Bidou_cornet=mus["Bidou_cornet_totoro"]
Serge_trompette=mus["Serge_trompette_totoro"]
Marianne_trompette=mus["Marianne_trompette_totoro"]
Svoisine_tuba=mus["Svoisine_tuba"]
Serge_baryton=mus["Serge_baryton_totoro_recadre"]
Srevol_tuba_recadre=mus["Srevol_tuba_recadre"]


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
        self.Andre_cor=Andre_cor
        self.Myrtille_cor=Myrtille_cor
        self.all=[Andre_cor,Myrtille_cor]
        return
cor=Cor()

class Euphonium(object) :
    def __init__(self):
        self.Bidou_euphonium=Bidou_euphonium
        self.Serge_baryton=Serge_baryton
        self.Serge_euphonium=Serge_euphonium
        self.all=[Bidou_euphonium,Serge_baryton,Serge_euphonium]
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
        self.Alizee_piano=Alizee_piano
        self.JeanJacques_percu=JeanJacques_percu
        self.all=[Alizee_piano,JeanJacques_percu]
        return
perc=Percussions()

class Trombone(object) :
    def __init__(self):
        self.Camille_trombone=Camille_trombone
        self.Cecile_trombone=Cecile_trombone
        self.daniel_trombone=daniel_trombone
        self.all=[Camille_trombone,Cecile_trombone,daniel_trombone]
        return
trb=Trombone()

class Trompettesetcornets(object) :
    def __init__(self):
        self.Bidou_cornet=Bidou_cornet
        self.Marianne_trompette=Marianne_trompette
        self.Serge_trompette=Serge_trompette
        self.all=[Bidou_cornet,Marianne_trompette,Serge_trompette]
        return
trp=Trompettesetcornets()

class Tuba(object) :
    def __init__(self):
        self.Srevol_tuba_recadre=Srevol_tuba_recadre
        self.Svoisine_tuba=Svoisine_tuba
        self.all=[Srevol_tuba_recadre,Svoisine_tuba]
        return
tb=Tuba()