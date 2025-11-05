# ============================================================================
# II. AFFICHAGE D'UNE PHRASE COMPLÈTE
# ============================================================================

def afficher_phrase_complete(nom_boutique, produit, prix_unitaire, quantite_stock, tva, compte_client, compte_boutique):
     
    print(f"""Bienvenue chez {nom_boutique}, 👋 M. Jean-Cristopher ! Dans notre boutique de gens bizarres "Fk🖕 Microsfot", nous vendons des {produit}🧦 avec des motifs de fou 😆. 
    Prix unitaire : {prix_unitaire}€ 
    Stock disponible : {quantite_stock} paires 
    TVA : {tva * 100}% 
    Compte client : {compte_client}€ 
    Compte boutique : {compte_boutique}€""")


# ============================================================================
# III. OPÉRATIONS ARITHMÉTIQUES (partie affichage)
# ============================================================================

def afficher_prix_arithmetiques(montant_ht, montant_ttc):
   
    print(f"\nPrix HT unitaire: {montant_ht:.2f}€") #Arrondir à 2 décimales  .2f
    print(f"Prix TTC unitaire: {montant_ttc:.2f}€")#Arrondir à 2 décimales  .2f


# ============================================================================
# VI. CALCULER ET STOCKER (partie affichage du récapitulatif)
# ============================================================================

def afficher_recapitulatif(produit, quantite_demandee, montant_ht, montant_ttc, quantite_stock, compte_client, compte_boutique):
     
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
# IX. CONVERTIR LE PRIX EN TTC EN STRING AVEC €
# ============================================================================

def convertir_prix_string(montant_ttc):
     
    montant_ttc_str = f"{montant_ttc:.2f}€"
    print(f"\n ▶️Montant total à payer : {montant_ttc_str}")


# ============================================================================
# X. AFFICHER JOLIMENT UNE FACTURE DANS LE FORMAT SUIVANT
# ============================================================================

def afficher_facture(nom_boutique, produit, quantite_demandee, montant_ht, tva, montant_ttc):
     
    print("\n" + "-" * 80)
    print(f"{nom_boutique:^80}")  # Centré sur 80 caractères
    print("-" * 80)
    print(" FACTURE".center(75))
    print()
    print(f"Produit{' ' * 45}qté{' ' * 10}ht")
    print(f"{produit.capitalize()}{' ' * 42}{quantite_demandee}{' ' * 6}{montant_ht:.2f}€")
    print(f"\n{' ' * 45}Total HT : {' ' * 5}{montant_ht:.2f}€")
    print(f"{' ' * 50}TVA : {' ' * 6}{tva:.2f}€")
    print(f"{' ' * 44}Total TTC : {' ' * 5}{montant_ttc:.2f}€")
    print("-" * 80)


# ============================================================================
# XI. AFFICHAGE DU TYPE DES VARIABLES
# ============================================================================

def afficher_types(nom_boutique, produit, prix_unitaire, quantite_stock, tva, compte_client, compte_boutique, quantite_demandee, montant_ht, montant_ttc, montant_ttc_str):
     
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