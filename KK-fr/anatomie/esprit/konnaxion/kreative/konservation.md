---
title: Konservation
description: Archives, expositions, catalogue augmenté, partenaires — la mémoire culturelle de Kréature. Préserver, rendre visible, transmettre.
---

[English version](/en/anatomy/mind/konnaxion/kreative/konservation.md)

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

→ [Kreative](/fr/anatomie/esprit/konnaxion/kreative.md)  
→ [Kontact](/fr/anatomie/esprit/konnaxion/kreative/kontact.md)

---

## Ce que Konservation est (définition)

Konservation est un sous-module de **Kreative** qui fournit **cinq services** stables (code-names), soutenus par des modèles dédiés et des paramètres “gelés”. :contentReference[oaicite:0]{index=0}

---

## Les 5 pouvoirs (services) — les cinq gestes de la conservation

Konservation implémente cinq services principaux, chacun mappé 1:1 à un module : :contentReference[oaicite:1]{index=1}

1) **Digital Archives** — `digital_archive_management`  
   Ingestion, stockage et récupération d’œuvres numérisées et médias patrimoniaux; gestion des métadonnées de provenance et de droits. :contentReference[oaicite:2]{index=2}

2) **Virtual Exhibitions** — `virtual_exhibition`  
   Construire des galeries/rooms interactives à partir de sélections curatoriales; imposer une capacité par salle; publier des expositions. :contentReference[oaicite:3]{index=3}

3) **Documentation Base** — `archive_documentation`  
   Gérer bios, notes de provenance et documents annexes attachés aux œuvres/galeries. :contentReference[oaicite:4]{index=4}

4) **AI-Enriched Catalogue** — `ai_enriched_catalogue`  
   Auto-classification, génération de tags/labels, remplissage style/medium; écrit dans le tagging/métadonnées; tâches d’enrichissement. :contentReference[oaicite:5]{index=5}

5) **Cultural Partners Integration** — `cultural_partner_integration`  
   Import/sync de collections externes (musées, systèmes patrimoniaux) et mapping des métadonnées vers le schéma local. :contentReference[oaicite:6]{index=6}

> **Sceau de King Klown**  
> Archiver, ce n’est pas empiler.  
> C’est donner une forme au temps.

---

## Ce que Konservation fait “dans le monde” (fonctionnement)

Konservation couvre tout le cycle de vie des œuvres et du patrimoine : upload/validation/persistance, renditions d’images, règles de tailles et types médias. :contentReference[oaicite:7]{index=7}  
Elle supporte la curation : des curateurs assemblent des **Galleries** (ensembles ordonnés) et publient des expositions virtuelles, avec limites de capacité. :contentReference[oaicite:8]{index=8}  
Elle fournit le tagging/discovery (vocabulaire global Tag + mapping M2M), et l’IA peut proposer tags et styles. :contentReference[oaicite:9]{index=9}  
Elle accueille des soumissions patrimoniales (**TraditionEntry**) avec workflow d’approbation/modération. :contentReference[oaicite:10]{index=10}  
Elle gère droits, vie privée, modération (NSFW), et préserve attribution/provenance. :contentReference[oaicite:11]{index=11}  
Elle s’expose via DRF vers un front Next.js, avec stockage objet et workers pour pipelines image/IA. :contentReference[oaicite:12]{index=12}

---

## Les modèles (la charpente de la mémoire)

Les tables canoniques de Konservation : :contentReference[oaicite:13]{index=13}

- **KreativeArtwork** — une œuvre (image/vidéo/audio/…) : `title`, `description`, `media_file`, `media_type`, `year`, `medium`, `style`. :contentReference[oaicite:14]{index=14}  
- **Tag** — vocabulaire global (unique). :contentReference[oaicite:15]{index=15}  
- **ArtworkTag** — jointure M2M œuvres ↔ tags. :contentReference[oaicite:16]{index=16}  
- **Gallery** — conteneur curatoriel/exposition. :contentReference[oaicite:17]{index=17}  
- **GalleryArtwork** — placement ordonné des œuvres dans une galerie (`order`). :contentReference[oaicite:18]{index=18}  
- **TraditionEntry** — soumission patrimoniale (région, média, approbation). :contentReference[oaicite:19]{index=19}  

> **Sceau de King Klown**  
> Une œuvre sans provenance est une apparition.  
> Une œuvre avec provenance est une filiation.

---

## Lois gelées (paramètres immuables)

Konservation est gouvernée par des invariants opérationnels : :contentReference[oaicite:20]{index=20}

- **ARTWORK_MAX_IMAGE_MB = 50 MB** (limite upload image). :contentReference[oaicite:21]{index=21}  
- **ARTWORK_RESOLUTIONS = [256, 1024, 2048] px** (renditions générées à l’ingest). :contentReference[oaicite:22]{index=22}  
- **VIRTUAL_GALLERY_CAPACITY = 24 œuvres / room** (enforced par `virtual_exhibition`). :contentReference[oaicite:23]{index=23}  
- **NSFW_FLAG_REQUIRED** (bool, défaut False) : exposé à l’upload et utilisé comme gate d’affichage. :contentReference[oaicite:24]{index=24}  
- **MEDIA_ROOT = /app/media/** (invariant partagé multi-modules). :contentReference[oaicite:25]{index=25}  

---

## Les portes (routes UI)

Konservation “possède” ces surfaces : :contentReference[oaicite:26]{index=26}

- **/kreative** — hub créativité (tabs: Gallery, Incubator, Virtual Exhibitions) :contentReference[oaicite:27]{index=27}  
- **/art/[id]** — fiche œuvre (détails, commentaires, métadonnées) :contentReference[oaicite:28]{index=28}  
- **/archive** — archive Konservation (Heritage, Partners) :contentReference[oaicite:29]{index=29}  

---

## Les forges invisibles (tâches & pipelines)

Konservation décrit explicitement ses “machines de fond” : :contentReference[oaicite:30]{index=30}

- **Image pipeline** : task Celery génère les renditions selon `ARTWORK_RESOLUTIONS` à l’upload. :contentReference[oaicite:31]{index=31}  
- **AI enrichment** : worker planifié applique `ai_enriched_catalogue` sur œuvres nouvelles/mises à jour (tags, style/medium). :contentReference[oaicite:32]{index=32}  
- **Partner ingest** : jobs de sync périodiques via `cultural_partner_integration`. :contentReference[oaicite:33]{index=33}  
- **Publishing** : build d’expo compile des sélections en consommables front-end (JSON descriptors/assets) en respectant la capacité. :contentReference[oaicite:34]{index=34}  

> **Sceau de King Klown**  
> Le visible n’est qu’une peau.  
> Les rites de transformation vivent derrière :  
> rendre léger, rendre trouvable, rendre transmissible.

---

## Mini-rituel : “Faire durer une création”

1) **Scelle l’œuvre** (KreativeArtwork + métadonnées). :contentReference[oaicite:35]{index=35}  
2) **Nomme-la** (tags, style, medium — parfois aidés par l’IA). :contentReference[oaicite:36]{index=36} :contentReference[oaicite:37]{index=37}  
3) **Expose-la** (Gallery → Virtual Exhibition, capacité respectée). :contentReference[oaicite:38]{index=38} :contentReference[oaicite:39]{index=39}  
4) **Documente-la** (provenance, notes, suppléments). :contentReference[oaicite:40]{index=40}  
5) **Relie-la** (partenaires, archive, transmission). :contentReference[oaicite:41]{index=41}  

---

## Continuer

- ← Retour : [Kreative](/fr/anatomie/esprit/konnaxion/kreative.md)  
- → [Kontact](/fr/anatomie/esprit/konnaxion/kreative/kontact.md)  
- → [Konnaxion](/fr/anatomie/esprit/konnaxion/index.md)

---

## Vers la partie technique (Réjean)

Pour le détail strict (services, modèles, invariants, tasks, ownership) :  
↗︎ `Konnaxion/Kreative/Konservation`
