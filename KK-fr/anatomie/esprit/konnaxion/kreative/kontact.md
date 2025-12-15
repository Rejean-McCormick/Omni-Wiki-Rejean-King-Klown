---
title: Kontact
description: Réseau, rencontres, opportunités, confiance — le tissu relationnel de Kréature. Profils, matching, salles de co-création, appels, endorsements.
---

[English version](../../../../../KK-en/anatomy/mind/konnaxion/kreative/kontact.md)

# Kontact — le Tissu relationnel

Un être vivant peut être brillant… et mourir d’isolement.

Chez l’humain, il existe un organe invisible :
un ensemble de fils tendus entre les personnes —  
confiance, réputation, affinités, rencontres, invitations, promesses tenues.

**Kontact** est ce tissu dans Kréature :  
la partie de la Culture qui cesse d’être archive, pour devenir **réseau vivant**.

> **Sceau de King Klown**  
> Une communauté n’est pas une foule.  
> C’est une mémoire partagée de qui a été digne de confiance —  
> et de qui a su bâtir avec les autres.

---

## Le parallèle humain (fortement corrélé)

Dans ton modèle :

- le corps est fermé (on ne “sent” pas directement l’autre),
- le langage transige,
- l’esprit débat et choisit,
- puis il faut **entrer en relation** et **agir avec**.

Kontact correspond à ce que l’humain possède de plus déterminant, après la pensée :
- la capacité de se **lier** (sans se confondre),
- de reconnaître des affinités,
- de créer des espaces où l’on peut co-créer,
- de faire circuler des opportunités,
- et de laisser des marques de confiance.

Kontact est donc un organe de **rencontre structurée**, pas une simple messagerie.

---

## Ce que Kontact est (définition et routes)

Kontact est un sous-module de **Kreative** et possède explicitement l’ownership UI/API sur deux routes : **/connect** et **/profile/[user]**. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

- **/connect** : People, Opportunities, Workspace  
- **/profile/[user]** : profil public (portfolio, tags, signaux)

> Dans la mythologie Kréature :  
> **/profile** est le visage. **/connect** est la place publique.

---

## Les 5 fonctions (services) — les cinq nerfs du lien

Kontact délivre cinq services “canon” (code-names stables), chacun mappé 1:1 à un module de service (consommé par DRF views et tâches Celery). :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3}

### 1) Professional Profiles — `professional_profile`
Profils publics riches : bio, skills, liens de portfolio. Intégration directe avec artworks et tags pour la découverte. :contentReference[oaicite:4]{index=4}

### 2) Intelligent Matching — `intelligent_matching`
Recommande des personnes à suivre/contacter ou à inviter en collaboration, via recouvrement skills/tags + signaux d’activité. EkoH (et même Smart Vote) peuvent être utilisés *optionnellement* comme signaux contextuels. :contentReference[oaicite:5]{index=5} :contentReference[oaicite:6]{index=6}

### 3) Collaboration Workspaces — `collaboration_workspace`
Salles légères (chat/notes/canvas) pour se rencontrer, planifier et co-créer; réutilise l’infra temps réel. :contentReference[oaicite:7]{index=7}

### 4) Opportunities Board — `opportunity_announcement`
Publier/consulter des résidences, expositions, appels, emplois; filtrable par tags, région, dates. :contentReference[oaicite:8]{index=8}

### 5) Reviews & Endorsements — `partner_recommendation`
Endorsements/ratings post-engagement pour établir la confiance entre collaborateurs/hôtes; surfaced sur les profils. :contentReference[oaicite:9]{index=9} :contentReference[oaicite:10]{index=10}

> **Sceau de King Klown**  
> Le réseau sans confiance devient bruit.  
> La confiance sans trace devient mythe.  
> Kontact fait de la trace un lien.

---

## Fonctions back-end (la mécanique réelle)

Kontact documente explicitement ce qu’il opère en coulisses : :contentReference[oaicite:11]{index=11}

- **Profiles & portfolios** : APIs read/write pour profils, reliés aux assets créatifs existants (artworks, tags). :contentReference[oaicite:12]{index=12}  
- **People matching** : ranking top-N, tunable, basé sur overlap skills/tags + activité, avec signaux optionnels EkoH/Smart Vote quand pertinent. :contentReference[oaicite:13]{index=13}  
- **Real-time meetups** : rooms éphémères DM/groupe via Channels/Redis; cap participants enforce à l’exécution. :contentReference[oaicite:14]{index=14}  
- **Opportunity lifecycle** : CRUD postings (type, location, dates, attachments), listing/search, statut (open/closed/filled). :contentReference[oaicite:15]{index=15}  
- **Trust signals** : endorsements structurés après une session/engagement, visibles sur profils. :contentReference[oaicite:16]{index=16}  

---

## Modèles (ce que Kontact “pose” dans le monde)

Le référentiel DB cite explicitement **CollabSession** sous Kontact (les autres objets peuvent réutiliser core tables ou être au niveau app). :contentReference[oaicite:17]{index=17} :contentReference[oaicite:18]{index=18}

### CollabSession — la chambre de co-création
Une session collaborative temps réel (networking/co-creation room) : `id`, `name`, `host`, `session_type`, `started_at`, `ended_at`, `final_artwork` (nullable). :contentReference[oaicite:19]{index=19}

### Réutilisations (portfolio & discovery)
Kontact réutilise explicitement :
- **KreativeArtwork** (items de portfolio surfacés sur profils, read-only côté Kontact) :contentReference[oaicite:20]{index=20}  
- **Tag / ArtworkTag** (skills/genre tags pour discovery et matching) :contentReference[oaicite:21]{index=21}  

> Traduction mythique :  
> **KreativeArtwork** est la preuve.  
> **Tag** est le langage du clan.  
> **CollabSession** est le foyer où l’on se reconnaît.

---

## Configuration gelée (les lois du lieu)

Certaines règles sont fixes et structurantes : :contentReference[oaicite:22]{index=22}

- **COLLAB_CANVAS_MAX_USERS = 6** : 6 éditeurs simultanés dans une room temps réel. :contentReference[oaicite:23]{index=23}  
- **MEDIA_ROOT = /app/media/** : attachments partagés (invariant cross-modules). :contentReference[oaicite:24]{index=24}  
- **Routes réservées** : `/connect` et `/profile/[user]` sont possédées par Kontact; les onglets internes ne créent pas de nouvelles routes top-level. :contentReference[oaicite:25]{index=25}  

> **Sceau de King Klown**  
> Sans limites, une salle devient un couloir.  
> Sans route claire, un réseau devient un labyrinthe.

---

## Ponts vers le reste de Kréature

### Vers Konservation (culture conservée)
Kontact fait circuler les liens; Konservation fait durer les œuvres.

→ [Konservation](konservation.md)

### Vers EkoH / Smart Vote (confiance pondérée, signaux d’expertise)
Le matching peut intégrer EkoH/Smart Vote comme signaux optionnels (quand pertinent). :contentReference[oaicite:26]{index=26}

→ [EkoH](../kollective/ekoh.md)  
→ [Smart Vote](../kollective/smart-vote.md)

### Vers keenKonnect (du lien au chantier)
Quand la rencontre devient projet, on bascule vers les espaces de construction.

→ [keenKonnect](../keen-konnect.md)

---

## Mini-rituel : “Devenir trouvable, puis devenir fiable”

1) **Rends ton profil lisible** (bio, skills, portfolio). :contentReference[oaicite:27]{index=27}  
2) **Tague ton œuvre** (pour être matché sans te vendre). :contentReference[oaicite:28]{index=28}  
3) **Entre dans une CollabSession** (rencontre → co-création). :contentReference[oaicite:29]{index=29}  
4) **Cherche ou publie une opportunité** (open/closed/filled). :contentReference[oaicite:30]{index=30}  
5) **Laisse une recommandation** après engagement (la confiance devient trace). :contentReference[oaicite:31]{index=31}  

---

## Continuer

- ← Retour : [Kreative](../kreative.md)  
- → [Konservation](konservation.md)  
- → [keenKonnect](../keen-konnect.md)

---

## Vers la partie technique (Réjean)

Pour la fiche technique (services, modèles, invariants, stack DRF + Channels + Redis) :  
↗︎ `Konnaxion/Kreative/Kontact`
