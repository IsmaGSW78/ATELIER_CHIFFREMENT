import os
import sys
from cryptography.fernet import Fernet

def main():
    # 1. Récupération de la clé depuis l'environnement (Injectée par GitHub Secrets)
    key = os.environ.get("SECRET_FERNET_KEY")
    
    if not key:
        print("❌ ERREUR : Le Secret 'SECRET_FERNET_KEY' est introuvable.")
        print("Vérifie que le secret est bien configuré sur GitHub et que ton environnement a été rechargé.")
        sys.exit(1)

    print("✅ Clé secrète récupérée avec succès depuis GitHub !")
    
    # 2. Initialisation de l'outil de chiffrement
    cipher = Fernet(key)

    fichier_source = "secret_atelier.txt"
    fichier_chiffre = "secret_atelier.enc"
    fichier_dechiffre = "secret_atelier.dec.txt"

    # Création d'un petit fichier de test s'il n'existe pas
    if not os.path.exists(fichier_source):
        with open(fichier_source, "wb") as f:
            f.write(b"Ceci est un message ultra confidentiel pour l'atelier 1 !")

    # --- ENCODAGE (Chiffrement) ---
    print(f"[*] Chiffrement de {fichier_source}...")
    with open(fichier_source, "rb") as f:
        donnees_claires = f.read()
    
    donnees_chiffrees = cipher.encrypt(donnees_claires)
    
    with open(fichier_chiffre, "wb") as f:
        f.write(donnees_chiffrees)

    # --- DÉCODAGE (Déchiffrement) ---
    print(f"[*] Déchiffrement de {fichier_chiffre}...")
    with open(fichier_chiffre, "rb") as f:
        donnees_a_decoder = f.read()
        
    donnees_retrouvees = cipher.decrypt(donnees_a_decoder)
    
    with open(fichier_dechiffre, "wb") as f:
        f.write(donnees_retrouvees)

    print(f"✅ Opération terminée. Le fichier a été chiffré puis déchiffré avec succès !")

if __name__ == "__main__":
    main()