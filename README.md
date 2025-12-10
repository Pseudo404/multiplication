# ➗ Quiz de multiplication — Évolution d’un projet

Ce dépôt regroupe **trois versions successives** d’un même concept :  
un **jeu de quiz de multiplication** en Python.

À travers ces trois fichiers, on peut suivre **l’évolution de mon niveau**, depuis mes tout premiers essais en programmation jusqu’à une version graphique plus aboutie.

---

## 🧠 table_multiplication.py — Version originale (console)

**table_multiplication.py** est **mon tout premier jeu en console** et l’un de mes **tout premiers codes Python**.

### 🔹 Principe
- L’utilisateur choisit une table de multiplication via un `input`
- Chaque calcul est affiché manuellement (`1x2`, `1x3`, `1x4`, etc.)
- Une saisie est demandée pour chaque calcul
- Toute la logique repose presque exclusivement sur des conditions `if`

### ⚠️ État du code
- Environ **900 lignes**
- Code très répétitif
- Aucune abstraction
- Peu lisible et difficilement maintenable

➡️ Ce code est objectivement mauvais selon les standards actuels,  
mais **il fonctionne** et représente ma toute première expérience avec la logique algorithmique.

---

## 🔄 #--Mathématiques_remaster--#.py — Version remasterisée (console)

Cette version est une **refonte complète** de la première, réalisée après avoir acquis de meilleures bases.

### ✅ Améliorations
- **23 lignes de code** environ
- Multiplications générées aléatoirement
- Système de score :
  - +1 pour une bonne réponse
  - -1 pour une mauvaise réponse
  - victoire à 20 points
- Logique simplifiée et beaucoup plus lisible

### 🔹 Principe
- Une multiplication aléatoire est affichée
- Le joueur répond via la console
- Le score évolue jusqu’à atteindre 20 points

Cette version marque un **premier vrai déclic** dans ma compréhension des boucles et de la simplification du code.

---

## 🖥️ quiz.py — Version graphique (GUI)

**quiz.py** est la version la plus récente du projet.  
Elle reprend le principe du quiz aléatoire, mais avec une **interface graphique**.

### ✅ Nouveautés
- Interface graphique avec `tkinter` et `customtkinter`
- Bouton de validation
- Champ de saisie
- Affichage :
  - de la question
  - du score (bonnes réponses / questions)
  - du retour immédiat (+1 / mauvaise réponse)

### 🔹 Principe
- Une multiplication aléatoire est affichée à l’écran
- Le joueur saisit sa réponse
- Le score est mis à jour en temps réel
- Une nouvelle question est générée automatiquement

Cette version marque mon passage :
- du **console → graphique**
- d’un script basique → une application interactive

---

## 🛠️ Technologies utilisées

- **Langage** : Python
- **Librairies** :
  - `random` (bibliothèque standard)
  - `tkinter`
  - `customtkinter`
- **Concepts abordés** :
  - Entrées utilisateur (`input`, `Entry`)
  - Conditions
  - Boucles
  - Génération aléatoire
  - Gestion du score
  - Interfaces graphiques (GUI)

---

## ▶️ Lancer les projets

### Version console (ancienne) :
```bash
python table_multiplication.py
```
```bash
python "#--Mathématiques_remaster--#.py"
```
```bash
pip install customtkinter
python quiz.py
```
