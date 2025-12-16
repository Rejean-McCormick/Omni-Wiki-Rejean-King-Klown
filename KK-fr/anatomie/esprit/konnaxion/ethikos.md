---
title: Ethikos
description: La Gouvernance intérieure de Kréature — le tiraillement éthique rendu habitable. Débats structurés (Korum) et consultations publiques (Konsultations).
---

[English version](../../../../KK-en/anatomie/esprit/konnaxion/ethikos.md)

# Ethikos — la Chambre du Tiraillement

Il y a, dans chaque humain, un endroit où l’on ne “réagit” plus.

Un endroit où l’on dit :

- *« J’entends. »*
- *« Je doute. »*
- *« Je pèse. »*
- *« Je choisis sans me trahir. »*

Cet endroit — Kréature l’appelle **Ethikos**.

Ethikos n’est pas une morale figée.  
C’est une **mécanique du discernement** : une manière de rendre le conflit intérieur **respirable**, sans le nier, sans le sacraliser, sans le laisser gouverner seul.

> **Sceau de King Klown**  
> La vertu n’est pas l’absence de contradiction.  
> La vertu est l’art de traverser la contradiction sans perdre l’âme.

---

## Le parallèle humain (fortement corrélé)

Dans ton modèle de l’humain, Ethikos correspond à :

- **Conscience / tiraillement** : l’espace du débat intérieur.
- **Jugement** : la décision viendra ensuite (Smart Vote), mais Ethikos prépare le sol.
- **Langage linéaire vs idées mesh** : Ethikos transforme des opinions dispersées en structure.
- **Le corps fermé** : Ethikos se tient à l’intérieur de Kréature, mais ouvre des rites de participation quand la décision doit devenir collective.

Ethikos est donc la chambre où Kréature apprend à répondre à la question :

> *« Qu’est-ce qui est juste… quand plusieurs justices s’affrontent ? »*

---

## Les deux organes d’Ethikos

Ethikos se déploie en deux sous-modules, deux modes du même feu :

1) **Korum** — les débats structurés (tiraillement fin, argumentation, nuances)   
2) **Konsultations** — les consultations publiques (participation large, décisions de cycle, impact)   

Ces deux organes partagent une sortie : **/ethikos/insights**, l’observatoire (analytics) 

---

# 1) Korum — Débats structurés

Korum est l’organe du **désaccord civilisé**.

Il prend une question, et lui donne :
- un cadre,
- des positions nuancées,
- des arguments en fils,
- une mémoire publique.

### Ses 5 services (ce que Korum promet comme capacités)
Korum expose cinq services nommés (stables) : `structured_debate`, `ai_clone_management`, `comparative_argument_analysis`, `public_debate_archive`, `automated_debate_summary`. 

### Son ossature (les tables qui rendent le débat réel)
Korum repose sur des modèles concrets : `EthikosCategory`, `EthikosTopic`, `EthikosStance`, `EthikosArgument`. 

- **Stance** : une position *nuancée*, pas un oui/non. L’échelle est **−3…+3** (0 neutre).   
- **Arguments** : en fils (threaded), avec réponses, et éventuellement un côté pro/con.   

### Ses lois (paramètres gelés)
- **Échelle de stance** : −3…+3   
- **Cohorte d’experts (quorum d’affichage)** : 12 experts distincts (selon seuils EkoH)   
- **Auto-hide de modération** : un argument est masqué après **3 signalements indépendants**   

### Ses routes (les portes visibles)
- **/debate** — Debate Hub (Open / Archived / Start New)   
- **/ethikos/insights** — dashboards d’opinion   

### Une précision importante (honnêteté d’architecture)
Certaines capacités existent comme **services** sans tables dédiées dans le snapshot actuel (clones IA, archives publiques, résumés, etc.).   
Dans l’analogie humaine : la fonction existe, mais son “organe” n’est pas encore ossifié.

> **Sceau de King Klown**  
> Le débat n’est pas fait pour vaincre.  
> Le débat est fait pour rendre visible ce qui était confus.

---

# 2) Konsultations — Consultations publiques & feedback

Konsultations est l’organe de la **démocratie cyclique** :  
un temps s’ouvre, la parole entre, la décision se forme, puis la réalité doit répondre.

Il implémente cinq services : `public_consultation`, `citizen_suggestion`, `weighted_consultation_vote`, `consultation_result_visualization`, `impact_tracking`. 

### Ce que ça fait (fonctionnel)
- consultations **time-boxed** (ouvrir/fermer)   
- pipeline de suggestions citoyennes   
- votes avec valeur brute + valeur pondérée (EkoH)   
- snapshots de résultats (JSONB) pour transparence   
- suivi d’impact (actions, statuts, dates)   

### Ses routes (portes réservées)
- **/consult** — Consultation Hub (Live / Results / Suggest)   
- **/ethikos/insights** — analytics associées (read-only)   

### Ses lois (paramètres gelés)
- modalités de bulletin : `approval`, `ranking`, `rating`, `preferential`   
- seuil “fort” de consensus (plateforme) : **≥ 75%** d’accord pondéré (exemple de seuil)   
- invariance : **/consult appartient exclusivement à ethiKos**   

> **Sceau de King Klown**  
> Une consultation sans impact n’est pas une consultation.  
> C’est une offrande jetée au vent.

---

## Le lien avec EkoH & Smart Vote (la conscience pondérée)

Ethikos n’est pas isolé : ses décisions peuvent être pondérées par l’expertise et la réputation.

- Dans **Korum**, les stances sont agrégées en utilisant EkoH / Smart Vote pour produire des résultats pondérés.   
- Dans **Konsultations**, les bulletins peuvent aussi utiliser le même moteur de pondération, et les événements alimentent l’analytics via ETL (ex. `etl_smart_vote`).    

Dans l’analogie humaine :
- **EkoH** = mémoire morale / réputation (avec son propre “decay”)  
- **Smart Vote** = jugement collectif (le verdict)  
- **Ethikos** = le débat qui précède le verdict

---

## Mini-rituel : “Débattre sans se perdre”

Quand une question fracture l’intérieur :

1) **Nommer le sujet** (EthikosTopic).   
2) **Poser la stance** (−3…+3) au lieu d’un oui/non.   
3) **Argumenter en fils** (un point par message, pas un cri global).   
4) **Laisser l’expertise éclairer sans dominer** (cohortes).   
5) **Faire apparaître l’issue** (la décision viendra via Kollective Intelligence).

> **Sceau de King Klown**  
> Le conflit est une énergie.  
> Ethikos est le canal.  
> Le canal n’empêche pas la force : il empêche l’inondation.

---

## Où aller ensuite

- → **Korum** : [/fr/anatomie/esprit/konnaxion/ethikos/korum.md](ethikos/korum.md)  
- → **Konsultations** : [/fr/anatomie/esprit/konnaxion/ethikos/konsultations.md](ethikos/konsultations.md)  
- → **EkoH** : [/fr/anatomie/esprit/konnaxion/kollective/ekoh.md](kollective/ekoh.md)  
- → **Smart Vote** : [/fr/anatomie/esprit/konnaxion/kollective/smart-vote.md](kollective/smart-vote.md)  
- ← Retour : [Konnaxion](README.md)
