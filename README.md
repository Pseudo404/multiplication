# ➗ Table de multiplication (Console)

Ce dépôt regroupe **mes premiers jeux en console Python**, centrés sur l’entraînement aux tables de multiplication.  
Ces projets font partie de **mes tout premiers codes**, écrits lors de mes débuts en programmation.

Ils illustrent parfaitement mon **évolution technique**, du code très naïf et répétitif vers un code plus court, lisible et efficace.

---

## 🧠 table_multiplication.py — Version originale

**table_multiplication.py** est **mon tout premier jeu en console**.  
Il s’agit d’un test de mathématiques permettant de s’entraîner aux tables de multiplication.

### 🔹 Principe
- L’utilisateur choisit une table de multiplication via un `input`
- Chaque calcul est affiché un par un (`1x2`, `1x3`, `1x4`, etc.)
- Une saisie est demandée pour chaque calcul
- Toute la logique repose principalement sur des **conditions `if`**

### ⚠️ État du code
- **960 lignes**
- Code extrêmement répétitif
- Aucune abstraction (pas de boucles efficaces, pas de fonctions)
- Lisibilité faible

➡️ **C’est un code objectivement mauvais**, mais **fonctionnel**.  
Il fait partie intégrante de mes débuts et représente ma première confrontation à la logique algorithmique.

---

## 🔄 #--Mathématiques_remaster--#.py — Version remasterisée

Ce fichier est une **refonte complète** du projet initial, réalisée plus tard, une fois que j’avais compris :
- les boucles
- la génération aléatoire
- la simplification de la logique

### ✅ Améliorations majeures
- **23 lignes de code** au lieu de 960 lignes
- Génération aléatoire des multiplications
- Système de score :
  - +1 point pour une bonne réponse
  - -1 point pour une mauvaise
  - victoire à 20 points
- Code plus lisible, plus propre et plus maintenable

### 🔹 Principe du jeu
- Une question de multiplication est générée aléatoirement
- Le joueur répond via la console
- Le score évolue jusqu’à atteindre 20 points

---

## 🛠️ Technologies utilisées

- **Langage** : Python
- **Librairies** :
  - `random` (bibliothèque standard)
- **Concepts abordés** :
  - Entrées utilisateur (`input`)
  - Conditions (`if`)
  - Boucles (`while`)
  - Génération aléatoire
  - Gestion d’un score

---

## ▶️ Lancer les projets

Prérequis :
- **Python 3**

Lancer la version originale :

```bash
python table_multiplication.py
