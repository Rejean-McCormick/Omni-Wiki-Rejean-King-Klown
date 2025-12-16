---
title: Konsultations
description: Consultations publiques et feedback — fenêtres de participation, suggestions, vote pondéré, visualisation des résultats, suivi d’impact.
---

[English version](../../../../../KK-en/anatomy/mind/konnaxion/ethikos/konsultations.md)

# Konsultations — la Chambre des voix

Il y a des décisions qu’on ne peut pas prendre “entre initiés”.

Parce qu’elles touchent tout le monde.  
Parce qu’elles engagent une communauté.  
Parce qu’elles transforment le sol sous les pieds.

**Konsultations** est l’organe de la participation :  
un rite public, time-boxed, où la parole devient donnée, et la donnée devient trajectoire — puis où la trajectoire doit rendre des comptes.

> **Sceau de King Klown**  
> Une consultation n’est pas un micro tendu.  
> C’est une dette : si tu demandes la voix, tu dois montrer l’impact.

---

## Le parallèle humain (fortement corrélé)

Dans l’humain :
- le corps est fermé,
- le langage est le pont,
- le débat éthique est l’espace du tiraillement.

Konsultations est la version “cité” de ce tiraillement :
- on ouvre une fenêtre,
- on recueille des voix,
- on structure le chaos,
- on agrège,
- on décide,
- puis on suit les conséquences.

Ce n’est pas le *débat* (Korum).  
C’est l’*appel*.

→ [Korum](korum.md)  
→ [Ethikos](../ethikos.md)

---

## Ce que Konsultations fait (services)

Konsultations définit cinq services explicites : consultation publique, suggestions citoyennes, vote pondéré, visualisation des résultats, suivi d’impact. 

- `public_consultation`   
- `citizen_suggestion`   
- `weighted_consultation_vote`   
- `consultation_result_visualization`   
- `impact_tracking`   

---

## Les portes (routes UI)

Konsultations vit derrière des portes claires : 

- **/consult** — Consultation Hub  
  - Live Consultations  
  - Results Archive  
  - Submit Suggestion   

- **/ethikos/insights** — visualisation et analytics (read-only)   

Un invariant important : **/consult appartient exclusivement à ethiKos**. 

---

## L’ossature (modèles)

Konsultations s’appuie sur des modèles qui permettent de rendre la participation traçable :

- **ConsultationEvent** : événement time-boxed, “ouvert/fermé”, titre, description.   
- **ConsultationSuggestion** : proposition d’un participant, statut (pending/accepted/rejected).   
- **ConsultationVote** : bulletin (value brute + value pondérée), modalité, timestamp.   
- **ConsultationResultSnapshot** : snapshot JSONB des résultats (transparence).   
- **ImpactRecord** : suivi d’impact (action, statut, date, commentaire).   

> **Sceau de King Klown**  
> Un peuple sans archive devient un bruit.  
> Une archive sans impact devient un musée.  
> Konsultations exige les deux : mémoire et conséquence.

---

## Les modalités de vote (comment la cité choisit)

Konsultations supporte plusieurs modalités de bulletin :  
`approval`, `ranking`, `rating`, `preferential`. 

Dans l’analogie :
- **approval** : “je suis pour / pas pour”
- **ranking** : “voici mon ordre de préférence”
- **rating** : “je note la force de mon choix”
- **preferential** : “je choisis, mais je garde des transferts”

Ce pluralisme empêche une démocratie de n’avoir qu’un seul outil (souvent toxique).

---

## Le vote pondéré (conscience & expertise)

Konsultations distingue :
- **raw_value** (valeur brute)  
- **weighted_value** (valeur pondérée)

La pondération peut utiliser le même principe que la conscience/réputation (EkoH), et s’intégrer dans les agrégations via Smart Vote.  

Dans l’analogie humaine :
- tout le monde peut parler (valeur brute),
- mais l’expertise peut éclairer (valeur pondérée),
- sans fermer la porte au vivant.

→ [EkoH](../kollective/ekoh.md)  
→ [Smart Vote](../kollective/smart-vote.md)

---

## Le seuil “fort” de consensus

Konsultations mentionne un seuil “fort” de consensus pondéré, exemple : **≥ 75%**. 

Ce genre de seuil sert à distinguer :
- une majorité fragile,
- d’un alignement solide.

> **Sceau de King Klown**  
> Une majorité n’est pas toujours une légitimité.  
> Parfois c’est juste une vague.  
> Konsultations cherche les marées profondes.

---

## Résultats & transparence : snapshots

Les résultats ne sont pas seulement “affichés”.  
Ils sont **snapshottés** (JSONB) pour garder une trace consultable. 

Dans une cité vivante, la transparence est un organe :
- elle réduit la paranoïa,
- elle force la responsabilité,
- elle permet les audits.

---

## L’élément rare : le suivi d’impact

C’est là que Konsultations devient un vrai organe moral :  
il ne suffit pas de voter. Il faut **voir ce que ça a produit**.

ImpactRecord garde :
- l’action engagée,
- un statut,
- une date,
- un commentaire.

Dans l’analogie humaine :
- la décision est un acte,
- l’impact est la conséquence,
- la conscience se nourrit des conséquences.

Sans impact tracking, la consultation est un théâtre.

---

## Mini-rituel : “Ouvrir une consultation propre”

1) **Définir l’événement** (ConsultationEvent) : titre, fenêtre, but.   
2) **Ouvrir le canal de suggestions** : accepter le bruit, puis structurer.   
3) **Choisir la modalité de vote** (approval/ranking/rating/preferential).   
4) **Activer pondération si pertinent** (EkoH/Smart Vote) : éclairer sans fermer.   
5) **Publier un snapshot** des résultats.   
6) **Créer des ImpactRecords** : montrer ce qui a changé.   

> **Sceau de King Klown**  
> La participation est une prière.  
> L’impact est la réponse.

---

## Continuer

- ← [Ethikos](../ethikos.md)  
- ← [Korum](korum.md)  
- → [EkoH](../kollective/ekoh.md)  
- → [Smart Vote](../kollective/smart-vote.md)
