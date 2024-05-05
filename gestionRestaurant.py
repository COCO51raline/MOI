from exportCSV import exportInventaire
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
        if Ingredients['Quantité'][i] == '':
            break
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
            caisse["Depenses"] = float(caisse["Depenses"]) - (quantiteMinimale*prixIngredient)

    return caisse,inventaire
        
def finDeJournee(commandes:dict,menu:dict,inventaire:dict,caisse:list):
    # pour chaque commande
    for commande in commandes.keys():
        # on prend la commande
        inventaire = prendreCommande(commande, inventaire, commandes[commande])
        # on ajoute le prix de la commande à la caisse
        caisse["Recettes"] = float(caisse["Recettes"]) + (float(menu[commande]["Prix sur la carte"][0]) * commandes[commande])
        # on ajoute le prix de fabrication de la commande à la caisse
        caisse["Cout Fabrication"] = float(caisse["Cout Fabrication"]) + (float(menu[commande]["Coût de fabrication"][0].replace(',', '.'))*commandes[commande])
    # on remplit l'inventaire
    caisse, inventaire = remplissageInventaire(inventaire, caisse)
    # on calcule les bénéfices
    caisse["Benefices"] = caisse["Recettes"] - caisse["Cout Fabrication"]
    return caisse, inventaire


if __name__ == '__main__':
    fichierInven='Inventaire.csv'
    recette='Recettes.csv'
    Inventaire=lireInventaire(fichierInven) 
    Menu=lireRecette(recette)
    #test pour savoir si le pats est prposer ou non
    afficheInventaire(Inventaire)
    caisse = {"Depenses":0, "Recettes":0 , "Benefices":0,"Cout Fabrication":0}
    commandes = {"Hachis parmentier":30, "Chili con carne":10 , "Quiche lorraine":16}
    caisse, Inventaire = finDeJournee(commandes, Menu, Inventaire, caisse)
    afficheInventaire(Inventaire)
    print(caisse)
    exportInventaire(Inventaire)