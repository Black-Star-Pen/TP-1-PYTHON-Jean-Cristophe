# ============================================================================
# EXERCICE : Gestion simple d'une boutique
# Date : [04/2025]
# ============================================================================

from app.src.variables import creer_variables
from app.src.affichage import afficher_phrase_complete, afficher_prix_arithmetiques, afficher_recapitulatif, convertir_prix_string, afficher_facture, afficher_types
from app.src.interactions import demander_quantite, verifier_quantite
from app.src.calculs import calculer_montants, verifier_stock_faible, verifier_rupture


def main():
    # ============================================================================
    # I.  CRÉATION DES VARIABLES
    # ============================================================================
    nom_boutique, produit, prix_unitaire, quantite_stock, tva, compte_client, compte_boutique = creer_variables()

    # ============================================================================
    # II. AFFICHAGE D'UNE PHRASE COMPLÈTE
    # ============================================================================
    afficher_phrase_complete(nom_boutique, produit, prix_unitaire, quantite_stock, tva, compte_client, compte_boutique)

    # ============================================================================
    # III. OPÉRATIONS ARITHMÉTIQUES
    # ============================================================================
    montant_ht = prix_unitaire
    montant_ttc = montant_ht * (1 + tva)
    
    afficher_prix_arithmetiques(montant_ht, montant_ttc)

    # ============================================================================
    # IV. DEMANDE À L'UTILISATEUR
    # ============================================================================
    quantite_demandee = demander_quantite()

    # ============================================================================
    # V. CONVERSION ET VÉRIFICATION
    # ============================================================================
    quantite_demandee = verifier_quantite(quantite_demandee, quantite_stock)
    
    if quantite_demandee is None:
        return

    # ============================================================================
    # VI. CALCULER ET STOCKER 
    # ============================================================================
    montant_ht, montant_ttc, quantite_stock, compte_client, compte_boutique = calculer_montants(
        prix_unitaire, quantite_demandee, tva, quantite_stock, compte_client, compte_boutique
    )
    
    afficher_recapitulatif(produit, quantite_demandee, montant_ht, montant_ttc, quantite_stock, compte_client, compte_boutique)
    
    # ============================================================================
    # VII. CALCULER ET STOCKER 
    # ============================================================================
    verifier_stock_faible(quantite_stock)

    # ============================================================================
    # VIII. RAJOUTER UNE CONDITION
    # ============================================================================
    verifier_rupture(quantite_stock, prix_unitaire)
        
    # ============================================================================
    # IX. CONVERTIR LE PRIX EN TTC EN STRING AVEC €
    # ============================================================================
    convertir_prix_string(montant_ttc)
    
    # ============================================================================
    # X. AFFICHER JOLIMENT UNE FACTURE DANS LE FORMAT SUIVANT
    # ============================================================================
    afficher_facture(nom_boutique, produit, quantite_demandee, montant_ht, tva, montant_ttc)
    
    # ============================================================================
    # XI. AFFICHAGE DU TYPE DES VARIABLES
    # ============================================================================
    
    montant_ttc_str = f"{montant_ttc:.2f}€"
    afficher_types(nom_boutique, produit, prix_unitaire, quantite_stock, tva, compte_client, compte_boutique, quantite_demandee, montant_ht, montant_ttc, montant_ttc_str)


if __name__ == "__main__":
    main()