---
title: Knowledge
description: La Bibliothèque vivante de Kréature — cataloguer, chercher, recommander, co-créer, débattre, suivre la progression. Le mesh du savoir.
---

[English version](/en/anatomy/mind/konnaxion/konnected/knowledge.md)

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

Knowledge (KonnectED) fournit une *learning library* et sa couche sociale, structurée autour de cinq services nommés, et branchée sur deux grands parcours UX : **/learn** (catalogue, recommandations, offline) et **/course/[slug]** (lecteur de cours, progression). :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

Ces cinq services (avec leurs noms de service) sont : :contentReference[oaicite:2]{index=2}

1) **Bibliothèque collaborative** — `library_resource_management` :contentReference[oaicite:3]{index=3}  
2) **Recommandations personnalisées** — `personalized_recommendation` :contentReference[oaicite:4]{index=4}  
3) **Co-création** — `content_co_creation` :contentReference[oaicite:5]{index=5}  
4) **Forums thématiques** — `thematic_forum` :contentReference[oaicite:6]{index=6}  
5) **Suivi de progression** — `learning_progress_tracking` :contentReference[oaicite:7]{index=7}  

---

## Le parallèle humain (fortement corrélé)

Dans ta définition de l’humain, **apprendre = mapper le knowledge** (créer un mesh).  
Knowledge est précisément le moteur qui fabrique ce mesh.

### 1) La Bibliothèque collaborative
**Rôle humain :** mémoire déclarative + classement + “je sais où trouver”.

Knowledge gère une bibliothèque de ressources (CRUD, classification, publication), avec des types de contenu autorisés (enum) et un état brouillon/publication. :contentReference[oaicite:8]{index=8} :contentReference[oaicite:9]{index=9}  
Les types autorisés sont : `article`, `video`, `lesson`, `quiz`, `dataset`. :contentReference[oaicite:10]{index=10}

### 2) La Recherche & la Découverte
**Rôle humain :** attention dirigée (“je cherche”) + reconnaissance (“je retrouve”).

La découverte inclut une recherche plein-texte sur titres/descriptions via PostgreSQL *tsvector* (SEARCH_BACKEND = "postgres"). :contentReference[oaicite:11]{index=11} :contentReference[oaicite:12]{index=12}

### 3) Les Recommandations personnalisées
**Rôle humain :** intuition guidée (“voici ce qui te nourrit ensuite”).

Des recommandations peuvent être générées périodiquement ou à la demande, enregistrées par utilisateur, et classées par un mélange (popularité, récence, pertinence du profil). :contentReference[oaicite:13]{index=13}

### 4) La Co-création
**Rôle humain :** main + atelier + apprentissage par fabrication.

Knowledge fournit des espaces de création/édition collaborative, avec contributions versionnées ; on itère en brouillon avant publication à la bibliothèque. :contentReference[oaicite:14]{index=14}

> Une limite explicite protège l’organisme : **MAX_CONTRIBUTION_DRAFTS = 10** brouillons par utilisateur. :contentReference[oaicite:15]{index=15}

### 5) Les Forums thématiques
**Rôle humain :** cognition sociale (“penser avec les autres”).

Knowledge expose des forums par sujet, reliés aux ressources/cours, avec modération, et visibles dans le flux /learn. :contentReference[oaicite:16]{index=16}

### 6) Le Suivi de progression
**Rôle humain :** proprioception cognitive (“où j’en suis ?”).

Le lecteur **/course/[slug]** lit/écrit des marqueurs de progression pour piloter le % de complétion, la reprise (resume) et des achievements. :contentReference[oaicite:17]{index=17}

### 7) La Distribution hors-ligne
**Rôle humain :** mémoire portable (survivre au manque de réseau).

Knowledge prévoit le packaging de contenus pour environnements à faible connectivité, avec une planification hebdomadaire : `OFFLINE_PACKAGE_CRON = 0 3 * * SUN`. :contentReference[oaicite:18]{index=18} :contentReference[oaicite:19]{index=19}

---

## Les “os” (modèles de données)

Pour rester fidèle, Knowledge repose sur des tables/modèles concrets : :contentReference[oaicite:20]{index=20}

- **KnowledgeResource** : ressource canonique (article/vidéo/leçon/quiz/dataset) :contentReference[oaicite:21]{index=21}  
- **KnowledgeRecommendation** : recommandation pour un utilisateur :contentReference[oaicite:22]{index=22}  
- **LearningProgress** : progression par utilisateur et ressource (progress_percent, unique user+resource) :contentReference[oaicite:23]{index=23}  
- **CoCreationProject** / **CoCreationContribution** : conteneur de création + contributions :contentReference[oaicite:24]{index=24}  
- **ForumTopic** / **ForumPost** : sujets et posts de discussion :contentReference[oaicite:25]{index=25}  

---

## Pourquoi Knowledge existe dans Kréature

Parce que sans cet organe :

- l’esprit débat sur du vide,
- la conscience pèse des intuitions sans matière,
- le jugement tranche sans apprendre,
- et la mémoire (SwarmCraft) ne peut pas recoudre un récit stable.

Knowledge est la “terre” du parlement intérieur.

- → [KonnectED](/fr/anatomie/esprit/konnaxion/konnected.md)  
- → [Le parlement intérieur](/fr/rituels/parlement-interieur.md)

---

## Liens utiles

### Dans la même langue (FR)
- → [CertifiKation](/fr/anatomie/esprit/konnaxion/konnected/certifikation.md)

### Vers la partie technique (Réjean)
- ↗︎ **Détails techniques : Knowledge (KOA / Konnaxion)** : `/Konnaxion/KonnectED/Knowledge.md` :contentReference[oaicite:26]{index=26}
