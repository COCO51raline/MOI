from loafCSV import lireInventaire, lireRecette, afficheInventaire

def prendreCommande (plat: str, inventaire:dict, NbCommande:int = 1):
    #print(Menu)
    # si le plat n'est pas dans le menu
    if plat not in Menu.keys():
        # on retourne l'inventaire sans rien modifier
        return inventaire
    # si le plat est dans le menu
    # on récupère les ingrédients du plat
    Ingredients = Menu[plat]
    # pour chaque ingrédient du plat
    for i in range (len(Ingredients['Ingrédients'])):
        # on récupère la quantité de l'ingrédient
        quantite = float(Ingredients['Quantité'][i].replace(',', '.') )
        # on soustrait la quantité de l'ingrédient du stock de l'inventaire en multipliant par le nombre de commandes
        inventaire[Ingredients['Ingrédients'][i]][0] = float(inventaire[Ingredients['Ingrédients'][i]][0]) - (quantite*NbCommande)
            
    return inventaire
        
if __name__ == '__main__':
    fichierInven='Inventaire.csv'
    recette='Recettes.csv'
    Inventaire=lireInventaire(fichierInven) 
    Menu=lireRecette(recette)
    #test pour savoir si le pats est prposer ou non
    afficheInventaire(Inventaire)
    prendreCommande('Hachis parmentier', Inventaire, 4)
    afficheInventaire(Inventaire)