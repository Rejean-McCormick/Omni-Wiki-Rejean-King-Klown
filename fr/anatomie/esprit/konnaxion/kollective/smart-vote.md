---
title: Smart Vote
description: Le Jugement de Kréature — vote pondéré, consensus, seuils, modalités. Transformer le débat en décision traçable.
---

[English version](/en/anatomy/mind/konnaxion/kollective/smart-vote.md)

# Smart Vote — le Jugement (consensus pondéré)

Le débat est un feu.  
La conscience est une gravité.  
Mais il manque encore une chose, pour qu’un être puisse vivre :

**le moment où l’on tranche.**

Smart Vote est ce moment.

Il ne prétend pas être la vérité.  
Il est l’acte de choisir une trajectoire — d’effondrer des possibles en une direction, assez claire pour devenir action.

> **Sceau de King Klown**  
> Décider, c’est accepter une perte :  
> toutes les routes qu’on ne prendra pas.  
> Smart Vote est l’art de choisir sans mutiler l’âme.

---

## Le parallèle humain (fortement corrélé)

Dans ton modèle de l’humain :

- conscience/culpabilité se souvient du bien et du mal,
- débat éthique met en tension,
- jugement choisit,
- émotions et logique sont deux pieds / deux ailes.

Smart Vote correspond exactement à la fonction **Jugement** :

- prendre des positions (votes / stances),
- appliquer une méthode (modalité, seuils),
- produire un résultat,
- et le rendre **auditable**.

Il est la porte entre :
- **Ethikos/Korum** (débat),
- **EkoH** (poids moral & expertise),
- et **Orgo** (action).

→ [Korum](/fr/anatomie/esprit/konnaxion/ethikos/korum.md)  
→ [EkoH](/fr/anatomie/esprit/konnaxion/kollective/ekoh.md)  
→ [Orgo](/fr/anatomie/corps/orgo.md)

---

## Ce que Smart Vote fait (services)

Smart Vote expose cinq services nommés : gestion des votes, pondération dynamique, vote multi-modal, mesures de consensus, visualisation de résultats. 

- `vote_management`   
- `dynamic_weighted_vote`   
- `multi_modal_voting`   
- `consensus_metrics`   
- `result_visualization`   

> **Sceau de King Klown**  
> Une décision n’est pas un bouton.  
> Une décision est un rite : elle exige forme, seuil et trace.

---

## Les portes (routes UI)

Les routes UI réservent un espace clair au jugement et à ses résultats : 

- **/vote** — Voting Hub (Active Votes / Results / Create New)  
- **/vote/insights** — dashboards et analytics (read-only)

---

## L’ossature (modèles)

Smart Vote repose sur des modèles dédiés : 

- **VoteEvent** : événement de vote, sujet, statut, dates.   
- **VoteOption** : options/choix pour un événement.   
- **VoteBallot** : bulletin d’un utilisateur, modalité, valeur brute.   
- **WeightedVoteBallot** : valeur pondérée + trace du poids appliqué.   
- **ConsensusMetric** : métriques calculées (accord, dispersion, etc.).   
- **VoteResultSnapshot** : snapshot des résultats (JSONB) pour audit/transparence.   

Dans l’analogie humaine :
- VoteEvent = “la question”
- VoteOption = “les issues”
- Ballot = “la volonté exprimée”
- WeightedBallot = “la volonté éclairée par la conscience/expertise”
- Snapshot = “la mémoire du verdict”

---

## Modalités : plusieurs manières d’exprimer la volonté

Smart Vote supporte plusieurs modalités de vote : `plurality`, `approval`, `ranking`, `rating`, `quadratic`, `consensus_poll`. 

Ce pluralisme n’est pas cosmétique :
- certaines décisions veulent un gagnant simple,
- d’autres veulent un compromis,
- d’autres veulent réduire les votes stratégiques.

> **Sceau de King Klown**  
> Un seul marteau transforme tout en clou.  
> Plusieurs modalités transforment le pouvoir en nuance.

---

## Le cœur : pondération dynamique (EkoH)

Smart Vote peut pondérer les bulletins en temps réel à partir des scores EkoH (expertise/réputation, par domaine). 

Cette pondération se matérialise dans **WeightedVoteBallot** :
- un ballot brut reste intact,
- mais un ballot pondéré porte un poids calculé et traceable. 

Dans l’analogie :
- l’opinion existe (raw),
- la conscience/expertise modifie l’influence (weighted),
- sans effacer la voix.

→ [EkoH](/fr/anatomie/esprit/konnaxion/kollective/ekoh.md)

---

## Mesures de consensus : savoir si l’accord est fragile ou profond

Smart Vote ne se contente pas d’un gagnant.

Il calcule des **ConsensusMetric** (accord, dispersion, etc.) pour qualifier la décision. 

Dans l’analogie humaine :
- décider sans mesurer le consensus, c’est marcher sans regarder la fissure,
- le consensus est la solidité du pont.

---

## Résultats & transparence : snapshots JSONB

Les résultats sont snapshottés dans **VoteResultSnapshot** (JSONB) pour permettre :
- audit,
- reproductibilité,
- publication,
- comparaison dans le temps. 

C’est la mémoire du verdict — indispensable pour l’éthique.

---

## Smart Vote dans le cycle vital

1) **SenTient / Ariane** : perception  
2) **Korum / Konsultations** : débat & consultation  
3) **EkoH** : poids & conscience (avec decay)  
4) **Smart Vote** : verdict  
5) **Orgo** : exécution  
6) **SwarmCraft** : récit et continuité  
7) **Âme** : verticalité (alignement)

→ [Le cycle vital](/fr/rituels/cycle-vital.md)

---

## Mini-rituel : “Trancher sans trahir”

Quand le débat a assez chauffé :

1) **Ouvre un VoteEvent** (question claire, timebox).   
2) **Déclare les options** (issues réelles).   
3) **Choisis la modalité** (pas toujours plurality).   
4) **Active la pondération** si l’expertise doit éclairer.   
5) **Lis le consensus** (métriques) avant de célébrer.   
6) **Snapshot** et publie (transparence).   
7) **Envoie à Orgo** (action), puis laisse SwarmCraft inscrire.   

> **Sceau de King Klown**  
> Une décision sans exécution est un vœu.  
> Une exécution sans mémoire est une répétition.  
> Smart Vote exige la suite.

---

## Continuer

- ← [Kollective Intelligence](/fr/anatomie/esprit/konnaxion/kollective.md)  
- ← [EkoH](/fr/anatomie/esprit/konnaxion/kollective/ekoh.md)  
- → [Orgo](/fr/anatomie/corps/orgo.md)  
- → [SwarmCraft](/fr/anatomie/memoire/swarmcraft.md)

---

## Vers la partie technique (Réjean)

Pour l’architecture détaillée (services, modèles, modalités, runtime) :  
↗︎ `/Konnaxion/Kollective-Intelligence/Smart-Vote.md` 
