def lireInventaire (NomFichier):
    fichier=open(NomFichier,encoding="UTF-8")
    contenu = fichier.read()
    fichier.close()
    
    '''Séparé les Information'''
    Inventaire=contenu.split("\n")
    
    lignes=contenu.split("\n")#sépare les lignes
    for i in range (len(lignes)-1):#sépare les données dans les lignes
        Inventaire[i]=lignes[i].split(";")
    
    
    '''Trier les information'''
    Informations=Inventaire[1:]
    dictionaireInven={}
    for iIn in range (len(Informations)-1):
        cle=Informations[iIn][0]
        valeur=Informations[iIn][1:]
        dictionaireInven[cle]=valeur
        
    for cle, valeurs in dictionaireInven.items():
        partieentiere, partiedecimale= valeurs.split(',')
        valeurconvertie = float(partieentiere+'.'+partiedecimale)
        dictionaireInven[cle]=valeurconvertie
            
       
    return dictionaireInven


def lireRecette (NomFichier):
    # Utilisation de l'encoding UTF-8 pour prendre en compte les caracteres avec des accents
    fichier=open(NomFichier,encoding="UTF-8")
    contenu = fichier.read()
    fichier.close()

    '''Séparer les infos'''
    Menu=contenu.split("\n")
    
    plats = {}
    for i in range(len(Menu)-1):
        if(i%6 == 0):    #met en clé les noms des plats
            plats[Menu[i].split(";")[0]]={}
        if(i%6 != 0):
            plats[Menu[i-(i%6)].split(";")[0]][Menu[i].split(";")[1]]=Menu[i].split(";")[2:]
            
    return plats


def afficheInventaire (inventaire):
    titre=['Ingrédients','Quantité','Minimale','Péremption']
    for i in range (1):
        print(f'{titre[0]:<16}|{titre[1]:<10}|{titre[2]:<10}|{titre[3]}')
    print('-'*16,'+','-'*10,'+','-'*10,'+','-'*10, sep="")#sep pour enlever les espaces entre les - et les +
    for clé, valeurs in inventaire.items():
        print(f'{clé:<16}|{valeurs[0]:<10}|{valeurs[3]:<10}|{valeurs[2]}')
    
def afficheMenu (menu) :
    for clép, valeursp in menu.items():
        print(f'{clép}:{valeursp[0]}')
        #for clé, valeurs in menu[clép].items():#valeur 0 et 2
            #print(f"{clé}:{valeurs}")

if __name__ == '__main__':
    fichierInven='Inventaire.csv'
    recette='Recettes.csv'
    Inventaire=lireInventaire(fichierInven)
    print(Inventaire)
    Menu=lireRecette(recette)
    #afficheInventaire(Inventaire)
    #afficheMenu(Menu)