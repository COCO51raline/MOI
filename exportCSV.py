def exportInventaire (inventaire,path= 'Export.csv'):
    fichierAecraser=open(path,'w')
    fichierAecraser.write('Ingrédients;Quantité;Prix;Minimale;Péremption\n')
    for clé, valeurs in inventaire.items():
        fichierAecraser.write(f'{clé};{valeurs[0]};{valeurs[1]};{valeurs[3]};{valeurs[2]}\n')
    fichierAecraser.close()



