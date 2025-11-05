# ============================================================================
# VI. CALCULER ET STOCKER (partie calculs)
# ============================================================================

def calculer_montants(prix_unitaire, quantite_demandee, tva, quantite_stock, compte_client, compte_boutique):
  
    montant_ht = prix_unitaire * quantite_demandee # Prix hors taxe total de la commande
    montant_ttc = montant_ht * (1 + tva) # Prix toutes taxes comprises total de la commande
    
    quantite_stock = quantite_stock - quantite_demandee # Met à jour le stock disponible
    
    compte_client = compte_client - montant_ttc # Met à jour le compte client
    compte_boutique = compte_boutique + montant_ttc # Met à jour le compte boutique
    
    return montant_ht, montant_ttc, quantite_stock, compte_client, compte_boutique


# ============================================================================
# VII. CALCULER ET STOCKER 
# ============================================================================

def verifier_stock_faible(quantite_stock):
    
    if quantite_stock < 10:     #a)
        print("\n ⛔!! Stock bientôt épuisé !!⛔")  #affiche un message d'alerte si le stock est inférieur à 10 paires


# ============================================================================
# VIII. RAJOUTER UNE CONDITION
# ============================================================================

def verifier_rupture(quantite_stock, prix_unitaire):
   
    if quantite_stock < 15 and quantite_stock > 10 and prix_unitaire > 5:#Opérateur Logique AND,    
        print("⚠️!! Attention produit presque en rupture !!⚠️")