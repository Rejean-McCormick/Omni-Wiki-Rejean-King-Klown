---
title: Knowledge
description: La Bibliothèque vivante de Kréature — cataloguer, chercher, recommander, co-créer, débattre, suivre la progression. Le mesh du savoir.
---

[English version](../../../../../KK-en/anatomy/mind/konnaxion/konnected/knowledge.md)

# Knowledge — la Bibliothèque vivante

Il existe un savoir qui dort dans des pages.  
Et un savoir qui **circule**, qui **s’attache**, qui **revient** quand on en a besoin.

**Knowledge** est cette circulation.

Dans l’anatomie de Kréature, Knowledge n’est pas “un wiki de plus”.  
C’est un organe : **l’hippocampe social**, la mémoire qui classe, relie, et rend le monde apprenable.

> **Sceau de King Klown**  
> Le chaos devient connaissance quand il accepte d’être indexé.  
> La connaissance devient sagesse quand elle revient au bon moment.

---

## Ce que Knowledge est, exactement

Knowledge (KonnectED) fournit une *learning library* et sa couche sociale, structurée autour de cinq services nommés, et branchée sur deux grands parcours UX : **/learn** (catalogue, recommandations, offline) et **/course/[slug]** (lecteur de cours, progression).  

Ces cinq services (avec leurs noms de service) sont : 

1) **Bibliothèque collaborative** — `library_resource_management`   
2) **Recommandations personnalisées** — `personalized_recommendation`   
3) **Co-création** — `content_co_creation`   
4) **Forums thématiques** — `thematic_forum`   
5) **Suivi de progression** — `learning_progress_tracking`   

---

## Le parallèle humain (fortement corrélé)

Dans ta définition de l’humain, **apprendre = mapper le knowledge** (créer un mesh).  
Knowledge est précisément le moteur qui fabrique ce mesh.

### 1) La Bibliothèque collaborative
**Rôle humain :** mémoire déclarative + classement + “je sais où trouver”.

Knowledge gère une bibliothèque de ressources (CRUD, classification, publication), avec des types de contenu autorisés (enum) et un état brouillon/publication.    
Les types autorisés sont : `article`, `video`, `lesson`, `quiz`, `dataset`. 

### 2) La Recherche & la Découverte
**Rôle humain :** attention dirigée (“je cherche”) + reconnaissance (“je retrouve”).

La découverte inclut une recherche plein-texte sur titres/descriptions via PostgreSQL *tsvector* (SEARCH_BACKEND = "postgres").  

### 3) Les Recommandations personnalisées
**Rôle humain :** intuition guidée (“voici ce qui te nourrit ensuite”).

Des recommandations peuvent être générées périodiquement ou à la demande, enregistrées par utilisateur, et classées par un mélange (popularité, récence, pertinence du profil). 

### 4) La Co-création
**Rôle humain :** main + atelier + apprentissage par fabrication.

Knowledge fournit des espaces de création/édition collaborative, avec contributions versionnées ; on itère en brouillon avant publication à la bibliothèque. 

> Une limite explicite protège l’organisme : **MAX_CONTRIBUTION_DRAFTS = 10** brouillons par utilisateur. 

### 5) Les Forums thématiques
**Rôle humain :** cognition sociale (“penser avec les autres”).

Knowledge expose des forums par sujet, reliés aux ressources/cours, avec modération, et visibles dans le flux /learn. 

### 6) Le Suivi de progression
**Rôle humain :** proprioception cognitive (“où j’en suis ?”).

Le lecteur **/course/[slug]** lit/écrit des marqueurs de progression pour piloter le % de complétion, la reprise (resume) et des achievements. 

### 7) La Distribution hors-ligne
**Rôle humain :** mémoire portable (survivre au manque de réseau).

Knowledge prévoit le packaging de contenus pour environnements à faible connectivité, avec une planification hebdomadaire : `OFFLINE_PACKAGE_CRON = 0 3 * * SUN`.  

---

## Les “os” (modèles de données)

Pour rester fidèle, Knowledge repose sur des tables/modèles concrets : 

- **KnowledgeResource** : ressource canonique (article/vidéo/leçon/quiz/dataset)   
- **KnowledgeRecommendation** : recommandation pour un utilisateur   
- **LearningProgress** : progression par utilisateur et ressource (progress_percent, unique user+resource)   
- **CoCreationProject** / **CoCreationContribution** : conteneur de création + contributions   
- **ForumTopic** / **ForumPost** : sujets et posts de discussion   

---

## Pourquoi Knowledge existe dans Kréature

Parce que sans cet organe :

- l’esprit débat sur du vide,
- la conscience pèse des intuitions sans matière,
- le jugement tranche sans apprendre,
- et la mémoire (SwarmCraft) ne peut pas recoudre un récit stable.

Knowledge est la “terre” du parlement intérieur.

- → [KonnectED](../konnected.md)  
- → [Le parlement intérieur](../../../../rituels/parlement-interieur.md)

---

## Liens utiles

### Dans la même langue (FR)
- → [CertifiKation](certifikation.md)

### Vers la partie technique (Réjean)
- ↗︎ **Détails techniques : Knowledge (KOA / Konnaxion)** : `/Konnaxion/KonnectED/Knowledge.md` 
