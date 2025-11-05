# ============================================================================
# IV. DEMANDE À L'UTILISATEUR
# ============================================================================

def demander_quantite():
     
    quantite_demandee = input("\nCombien de paires de chaussettes ChossettZ voulez-vous acheter ? ")
    return quantite_demandee


# ============================================================================
# V. CONVERSION ET VÉRIFICATION
# ============================================================================

def verifier_quantite(quantite_demandee, quantite_stock):
   
    try:
        quantite_demandee = int(quantite_demandee)
    except ValueError:
        print("🛑 Erreur : La quantité demandée doit être un nombre entier positif et non des lettres. On vend des paires de chaussettes entière, pas des cryptos de chaussette (Ahahaha..je Rigole — hein ?) 😆.")
        return None  # quitte la fonction proprement

    if quantite_demandee <= 0:
        print("🛑 Erreur : La quantité demandée doit être un nombre entier positif. On vend des chaussettes, pas des cryptos de chaussette (Ahahah...Je rigole — Hein ??) 😆.")
        return None  

    if quantite_demandee > quantite_stock:
        print(f"Erreur : La quantité demandée dépasse le stock disponible ({quantite_stock} paires). Ne vous en faites pas, nous allons réapprovisionner ça très vite, en espérant vous revoir ! 😉.")
        return None
    
    print("✅ Quantité demandée valide.")
    
    return quantite_demandee