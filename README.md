# TP-Gestion-Projet-1

# TP – Gestion de projet avec GitHub Projects

**Développement Python avec GitHub Projects (Kanban & Roadmap)**

## Objectifs

* Structurer un **projet informatique collaboratif**
* Utiliser **GitHub Projects** pour planifier et suivre un projet
* Mettre en œuvre un **workflow Kanban** et une **Roadmap (Gantt)**
* Gérer des **issues**, des **milestones (sprints)** et des **labels**
* Relier **développement**, **tests** et **documentation**
* Produire un **livrable professionnel** (code + suivi de projet)

## Pré-requis

* Compte GitHub actif
* Notions de base sur :

  * repositories
  * issues
* Poste avec navigateur web
* Bases de Python

## Outils utilisés

* GitHub
* GitHub Projects (Kanban + Roadmap)
* Python
  *(IDLE, VS Code, Thonny ou Jupyter Notebook)*

## Mini-projet support

### Application Python : **Gestionnaire de contacts**

L’application permet de gérer une liste de contacts stockée dans un fichier (JSON ou CSV).

### Fonctionnalités attendues

| Issue                     | Description                         | Responsable | Sprint   | Début | Fin   |
| ------------------------- | ----------------------------------- | ----------- | -------- | ----- | ----- |
| Création fichier contacts | Stockage des contacts (JSON ou CSV) | Noa         | Sprint 1 | 19/01 | 20/01 |
| Ajouter un contact        | Ajout d’un contact                  | Charles     | Sprint 1 | 19/01 | 21/01 |
| Supprimer un contact      | Suppression d’un contact            | Charles     | Sprint 1 | 20/01 | 22/01 |
| Lister les contacts       | Affichage des contacts              | Luc         | Sprint 1 | 20/01 | 22/01 |
| Tests unitaires           | Vérification des fonctionnalités    | Enzo        | Sprint 2 | 22/01 | 23/01 |
| Documentation utilisateur | Procédure d’utilisation             | Luc         | Sprint 2 | 22/01 | 23/01 |

## Répartition des rôles

### 1. Chef de projet / Scrum Master

* Création et gestion du **GitHub Project**
* Suivi du Kanban et de la Roadmap
* Reporting d’avancement

### 2. Développeur Python principal

* Développement des fonctionnalités cœur
* Mise à jour des issues associées

### 3. Développeur Python secondaire / Testeur

* Fonctions complémentaires
* Tests unitaires simples

### 4. Documentaliste / Testeur

* Fiches de test
* Fiche de recette
* Mini-manuel utilisateur

📝 Description du Projet : Test d'Implémentation GitHub
Ce projet sert de bac à sable (sandbox) pour tester et valider les fonctionnalités de gestion de projet natives de GitHub. L'objectif est de simuler un flux de travail réel en reliant les tâches techniques aux objectifs stratégiques à long terme.

🎯 Objectifs principaux
Centralisation du suivi : Utiliser les Issues pour documenter chaque tâche, bug ou amélioration.

Visualisation Roadmap : Exploiter l'outil GitHub Projects (v2) pour transformer les issues en une feuille de route chronologique.

Automatisation : Tester les changements d'état automatiques (ex: passer une issue en "In Progress" lors de l'ouverture d'une Pull Request).

Interconnexion : Vérifier la fluidité entre le code, les discussions et la planification globale.

🛠️ Fonctionnement du test
Issues : Chaque test unitaire est créé sous forme d'issue avec un label spécifique.

Milestones : Les issues sont regroupées par jalons pour définir des dates clés dans la Roadmap.

Project Board : Vue Kanban et vue Gantt (Roadmap) pour suivre l'avancement en temps réel.
