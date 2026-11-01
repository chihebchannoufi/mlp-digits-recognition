# Reconnaissance de chiffres avec un MLP

> **Travail réalisé par Chiheb Channoufi et Ines Ayari.**

Ce projet utilise un perceptron multicouche (*Multi-Layer Perceptron*, MLP) pour
reconnaître des chiffres manuscrits. L'application Streamlit permet de tester
le modèle sur une image du jeu de données `digits` de scikit-learn ou sur une
image importée par l'utilisateur.

## Contenu du projet

- `app.py` : interface web Streamlit.
- `modele_et_scaler.pkl` : modèle MLP et scaler sauvegardés.
- `exercice-mlp-pour-digitsd.ipynb` : notebook d'entraînement et d'évaluation.
- `requirements.txt` : dépendances Python du projet.

## Installation et exécution

### 1. Cloner le projet

```bash
git clone https://github.com/chihebchannoufi/mlp-digits-recognition.git
cd mlp-digits-recognition
```

### 2. Créer un environnement virtuel

Avec Windows PowerShell :

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Si PowerShell bloque l'activation des scripts, exécuter au préalable :

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Avec Windows CMD :

```bat
python -m venv venv
venv\Scripts\activate
```

Sur Linux ou macOS :

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances

Une fois l'environnement virtuel activé, installer les packages nécessaires :

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Lancer l'interface Streamlit

Depuis le dossier du projet et avec l'environnement virtuel activé :

```bash
python -m streamlit run app.py
```

Une adresse locale s'affichera dans le terminal, généralement
`http://localhost:8501`. Ouvrir cette adresse dans un navigateur.

L'interface permet de :

1. sélectionner une image du jeu de données intégré ;
2. comparer le chiffre réel avec la prédiction du modèle ;
3. importer une image PNG, JPG ou JPEG de son choix ;
4. inverser les couleurs de l'image si nécessaire avant la prédiction.

### 5. Arrêter l'application

Dans le terminal où Streamlit est lancé, appuyer sur `Ctrl+C`, puis désactiver
l'environnement virtuel avec :

```bash
deactivate
```

## Réentraîner le modèle

Le modèle utilisé par l'interface est déjà fourni dans
`modele_et_scaler.pkl`. Pour le réentraîner ou modifier la recherche
d'hyperparamètres, ouvrir `exercice-mlp-pour-digitsd.ipynb` dans Jupyter
Notebook ou JupyterLab, exécuter les cellules, puis relancer l'application
Streamlit.
