---
title: EkoH
description: La Conscience de Kréature — réputation, expertise, éthique, mémoire et oubli (decay). Le poids invisible qui modifie chaque décision.
---

[English version](../../../../../KK-en/anatomy/mind/konnaxion/kollective/ekoh.md)

# EkoH — la Conscience (réputation & expertise)

Dans l’humain, la conscience n’est pas un sermon.  
C’est une **gravité**.

Elle ne t’empêche pas d’agir.  
Elle fait que certains gestes **pèsent** plus que d’autres —  
et que certains gestes laissent une trace, même quand tu voudrais les effacer.

**EkoH** est cette gravité dans Kréature :  
un moteur de réputation et d’expertise **par domaine**, modulé par une éthique, visible sans trahir l’identité, et traçable sans devenir inquisitorial.

> **Sceau de King Klown**  
> La conscience n’est pas une cage : c’est un poids.  
> Elle n’éteint pas la liberté. Elle donne un prix à la facilité.

---

## Ce que fait EkoH (services)

EkoH expose **sept services stables** (code-names), chacun mappable à des modules de service dédiés.  

- **Multidimensional Scoring** — `multidimensional_scoring` : calcule des scores selon plusieurs axes (qualité, fréquence, pertinence, expertise).   
- **Criteria Customization** — `configuration_weights` : ajuste les poids/coefficients (globalement ou par domaine).   
- **Automatic Contextual Analysis** — `contextual_analysis` : ajuste des sous-scores selon contexte, historique, complexité (signal IA).   
- **Dynamic Privacy** — `privacy_settings` : permet pseudonyme/anonymat tout en gardant la “valeur” du mérite.   
- **History & Traceability** — `score_history` : conserve l’historique des changements pour audit.   
- **Interactive Visualizations** — `score_visualization` : alimente dashboards, cartes, matrices.   
- **Expertise Classification** — `expertise_field_classification` : rattache les scores à une taxonomie de domaines.   

---

## Le parallèle humain (fortement corrélé)

Dans ton modèle :

- la **culpabilité** est une mémoire du bien/mal,
- elle a un **decay rate** (elle s’estompe),
- la conscience influence le jugement sans être le jugement.

EkoH est exactement cette mécanique :
- il **marque** (réputation/expertise/éthique),
- il **pondère** (influence),
- il **s’estompe** (par cycles de recalcul),
- il **laisse une trace** (audit),
- et il peut rester **humble** (privacy).

EkoH n’est pas le tribunal.  
EkoH est le *poids* qui rend le tribunal moins aveugle.

→ [Kollective Intelligence](../kollective.md)  
→ [Smart Vote](smart-vote.md)

---

## La loi centrale : l’ethical multiplier

EkoH inclut une couche d’éthique qui **multiplie** l’expertise pour produire un poids final d’influence (hausse si comportement constructif, baisse si comportements signalés).  

C’est l’équivalent numérique d’un mécanisme humain simple :
- tu peux être très compétent,
- mais si tu détruis la confiance, ton influence se contracte.

Les bornes de ce multiplicateur sont **gelées** : plancher **0.20**, plafond **1.50**. 

> **Sceau de King Klown**  
> La compétence sans éthique est un couteau.  
> L’éthique sans compétence est une prière sans mains.  
> EkoH les oblige à se regarder.

---

## Les modèles (l’ossature de la conscience)

EkoH persiste expertise, éthique, audit et confidentialité via des tables dédiées. 

- **ExpertiseCategory** : taxonomie des domaines.   
- **UserExpertiseScore** : score par utilisateur et par domaine (raw + weighted).   
- **UserEthicsScore** : score d’éthique (le multiplicateur).   
- **ScoreConfiguration** : poids/coefficients (global ou par domaine).   
- **ContextAnalysisLog** : journaux d’ajustements contextuels (métadonnées + ajustements JSON).   
- **ConfidentialitySetting** : mode d’affichage d’identité (public/pseudonym/anonymous).   
- **ScoreHistory** : trace complète des variations (audit trail).   

Ce set de modèles est important pour l’analogie :
- la conscience n’est pas juste “une note”,
- c’est une mémoire structurée + des règles de visibilité + une trace temporelle.

---

## Les paramètres gelés (les “constantes morales”)

EkoH démarre avec des poids d’axes initiaux, explicitement listés :  
**quality=1.000**, **expertise=1.500**, **frequency=0.750**. 

Et une taxonomie de domaines : **EXPERTISE_DOMAIN_CHOICES** (26 domaines ISO-based). 

Dans la mise en scène Kréature :  
ce sont les “lois de la gravité” — discutables dans Ethikos, mais stables pour que l’organisme reste cohérent.

---

## Le “decay rate” (oubli contrôlé, pas amnésie)

Ton intuition humaine : **la culpabilité s’estompe**.

EkoH l’incarne par conception : il calcule des scores **à partir de l’activité dans le temps**, via déclencheurs d’événements et recomputations périodiques.  

Autrement dit :
- ce qui n’est plus nourri par le présent perd de son poids,
- sans effacer l’historique (ScoreHistory garde les traces). 

> **Sceau de King Klown**  
> Pardonner n’est pas oublier.  
> Pardonner, c’est empêcher le passé de tenir le volant.

---

## Privacy : être compté sans être exposé

EkoH prévoit explicitement des modes de confidentialité (public/pseudonym/anonymous) pour afficher des signaux de mérite sans livrer l’identité. 

Dans l’analogie :
- la conscience doit éclairer,
- mais elle ne doit pas devenir une humiliation publique permanente.

---

## EkoH n’est pas seul : intégration avec Smart Vote

EkoH sert de **backbone de pondération** : Smart Vote lit les scores (par domaine) pour re-pondérer des votes en temps réel (`dynamic_weighted_vote`).  

Korum et Konsultations consomment aussi cette pondération pour produire des vues pondérées/cohortées. 

→ [Korum](../ethikos/korum.md)  
→ [Konsultations](../ethikos/konsultations.md)  
→ [Smart Vote](smart-vote.md)

---

## Runtime : souffle nocturne, nerfs en temps réel

- **Recalcul périodique** via tâches planifiées (Celery Beat) pour rafraîchir scores et pré-calculs.   
- **Livraison temps réel** optionnelle via Channels + Redis (deltas de scores, leaderboards, résultats pondérés).   

Dans la mythologie Kréature :
- la nuit, la conscience “rêve” et recalcule,
- le jour, elle “réagit” et ajuste la gravité.

---

## Mini-rituel : “Devenir digne de poids”

1) **Agir** dans un domaine (produire, contribuer).   
2) **Laisser la trace** (score_history, audit).   
3) **Accepter l’éthique** (multiplicateur).   
4) **Protéger l’identité si nécessaire** (privacy settings).   
5) **Ne pas craindre l’oubli** : ce qui est vivant se prouve à nouveau (recomputation).   

---

## Continuer

- ← [Kollective Intelligence](../kollective.md)  
- → [Smart Vote](smart-vote.md)  
- → [Ethikos](../ethikos.md)

---

## Vers la partie technique (Réjean)

Pour l’architecture détaillée (services, modèles, paramètres, runtime) :  
↗︎ `/Konnaxion/Kollective-Intelligence/EkoH.md` 
