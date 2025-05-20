import plotly.express as px
import pandas as pd

# Chargement des données depuis un fichier CSV hébergé sur Google Sheets
donnees = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')


#Quantite vendue par region
figure_qte_per_region = px.pie(donnees, values='qte', names='region', title='quantite vendue par region')
figure_qte_per_region.write_html('ventes-par-region.html')
print('ventes-par-region.html genere avec succes !')

#Vente par produit
figure_qte_per_product = px.pie(donnees, values='qte', names='produit', title='ventes par produit')
figure_qte_per_product.write_html('ventes-par-produit.html')
print('ventes-par-produit.html genere avec succes !')

#Chiffre d'affaire par produit
#Rajout d'une colonne "chiffre d'affaire" pour pouvoir representer le chiffre d'affaire par produit
donnees["chiffre_affaire"] = donnees['prix']*donnees['qte'] 
figure_ca_per_produit = px.pie(donnees, values='chiffre_affaire', names='produit', title='chiffre d\'affaires par produit')
figure_ca_per_produit.write_html('ca-par-produit.html')
print('ca-par-produit.html genere avec succes !')

#Chiffre d'affaire par region
figure_ca_per_region = px.pie(donnees, values='chiffre_affaire', names='region', title='chiffre d\'affaires par région')
figure_ca_per_region.write_html('ca-par-région.html')
print('ca-par-région.html genere avec succes !')




