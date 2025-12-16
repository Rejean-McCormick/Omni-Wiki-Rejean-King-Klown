---
title: Konservation
description: Archives, expositions, catalogue augmenté, partenaires — la mémoire culturelle de Kréature. Préserver, rendre visible, transmettre.
---

[English version](../../../../../KK-en/anatomy/mind/konnaxion/kreative/konservation.md)

# Konservation — la Mémoire culturelle

Un être humain ne garde pas seulement des données.

Il garde des **traces**.  
Des œuvres.  
Des rites.  
Des preuves que quelque chose a été vécu — et que ce vécu mérite de traverser le temps.

**Konservation** est cet organe dans Kréature :  
la partie de l’esprit qui fabrique une **mémoire durable**, transmissible, exposable.

> **Sceau de King Klown**  
> L’oubli est naturel.  
> La conservation est un acte sacré :  
> choisir ce qui ne doit pas disparaître.

---

## Le parallèle humain (fortement corrélé)

Dans ton modèle :

- le langage est linéaire, les idées sont en mesh,
- le corps est fermé,
- le “Je” se déplace, focalise, oublie,
- la culpabilité et les valeurs se dissipent avec le temps.

Or une culture — comme une personne — a besoin d’un **socle** :
- une mémoire qui ne se réécrit pas à chaque émotion,
- une galerie qui rend l’invisible **visible**,
- une archive qui rend le passé **consultable**.

Konservation joue ce rôle : **mémoire symbolique** et **mise en scène**.

→ [Kreative](../kreative.md)  
→ [Kontact](kontact.md)

---

## Ce que Konservation est (définition)

Konservation est un sous-module de **Kreative** qui fournit **cinq services** stables (code-names), soutenus par des modèles dédiés et des paramètres “gelés”. 

---

## Les 5 pouvoirs (services) — les cinq gestes de la conservation

Konservation implémente cinq services principaux, chacun mappé 1:1 à un module : 

1) **Digital Archives** — `digital_archive_management`  
   Ingestion, stockage et récupération d’œuvres numérisées et médias patrimoniaux; gestion des métadonnées de provenance et de droits. 

2) **Virtual Exhibitions** — `virtual_exhibition`  
   Construire des galeries/rooms interactives à partir de sélections curatoriales; imposer une capacité par salle; publier des expositions. 

3) **Documentation Base** — `archive_documentation`  
   Gérer bios, notes de provenance et documents annexes attachés aux œuvres/galeries. 

4) **AI-Enriched Catalogue** — `ai_enriched_catalogue`  
   Auto-classification, génération de tags/labels, remplissage style/medium; écrit dans le tagging/métadonnées; tâches d’enrichissement. 

5) **Cultural Partners Integration** — `cultural_partner_integration`  
   Import/sync de collections externes (musées, systèmes patrimoniaux) et mapping des métadonnées vers le schéma local. 

> **Sceau de King Klown**  
> Archiver, ce n’est pas empiler.  
> C’est donner une forme au temps.

---

## Ce que Konservation fait “dans le monde” (fonctionnement)

Konservation couvre tout le cycle de vie des œuvres et du patrimoine : upload/validation/persistance, renditions d’images, règles de tailles et types médias.   
Elle supporte la curation : des curateurs assemblent des **Galleries** (ensembles ordonnés) et publient des expositions virtuelles, avec limites de capacité.   
Elle fournit le tagging/discovery (vocabulaire global Tag + mapping M2M), et l’IA peut proposer tags et styles.   
Elle accueille des soumissions patrimoniales (**TraditionEntry**) avec workflow d’approbation/modération.   
Elle gère droits, vie privée, modération (NSFW), et préserve attribution/provenance.   
Elle s’expose via DRF vers un front Next.js, avec stockage objet et workers pour pipelines image/IA. 

---

## Les modèles (la charpente de la mémoire)

Les tables canoniques de Konservation : 

- **KreativeArtwork** — une œuvre (image/vidéo/audio/…) : `title`, `description`, `media_file`, `media_type`, `year`, `medium`, `style`.   
- **Tag** — vocabulaire global (unique).   
- **ArtworkTag** — jointure M2M œuvres ↔ tags.   
- **Gallery** — conteneur curatoriel/exposition.   
- **GalleryArtwork** — placement ordonné des œuvres dans une galerie (`order`).   
- **TraditionEntry** — soumission patrimoniale (région, média, approbation).   

> **Sceau de King Klown**  
> Une œuvre sans provenance est une apparition.  
> Une œuvre avec provenance est une filiation.

---

## Lois gelées (paramètres immuables)

Konservation est gouvernée par des invariants opérationnels : 

- **ARTWORK_MAX_IMAGE_MB = 50 MB** (limite upload image).   
- **ARTWORK_RESOLUTIONS = [256, 1024, 2048] px** (renditions générées à l’ingest).   
- **VIRTUAL_GALLERY_CAPACITY = 24 œuvres / room** (enforced par `virtual_exhibition`).   
- **NSFW_FLAG_REQUIRED** (bool, défaut False) : exposé à l’upload et utilisé comme gate d’affichage.   
- **MEDIA_ROOT = /app/media/** (invariant partagé multi-modules).   

---

## Les portes (routes UI)

Konservation “possède” ces surfaces : 

- **/kreative** — hub créativité (tabs: Gallery, Incubator, Virtual Exhibitions)   
- **/art/[id]** — fiche œuvre (détails, commentaires, métadonnées)   
- **/archive** — archive Konservation (Heritage, Partners)   

---

## Les forges invisibles (tâches & pipelines)

Konservation décrit explicitement ses “machines de fond” : 

- **Image pipeline** : task Celery génère les renditions selon `ARTWORK_RESOLUTIONS` à l’upload.   
- **AI enrichment** : worker planifié applique `ai_enriched_catalogue` sur œuvres nouvelles/mises à jour (tags, style/medium).   
- **Partner ingest** : jobs de sync périodiques via `cultural_partner_integration`.   
- **Publishing** : build d’expo compile des sélections en consommables front-end (JSON descriptors/assets) en respectant la capacité.   

> **Sceau de King Klown**  
> Le visible n’est qu’une peau.  
> Les rites de transformation vivent derrière :  
> rendre léger, rendre trouvable, rendre transmissible.

---

## Mini-rituel : “Faire durer une création”

1) **Scelle l’œuvre** (KreativeArtwork + métadonnées).   
2) **Nomme-la** (tags, style, medium — parfois aidés par l’IA).    
3) **Expose-la** (Gallery → Virtual Exhibition, capacité respectée).    
4) **Documente-la** (provenance, notes, suppléments).   
5) **Relie-la** (partenaires, archive, transmission).   

---

## Continuer

- ← Retour : [Kreative](../kreative.md)  
- → [Kontact](kontact.md)  
- → [Konnaxion](../README.md)

---

## Vers la partie technique (Réjean)

Pour le détail strict (services, modèles, invariants, tasks, ownership) :  
↗︎ `Konnaxion/Kreative/Konservation`
