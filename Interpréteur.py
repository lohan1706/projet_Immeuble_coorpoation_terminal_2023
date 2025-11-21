from rue import dessiner_texte


# 1 - Création de l'objet-fichier : ouverture en mode r (read)
obj_fichier = open('texte_interpreteur.txt', 'r', encoding="utf-8")
 
# 2 - Lecture progressive du fichier
imm0 = obj_fichier.readline().replace('\n', '').split('-')
imm1 = obj_fichier.readline().replace('\n', '').split('-')
imm2 = obj_fichier.readline().replace('\n', '').split('-')
imm3 = obj_fichier.readline().replace('\n', '').split('-')
 
# 3 - Fermeture de l'objet-fichier
obj_fichier.close()

immeubles = [imm0, imm1, imm2,imm3]

if __name__ == '__main__':
    
dessiner_texte(immeubles)