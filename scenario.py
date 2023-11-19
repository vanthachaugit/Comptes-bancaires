from compte import *
 
def compte_simple(): 

    #Personne :

    P1 = Personne("Wayne", "Bruce")
    #print(P1)
    P2 = Personne("Kent", "Clark")
    #print(P2)

    C1 = CompteSimple(12000, P1)
    #print(C1)
    C2 = CompteSimple(1000, P2)
    #print(C2)

    #Assertion
    assert C1.solde == 12000 
    assert C1.titulaire is P1 
"""
    #Créditer : 
    C1.crediter(1000)
    assert C1.solde == 13000

    #Débiter : 
    C1.debiter(11000)
    assert C1.solde == 2000
"""

compte_simple()

def compte_courant():
    P1 = Personne("Wayne", "Bruce")
    P2 = Personne("Kent", "Clark")

    CC1 = CompteCourant(15000, P1)
    CC2 = CompteCourant(3000, P2)


    CC1.crediter(1000)
    CC1.debiter(2000)
    CC1.debiter(3000)
    CC1.debiter(6000)
    CC1.crediter(20000)

    H1 = CC1.editer_operations()
    #print(CC1.solde)

compte_courant()


def main_banque(): 
    
    B = Banque()

    P1 = Personne("John", "Doe")
    P2 = Personne("Kent", "Clark")
    P3 = Personne("Bruce", "Wayne")
    P4 = Personne("John", "Wick")

    cs1 = B.ouvrir_compte(P1, 1000)
    cs2 = B.ouvrir_compte(P2, 5000)

    cc1 = B.ouvrir_compte_courant(P1, 2000)
    cc2 = B.ouvrir_compte_courant(P2, 3000)
    cc3 = B.ouvrir_compte_courant(P3, 4000)
    cc4 = B.ouvrir_compte_courant(P4, 5000)
    #print(cc1)
    #print(cc2)

    T = B.total_argent()

    #B.prelever_frais(4)

    #assert B.total_argent() == 4996 

    B.prelever_frais(10)
    cc1.editer_operations()
    #print("C1 =", c1)


    E = B.editer_releve()
    for releve in E:
        print(releve)


main_banque()
