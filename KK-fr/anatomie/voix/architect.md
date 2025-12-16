---
title: Architect
description: La Voix de Kréature — transformer un mesh sémantique en phrases humaines, multilingues, testables. Le larynx algorithmique.
---

[English version](../../../KK-en/anatomy/voice/architect.md)

# Architect — la Voix (le larynx algorithmique)

Il y a une distance immense entre **comprendre** et **dire**.

Comprendre peut rester un nuage interne — un *mesh* de concepts et de liens.  
Dire exige une traversée : ordre, grammaire, souffle, rythme, articulation.

**Architect** (Abstract Wiki Architect) est la Voix de Kréature : un outil de génération de langage naturel (NLG) **familial**, **data-driven**, conçu pour rendre du savoir abstrait en texte dans de nombreuses langues. 

> **Sceau de King Klown**  
> Une idée sans voix est une étoile dans une gorge fermée.  
> Architect est l’ouverture — le passage de l’intérieur vers le monde.

---

## Le parallèle humain (fortement corrélé)

Dans l’humain, le langage est linéaire, alors que la pensée est maillée.

Pour parler, il faut un appareil :

- un **larynx** (production),
- une **morphologie** (accords, flexions, genres, cas),
- des **constructions** (patrons de phrases),
- un **lexique** (formes et traits des mots),
- une **logique discursive** (pronoms, topic/comment, micro-cohérence).

Architect est précisément structuré en ces couches — séparées, mais interopérables.  

Si **SenTient** est l’oreille + filtre immunitaire du langage (entrée),  
Architect est la **bouche + grammaire** (sortie).

→ [SenTient](../sens/sentient.md)

---

## Pourquoi Architect existe dans l’écosystème

Pour rendre Konnaxion “disponible à tous”, il fallait une façon de générer des textes multilingues à partir de données abstraites — sans écrire “un script par langue”. 

Architect répond à ça en organisant la NLG comme :

- ~15 **engines** partagés par familles de langues,  
- des **configuration cards** par langue,  
- une bibliothèque de **constructions** (patrons de phrases),  
- un **lexicon subsystem** (avec ponts vers Wikidata / lexèmes),  
- un petit inventaire de **semantic frames**,  
- et une **QA factory** (tests). 

---

## Comment la Voix est construite (la gorge en couches)

L’architecture résumée est explicite :

> **Engines (families)** + **Configs (languages)** + **Constructions (sentence patterns)**  
> + **Lexica** + **Frames (semantics)** + **Discourse** + **Router/API** 

### 1) Engines de familles — “les muscles profonds”
Chaque engine connaît la logique d’une famille (accords, genres, classes nominales, cas…), sans hardcoder des terminaisons : il consulte config + lexique. 

### 2) Constructions — “les gestes de phrase”
Les constructions sont des patrons cross-linguistiques (“X est un Y”, “X a Y”, “Il y a Y dans X”, etc.) et délèguent la réalisation à la morphologie + lexique. 

### 3) Lexique — “les dents et la matière”
Le lexique encode lemma/POS, traits (genre, nombre…), flags (human, nationality…), liens (fem/masc, sing/plur), IDs éventuels (Wikidata, lexèmes). 

### 4) Frames sémantiques — “le mesh propre”
Architect prend en entrée des frames (Entity, Event, etc.) et garde la sémantique proche d’Abstract Wikipedia/Wikifunctions. 

### 5) Discours — “le rythme”
Une couche de discours gère topic/pronoms/multi-sentences courtes (micro-cohérence). 

### 6) Router / API — “la bouche publique”
Un router charge profil de langue + lexique, choisit engine + constructions, retourne la chaîne de surface.   
Une API NLG publique expose `generate_bio(...)` / `generate(...)` et retourne un `GenerationResult` (texte final, phrases, debug), en cachant la plomberie interne. 

---

## QA factory — la voix qui se corrige

Architect est conçu autour de suites de tests et checks de régression : datasets CSV, générateur de suite, runner, QA lexique (couverture, validation schéma). 

Dans l’analogie :  
c’est l’oreille interne de la voix — la capacité à détecter les fautes et stabiliser le timbre.

---

## Les liens internes de Kréature

- **Entrée (oreilles / filtre)** : [SenTient](../sens/sentient.md)
- **Vision / navigation** : [Ariane](../sens/ariane.md)
- **Narratif long (histoire)** : [SwarmCraft](../narratif/swarmcraft.md)
- **Esprit (débat/jugement/apprentissage)** : [Konnaxion](../esprit/konnaxion/README.md)

> **Sceau de King Klown**  
> SenTient reçoit.  
> Architect prononce.  
> Entre les deux : l’esprit assemble le mesh.

---

## Vers la partie technique (Réjean)

Pour la documentation technique complète d’Architect (engines, morphology, constructions, lexicon, frames, router, API, QA, hosting) :  
↗︎ `/abstract-wiki-architect/Wiki-Architect-Hub.md` 
