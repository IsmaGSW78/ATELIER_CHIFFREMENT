import os
import nacl.secret
import nacl.utils

def main():
    print("--- ATELIER 2 : Chiffrement avec PyNaCl (SecretBox) ---")
    
    # 1. Génération d'une clé secrète (Doit faire exactement 32 octets pour SecretBox)
    key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
    
    # 2. Initialisation de la "Boîte Secrète" avec notre clé
    box = nacl.secret.SecretBox(key)
    
    fichier_source = "secret_pynacl.txt"
    fichier_chiffre = "secret_pynacl.enc"
    fichier_dechiffre = "secret_pynacl.dec.txt"

    # Création d'un fichier source de test
    with open(fichier_source, "wb") as f:
        f.write(b"Ceci est le message ultra secret de l'Atelier 2 chiffre avec PyNaCl !")

    # --- CHIFFREMENT ---
    print(f"\n[*] Chiffrement de {fichier_source}...")
    with open(fichier_source, "rb") as f:
        donnees_claires = f.read()
        
    # La méthode encrypt() de SecretBox génère automatiquement le "nonce" 
    # et l'attache au début du message chiffré.
    donnees_chiffrees = box.encrypt(donnees_claires)
    
    with open(fichier_chiffre, "wb") as f:
        f.write(donnees_chiffrees)
    print("✅ Fichier chiffré avec succès !")

    # --- DÉCHIFFREMENT ---
    print(f"[*] Déchiffrement de {fichier_chiffre}...")
    with open(fichier_chiffre, "rb") as f:
        donnees_a_decoder = f.read()
        
    # La méthode decrypt() va extraire le nonce automatiquement puis déchiffrer
    donnees_retrouvees = box.decrypt(donnees_a_decoder)
    
    with open(fichier_dechiffre, "wb") as f:
        f.write(donnees_retrouvees)
    
    print("✅ Fichier déchiffré avec succès !")
    print(f"\nContenu retrouvé : {donnees_retrouvees.decode('utf-8')}")

if __name__ == "__main__":
    main()