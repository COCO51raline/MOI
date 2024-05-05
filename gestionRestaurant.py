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

def remplissageInventaire (inventaire:dict, caisse:list):
    # pour chaque ingrédient de l'inventaire
    for ingredient in inventaire.keys():
        # si la quantité de l'ingrédient est inférieure à la quantité minimale
        quantiteIngredient = float(inventaire[ingredient][0])
        quantiteMinimale = float(inventaire[ingredient][3].replace(',', '.'))
        prixIngredient = float(inventaire[ingredient][1].replace(',', '.'))
        if quantiteIngredient < quantiteMinimale:
            # on ajoute la quantité minimale à la quant
            inventaire[ingredient][0] = quantiteIngredient + quantiteMinimale
            # on soustrait le prix de la quantité minimale à la caisse
            caisse[0] = float(caisse[0]) - (quantiteMinimale*prixIngredient)

    return caisse,inventaire
        
if __name__ == '__main__':
    fichierInven='Inventaire.csv'
    recette='Recettes.csv'
    Inventaire=lireInventaire(fichierInven) 
    Menu=lireRecette(recette)
    #test pour savoir si le pats est prposer ou non
    afficheInventaire(Inventaire)
    prendreCommande('Hachis parmentier', Inventaire, 4)
    afficheInventaire(Inventaire)
    caisse = [100]
    caisse, Inventaire = remplissageInventaire(Inventaire, caisse)
    afficheInventaire(Inventaire)
    print(caisse)