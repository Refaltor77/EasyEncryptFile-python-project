from hashlib import sha256
entree = input("Entrez le chemin d'accès du fichier à chiffrer / déchiffrer : ")
sortie = input("Entrez le chemin d'accès du fichier final (default: result.txt) : ")
if sortie == "":
    sortie = "result.txt"
key = sha256(input("Entrez la clé: ").encode('utf-8')).digest()
with open(entree, 'rb') as file_entree:
    with open(sortie, 'wb') as file_sortie:
        i = 0
        while file_entree.peek():
            file_sortie.write(bytes([ord(file_entree.read(1))^key[i % len(key)]]))
            i+=1
