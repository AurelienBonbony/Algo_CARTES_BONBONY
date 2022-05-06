class Carte:
    def __init__(self,name,coûtMana,description):
        self._name = name
        self._coûtMana = coûtMana
        self._description = description

    def getName(self):
        txt = ("La carte " + self._name + "est posée sur le terrain de jeu !")
        return txt
    def getCoûtMana(self):
        txt = ("La carte vous fait perdre " + self._coûtMana + " !")
        return txt
    


class Cristal(Carte):
    def __init__(self,name,valeur):
        Carte.__init__(self,name,5,"description")
        self._valeur = valeur
        

    def getCoûtMana(self):
        txt = ("La carte vous fait perdre " + self._coûtMana + " !")
        return txt
    
    def getDescription(self):
        txt = ("Description : Un Cristal possède une valeur. Il peut être joué pour son coût en mana (qui peut être de 0). Quand un-e Mage joue un Cristal, il reste dans sa zone de jeu, et son mana maximum augmente de sa valeur")
        return txt
    
    def getValeur(self):
        txt = "La valeur du Blast est de 2 !"
        return txt



class Creature(Carte):
    def __init__(self,name,pv,scoreAttaque):
        Carte.__init__(self,name,3,"description")
        self._pv = pv
        self._scoreAttaque = scoreAttaque
        

    def getCoûtMana(self):
        txt = ("La carte vous fait perdre " + self._coûtMana + " !")
        return txt

    def getDescription(self):
        txt = ("Une Creature peut être jouée (ce qui la place sur la zone de jeu du joueur) en payant son coût de mana, auquel cas elle reste dans la zone de jeu. Une Creature en jeu peut attaquer un-e Mage ou une autre Creature, auquel cas cette dernière l’attaque ensuite en retour. Une Creature peut perdre des points de vie, et même mourir : elle passe alors de la zone de jeu à la défausse.")
        return txt

    def getPv(self):
        txt = ("Les PV de la creature sont de ",20," !")
        return txt

    def getScoreAttaque(self):
        txt = ("L'attaque' de la creature est de ",10," !")
        return txt


class Blast(Carte):
    def __init__(self,name,valeur):
        Carte.__init__(self,name,7,"description")
        self._valeur = valeur

    def getValeur(self):
        txt = ("La valeur du Blast est de ",2," !")
        return txt
        


class Mage:
    def __init__(self,name,jouerCarte,recupMana,attaque,pv,main,défausse,zoneDeJeu,manaMax,manaActuel):
        self._name = name
        self._jouerCarte = jouerCarte
        self._recupMana = recupMana
        self._attaque = attaque
        self._pv = pv
        self._main = main
        self._défausse = défausse
        self._zoneDeJeu = zoneDeJeu
        self._manaMax = manaMax
        self._manaActuel = manaActuel

    def getPlay(self):
        self._jouerCarte = False

    def getRecupMana(self):
        self._recupMana = False


    def getAttaque(self):
        self._attaque = 5

    def getPv(self):
        self._pv = 50

    





mana = 10
valeur = 0


choix = input("choisissez votre carte parmi celles-ci : |Cristal| : 1  |Creature| : 2  |Blast| : 3    ")
if(choix=="1"):
    maCarte = Cristal("Cristal")
if(choix=="2"):
    maCarte = Creature("Zorg")
if(choix=="3"):
        maCarte = Blast("Blast")       




print (maCarte)

input()