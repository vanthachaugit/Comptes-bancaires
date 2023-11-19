
class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom 
        self.prenom = prenom

    def __str__(self) -> str:
        return f"Compte : {self.nom} {self.prenom}" 
    
class CompteSimple:

    def __init__(self, depot, titulaire : Personne): 
        self.titulaire = titulaire
        self.__solde = depot
        
    def __str__(self):
        return str(self.titulaire) + " : " + str(self.__solde)

    def crediter(self, montant): 
        self.__solde += montant

    def debiter(self, montant): 
        self.__solde -= montant 

    @property
    def solde(self):
        return self.__solde
    
class Banque: 
    def __init__(self) -> None:
        self.__comptes = [] 

    def __str__(self): 
        return f"La sommes des soldes des comptes : {self.total_argent()}"
    
    def ouvrir_compte(self, client, argent):
        c = CompteSimple(argent, client)
        self.__comptes.append(c)
        return c

    #total des soldes des comptes
    def total_argent(self):
        total = 0
        for c in self.__comptes:
            total += c.solde
        return total
        #solution 2 avec compréhension de liste: return sum(c.solde for c in self.__comptes)
    
    # prélever frais sur tous les comptes 
    def prelever_frais(self, frais):
        for c in self.__comptes:
            c.debiter(frais)
    
    def ouvrir_compte_courant(self, client, argent):
        cc = CompteCourant(argent, client)
        self.__comptes.append(cc)
        return cc

    def editer_releve(self):
        releve = []
        for compte in self.__comptes:
            if isinstance(compte, CompteSimple):
                releve.append(f"Compte Simple - {compte.titulaire.nom} {compte.titulaire.prenom}: {compte.solde}")
            elif isinstance(compte, CompteCourant):
                releve.append(f"Compte Courant - {compte.titulaire.nom} {compte.titulaire.prenom}: {compte.solde}")
        return releve


class CompteCourant(CompteSimple): 

    def __init__(self, depot, titulaire : Personne): 
        super().__init__(depot, titulaire)
        self.operations = [] 

    def crediter(self, montant): 
        super().crediter(montant)
        self.operations.append(montant)

    def debiter(self, montant): 
        super().debiter(montant)
        self.operations.append(-montant)

    def editer_operations(self):
        print(self.operations)