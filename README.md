(Web scraping)
# 🍫 Projet Cacao - Scraping & Transformation

## 📌 Contexte
Ce projet académique consiste à travailler sur un jeu de données issu du site [Codecademy Cacao Dataset](https://content.codecademy.com/courses/beautifulsoup/cacao/index.html).  

- La **partie extraction** (scraping avec `BeautifulSoup`) a été fournie .  
- La **partie transformation** (nettoyage, typage, enrichissement des données) a été réalisée dans un **package Python dédié** : `transformation_cacao`.

## Structure du projet
package_notes_de_cacao/
├─ Pipeline_using_scrapping.ipynb # Notebook enrichi avec ma transformation
├─ cacao_clean.csv # Données nettoyées exportées
├─ transformation_cacao/ # Package de transformation
│ ├─ init.py
│ ├─ nettoyage.py
│ ├─ typage.py
│ ├─ features.py
│ └─ pipeline.py

## ⚙️ Installation
Avant d'exécuter le notebook, installez les dépendances nécessaires :  
```bash
pip install -r requirements.txt

Librairies utilisées :

beautifulsoup4

requests

pandas

matplotlib

numpy

Utilisation

Ouvrir et exécuter Pipeline_using_scrapping.ipynb dans VS Code ou Jupyter.

Après l'extraction (df brut), le pipeline de transformation est appliqué via :

from transformation_cacao import transform_cacao
df_clean = transform_cacao(df)

Un export CSV est généré automatiquement :
cacao_clean.csv

Visualisations Bonus:

Le notebook inclut aussi des visualisations :

Histogramme de la distribution des notes (Rating);

Histogramme des pourcentages de cacao (CocoaPercent);

Nuage de points montrant la relation entre % de cacao et Rating;

 Résultat attendu :

Un DataFrame propre avec colonnes :

Company (catégorie)

BeanOrigin (catégorie)

Rating (float)

CocoaPercent (float)

CocoaFraction (float : CocoaPercent / 100) .


