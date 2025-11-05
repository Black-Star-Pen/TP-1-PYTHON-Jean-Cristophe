# ============================================================================
# EXERCICE : Gestion simple d'une boutique
# Date : [04/2025]
# ============================================================================


def boutique():
    # ============================================================================
    # I.  CRÉATION DES VARIABLES
    # ============================================================================
    nom_boutique: str = "ChossettZ"
    produit: str = "Chaussettes"
    prix_unitaire: float = 5.99
    quantite_stock: int = 20
    tva: float = 0.20
    compte_client: float = 100.00
    compte_boutique: float = 0.00

    # ============================================================================
    # II. AFFICHAGE D'UNE PHRASE COMPLÈTE
    # ============================================================================
    print(f"""Bienvenue chez {nom_boutique}, 👋 M. Jean-Cristopher ! Dans notre boutique de gens bizarres "Fk🖕 Microsfot", nous vendons des {produit}🧦 avec des motifs de fou 😆. 
    Prix unitaire : {prix_unitaire}€ 
    Stock disponible : {quantite_stock} paires 
    TVA : {tva * 100}% 
    Compte client : {compte_client}€ 
    Compte boutique : {compte_boutique}€""")

    # ============================================================================
    # III. OPÉRATIONS ARITHMÉTIQUES
    # ============================================================================
    montant_ht= prix_unitaire
    montant_ttc= montant_ht * (1 + tva)

    print(f"\nPrix HT unitaire: {montant_ht:.2f}€") #Arrondir à 2 décimales  .2f
    print(f"Prix TTC unitaire: {montant_ttc:.2f}€")#Arrondir à 2 décimales  .2f

    # ============================================================================
    # IV. DEMANDE À L'UTILISATEUR
    # ============================================================================
    quantite_demandee = input("\nCombien de paires de chaussettes ChossettZ voulez-vous acheter ? ")

    # ============================================================================
    # V. CONVERSION ET VÉRIFICATION
    # ============================================================================
    
    try:
        quantite_demandee = int(quantite_demandee)
    except ValueError:
        print("Erreur : La quantité demandée doit être un nombre entier positif et non des lettres. On vend des paires de chaussettes entière, pas des cryptos de chaussette (Ahahaha..je Rigole — hein ?) 😆.")
        return  # quitte la fonction proprement

    if quantite_demandee <= 0:
        print("Erreur : La quantité demandée doit être un nombre entier positif. On vend des chaussettes, pas des cryptos de chaussette 😆.")
        return  

    if quantite_demandee > quantite_stock:
        print(f"Erreur : La quantité demandée dépasse le stock disponible ({quantite_stock} paires). Ne vous en faites pas, nous allons réapprovisionner ça très vite, en espérant vous revoir ! 😉.")
        return
    
    print("✅ Quantité demandée valide.")
    
    # ============================================================================
    # VI. CALCULER ET STOCKER 
    # ============================================================================
    
    montant_ht = prix_unitaire * quantite_demandee # Prix hors taxe total de la commande
    montant_ttc = montant_ht * (1 + tva) # Prix toutes taxes comprises total de la commande
    
    quantite_stock = quantite_stock - quantite_demandee # Met à jour le stock disponible
    
    compte_client = compte_client - montant_ttc # Met à jour le compte client
    compte_boutique = compte_boutique + montant_ttc # Met à jour le compte boutique
    print(f"Merci pour votre achat Jean-Cristopher ( tu es un bon ) ! Vous avez acheté {quantite_demandee} paires de chaussettes ChossettZ pour un total de {montant_ttc:.2f}€ TTC. 🧦💰")
    
    #Affichage du récapitulatif
    
    print("\n=== RÉCAPITULATIF DE LA VENTE ===")
    print(f"Produit : {produit}")
    print(f"Quantité achetée : {quantite_demandee} paires")
    print(f"Prix HT total : {montant_ht:.2f}€")
    print(f"Prix TTC total : {montant_ttc:.2f}€")
    print(f"Stock restant : {quantite_stock} paires")
    print(f"Compte client restant : {compte_client:.2f}€")
    print(f"Compte boutique : {compte_boutique:.2f}€")
    
    # ============================================================================
    # VII. CALCULER ET STOCKER 
    # ============================================================================
                              
    if quantite_stock < 10:     #a)
        print("\n ⛔!! Stock bientôt épuisé !!⛔")  #affiche un message d'alerte si le stock est inférieur à 10 paires

    # ============================================================================
    # VIII. RAJOUTER UNE CONDITION
    # ============================================================================
    
    if quantite_stock < 15 and quantite_stock > 10 and prix_unitaire > 5:#Opérateur Logique AND,    
        print("⚠️!! Attention produit presque en rupture !!⚠️")
        
    # ============================================================================
    # IX. CONVERTIR LE PRIX EN TTC EN STRING AVEC €
    # ============================================================================
    
    montant_ttc_str = f"{montant_ttc:.2f}€"
    print(f"Montant total à payer : {montant_ttc_str}")
    
    # ============================================================================
    # X. AFFICHER JOLIMENT UNE FACTURE DANS LE FORMAT SUIVANT
    # ============================================================================
    
    print("\n" + "-" * 80)
    print(f"{nom_boutique:^80}")  # Centré sur 80 caractères
    print("-" * 80)
    print(" FACTURE".center(75))
    print()
    print(f"Produit{' ' * 45}qté{' ' * 10}ht")
    print(f"{produit.capitalize()}{' ' * 42}{quantite_demandee}{' ' * 7}{montant_ht:.2f}")
    print(f"\nTotal HT : {montant_ht:.2f}")
    print(f"TVA : {tva:.2f}")
    print(f"Total TTC : {montant_ttc:.2f}")
    print("-" * 80)
    
    # ============================================================================
    # XI. AFFICHAGE DU TYPE DES VARIABLES
    # ============================================================================
    
    print("\n=== TYPES DES VARIABLES ===")
    print()
    print(f"le type de {nom_boutique} est {type(nom_boutique)}")
    print(f"le type de {produit} est {type(produit)}")
    print(f"le type de {prix_unitaire} est {type(prix_unitaire)}")
    print(f"le type de {quantite_stock} est {type(quantite_stock)}")
    print(f"le type de {tva} est {type(tva)}")
    print(f"le type de {compte_client} est {type(compte_client)}")
    print(f"le type de {compte_boutique} est {type(compte_boutique)}")
    print(f"le type de {quantite_demandee} est {type(quantite_demandee)}")
    print(f"le type de {montant_ht} est {type(montant_ht)}")
    print(f"le type de {montant_ttc} est {type(montant_ttc)}")
    print(f"le type de {montant_ttc_str} est {type(montant_ttc_str)}")
    
    
    
   
if __name__ == "__main__":
    boutique()
