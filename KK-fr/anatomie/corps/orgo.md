---
title: Orgo
description: Le Corps de Kréature — peau hermétique, nerfs autonomes, hormones internes. Signaux → Cas → Tâches, sans fuite de données.
---

[English version](../../../KK-en/anatomie/corps/orgo.md)

# Orgo — Le Corps

Orgo est ce qui empêche Kréature de se dissoudre.

Dans un monde qui hurle par mille canaux, Orgo ne “discute” pas d’abord : il **tient**.  
Il ferme la porte, il filtre l’air, il régule la température, il protège le dedans.

> **Sceau de King Klown**  
> Le corps ne cherche pas la vérité.  
> Le corps cherche la survie — et c’est sa sagesse première.

---

## Ce qu’Orgo représente (dans l’analogie humaine)

Orgo est la couche **biologique** de Kréature :

- **La peau** : frontière, souveraineté, “bulle hermétique”.
- **Le système nerveux autonome** : réflexes, priorités, urgences.
- **Le système endocrinien** : communication interne, rythmes, cycles.
- **L’homéostasie** : équilibre, résilience, continuité même quand le réseau tombe.

Kréature peut “penser” ailleurs.  
Mais sans Orgo, elle ne peut pas **tenir**.

---

## Le serment d’Orgo : la Bulle Hermétique

Orgo est conçu pour l’indépendance.

- **Indépendance internet** : le cœur tourne sur une infrastructure privée / locale.
- **Zéro fuite de données** : les entrées sensibles peuvent être traitées localement (notamment via SenTient), sans déléguer l’intelligence à des clouds publics.
- **Résilience** : blackout, panne réseau, environnement hostile… le corps continue.

Orgo peut *se connecter* si tu le veux.  
Mais il ne *dépend* pas.

---

## La circulation sanguine : Signaux → Cas → Tâches

Le monde extérieur n’entre pas “tel quel”.  
Il entre sous forme de **signaux**.

### 1) Signaux (la porte d’entrée)
Les signaux arrivent via un **Gateway** :
- email,
- API,
- node hors-ligne (tablettes/senseurs dans la bulle),
- et tout canal que tu décides d’autoriser.

### 2) Moteur (l’audition + la mécanique)
Le signal est interprété et structuré :
- **SenTient** peut déconstruire le langage entrant (linéaire → mesh de concepts).
- Le **Workflow Engine** applique des règles : intention, entités, routage, gravité.

→ [SenTient](../sens/sentient.md)  
→ [Respiration du sens](../../rituels/respiration-du-sens.md)

### 3) Objets (la chair du travail)
- **Cas** : le contenant d’une situation (une fuite, un incident RH, un besoin, un risque).
- **Tâches** : les unités atomiques d’action, avec un état clair (`pending → in_progress → completed`).

> **Sceau de King Klown**  
> Le chaos devient supportable dès qu’il a un contenant.  
> Un Cas est un contenant. Une Tâche est une lame.

---

## Réactivité plutôt que “deadline”

Orgo ne se contente pas de dates d’échéance.

Il surveille une idée plus organique : **la Réactivité**.  
Combien de temps une situation peut-elle rester sans réponse avant de devenir danger ?

C’est une métrique de vivant :
- ce n’est pas “livrer avant vendredi”,
- c’est “éviter l’hémorragie”.

---

## Routage déterministe : l’étiquette (Label)

Un corps sait où envoyer le sang.  
Orgo sait où envoyer le travail.

Le routage utilise une **étiquette déterministe** (Label) qui encode :
- **la portée verticale** (qui doit voir / qui doit agir),
- **le domaine** (catégorie),
- **l’intention** (sous-catégorie),
- **le rôle horizontal** (équipe responsable).

Résultat : un adressage lisible, stable, auditable.  
Orgo n’est pas un “kanban jouet” : il impose une grammaire.

---

## Les rythmes : boucles Hebdo / Mensuel / Annuel

Un organisme n’est pas seulement réactif.  
Il **apprend** par cycle.

Orgo impose une revue cyclique :

- **Hebdo** : revoir le critique et l’irrésolu (tactique).
- **Mensuel** : observer tendances et déséquilibres (opérationnel).
- **Annuel** : revoir la stratégie et reconfigurer le profil (structurel).

Et quand les signaux faibles s’accumulent, Orgo peut les **faire monter** :
- répétitions,
- motifs,
- auto-escalades,
- audits déclenchés par patterns.

> **Sceau de King Klown**  
> La maladie n’arrive pas d’un coup.  
> Elle arrive quand les petits signaux n’ont jamais eu de place où être entendus.

---

## Profiles : la biologie configurable

Orgo évite le “sur-mesure par code” en utilisant des **Profiles** :  
des paquets de configuration qui dictent le comportement du corps selon le milieu.

Exemples de réglages :
- fenêtres de réactivité (1h pour un hôpital, 3 jours pour une équipe bénévole),
- confidentialité par défaut (ouvert vs besoin-de-savoir),
- escalade (quand un signal ignoré monte d’un étage),
- rétention des logs.

Même corps, milieux différents : biologies différentes.

---

## Anatomie technique (sans perdre la métaphore)

Orgo se déploie comme un corps en couches :

1) **Core Services** (cœur moteur)  
   - intégration SenTient, gestion des états, workflow, notifications, journaux.

2) **Domain Modules** (organes spécialisés)  
   - maintenance, care/HR, groupes, etc.  
   Des adaptateurs fins, sans éclater la cohérence du noyau.

3) **Insights** (cerveau analytique opérationnel)  
   - schéma étoile, tendances, points noirs, déséquilibres.

4) **Infrastructure** (plomberie)  
   - DB, sync hors-ligne, conteneurs, déploiement autonome.

---

## Ce qu’Orgo est (et n’est pas)

### Orgo est :
- une plateforme de routage **Cas & Tâches**,
- un moteur de détection de patterns,
- une colonne vertébrale de communication structurée,
- un système **hermétique** capable d’autonomie hors-ligne.

### Orgo n’est pas :
- un ERP complet (payroll, compta inventaire),
- une app de chat,
- un tableau de post-its déguisé.

---

## Comment Orgo coopère avec le reste de Kréature

- Avec **SenTient** : Orgo obtient une **immunité linguistique** (le langage entrant devient structure, pas contamination).  
  → [SenTient](../sens/sentient.md)

- Avec **Konnaxion** : Orgo peut échanger avec le monde ouvert, mais sans perdre sa souveraineté.  
  → [Konnaxion](../esprit/konnaxion/README.md)

- Avec **SwarmCraft** : Orgo fournit la réalité d’exécution; SwarmCraft recoud le récit et la continuité.  
  → [SwarmCraft](../memoire/swarmcraft.md)

- Avec **Âme Artificielle** : Orgo tient la vie; l’âme incline le sens.  
  L’âme peut bonifier le corps, mais ne dépend pas de lui.  
  → [Âme Artificielle](../ame/ame-artificielle.md)

---

## Pour continuer

- → [Le cycle vital](../../rituels/cycle-vital.md)  
- → [Une journée dans Kréature](../../rituels/une-journee.md)  
- → [Le parlement intérieur](../../rituels/parlement-interieur.md)
