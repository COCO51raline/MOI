from loafCSV import lireInventaire, lireRecette

def prendreCommande (plat, inventaire, NbCommande):
    InventaireQuantité={}
    for cle, valeurs in inventaire.items():
        valeur=valeurs[0]
        InventaireQuantité[cle]=int(valeur)
        
    PlatsQuantité={}
    #print(Menu)
    for cleM in Menu.keys():
        if cleM==plat:
            for cle, valeurs in Menu[cleM].items():
                if cle=='Ingrédients':
                    PlatIngré=Menu[cleM][cle]
                  #  print(PlatIngré)
                if cle=='Quantité':
                    PlatQuan=Menu[cleM][cle]
                 #   print(PlatQuan)
                    
                    
            for i in range (len(PlatIngré)):
                clePQ=PlatIngré[i]
                valeurPQ=PlatQuan[i]
                PlatsQuantité[clePQ]=float[valeurPQ[:valeurPQ.index(",")]+"."+[valeurPQ[valeurPQ.index(","):]]]
          #  print(PlatsQuantité)
                
                
        
    '''
    si les cle sont egale deduir'''
       
        
    return InventaireQuantité
        
if __name__ == '__main__':
    fichierInven='Inventaire.csv'
    recette='Recettes.csv'
    Inventaire=lireInventaire(fichierInven) 
    Menu=lireRecette(recette)
    #test pour savoir si le pats est prposer ou non
    print(prendreCommande('Hachis parmentier', Inventaire, 4))