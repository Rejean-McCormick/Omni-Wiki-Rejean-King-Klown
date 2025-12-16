---
title: CertifiKation
description: Les Rites de compétence de Kréature — chemins, évaluations, validation par les pairs, portfolios, certificats. Le passage du savoir au savoir-faire.
---

[English version](../../../../../KK-en/anatomy/mind/konnaxion/konnected/certifikation.md)

# CertifiKation — les Rites de compétence

Dans l’humain, il y a un gouffre entre **comprendre** et **savoir faire**.

On peut lire mille pages sur la nage,  
mais tant qu’on n’a pas traversé l’eau, le corps ne croit pas.

**CertifiKation** est cet organe :  
le moment où le savoir cesse d’être une opinion, et devient une **preuve**.

> **Sceau de King Klown**  
> La connaissance est une lumière.  
> La compétence est une flamme qui brûle même dans le vent.

---

## Ce que CertifiKation représente (dans l’analogie humaine)

CertifiKation correspond à la mécanique très humaine de :

- **l’initiation** (un chemin balisé),
- **l’épreuve** (un passage),
- **le témoin** (le pair / mentor qui atteste),
- **la cicatrice utile** (le portfolio : ce que tu as réellement fait),
- **le sceau** (le certificat : trace officielle).

C’est la “myéline” de Kréature :  
ce qui transforme l’hésitation en automatisme fiable.

---

## La promesse : une chaîne complète, du chemin au sceau

CertifiKation est explicitement conçu comme un parcours bout-à-bout : définir des programmes (*CertificationPath*), évaluer (*Evaluation*), arbitrer une preuve (*PeerValidation*), émettre un titre (*Certificate*), et exposer les preuves via un portfolio et les flows `/certs`. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

---

## Les 5 fonctions (services) — les cinq “portes” du rite

CertifiKation implémente cinq services canonisés (code-names stables) et les expose via le backend et les flows UI `/certs`. :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3}

1) **Certification Paths** — `certification_path_management` : définir et maintenir des chemins modulaires et des jalons de compétence. :contentReference[oaicite:4]{index=4}  
2) **Automated Evaluation** — `automated_evaluation` : quiz/tests auto-notés + calcul de score + métadonnées. :contentReference[oaicite:5]{index=5}  
3) **Peer Validation** — `peer_validation` : approbation/rejet par pair/mentor sur preuves liées à une évaluation. :contentReference[oaicite:6]{index=6}  
4) **Skills Portfolio** — `skills_portfolio` : portfolio d’artefacts et de compétences validées, surfacé dans “My Certificates”. :contentReference[oaicite:7]{index=7}  
5) **Interoperability (LMS)** — `certification_interoperability` : mapping / import / export avec LMS/registries externes. :contentReference[oaicite:8]{index=8}  

> **Sceau de King Klown**  
> Un chemin sans épreuve est une promenade.  
> Une épreuve sans témoin est un rêve.  
> Un témoin sans trace est un mensonge involontaire.

---

## Les modèles — l’ossature du passage

Les tables/modèles utilisés par CertifiKation sont décrits explicitement : :contentReference[oaicite:9]{index=9} :contentReference[oaicite:10]{index=10}

- **CertificationPath** : nom, description (le programme). :contentReference[oaicite:11]{index=11}  
- **Evaluation** : tentative utilisateur, `raw_score`, `metadata` JSON (réponses, rubriques). :contentReference[oaicite:12]{index=12} :contentReference[oaicite:13]{index=13}  
- **PeerValidation** : décision `approved/rejected` par un pair sur une évaluation. :contentReference[oaicite:14]{index=14} :contentReference[oaicite:15]{index=15}  
- **Portfolio (KonnectED)** : preuves et artefacts (M2M), utilisés pour rendre la compétence visible. :contentReference[oaicite:16]{index=16}  
- **InteropMapping** : lien entre un path interne et des IDs de systèmes externes. :contentReference[oaicite:17]{index=17}  
- **Certificate (Core)** : le sceau officiel (modèle commun consommé ici). :contentReference[oaicite:18]{index=18}  

---

## Les deux lois “gravées” (frozen parameters)

CertifiKation impose des seuils stables : la compétence n’est pas “à l’humeur du jour”.

- **Seuil de réussite** : `CERT_PASS_PERCENT = 80%`. :contentReference[oaicite:19]{index=19}  
- **Cooldown de reprise** : `QUIZ_RETRY_COOLDOWN_MIN = 30` minutes entre tentatives échouées. :contentReference[oaicite:20]{index=20}  

Cette rigidité n’est pas une dureté — c’est un **rite** :
on ne triche pas avec la porte, sinon la porte n’existe plus.

---

## Lieu sacré : le Centre `/certs`

Les routes UI sont explicitement réservées : `/certs` est le **Centre CertifiKation** (Programs, My Certificates). :contentReference[oaicite:21]{index=21}

Dans l’analogie :
- **Programs** = les temples (chemins)
- **My Certificates** = les reliques (sceaux acquis)

---

## Comment CertifiKation s’assemble avec le reste de Kréature

### Avec Knowledge : apprendre avant d’être attesté
Knowledge nourrit, CertifiKation scelle.

- → [Knowledge](knowledge.md)  
- ← [KonnectED](../konnected.md)

### Avec Ethikos : quand la compétence devient responsabilité
Plus une compétence est forte, plus son usage doit être orienté.

- → [Ethikos](../ethikos.md)

### Avec EkoH & Smart Vote : réputation, expertise, légitimité
La certification est une preuve.  
La réputation est une trajectoire.  
Le vote pondéré est une action collective.

- → [EkoH](../kollective/ekoh.md)  
- → [Smart Vote](../kollective/smart-vote.md)

---

## Mini-rituel : “Passer la porte”

Quand tu veux transformer un apprentissage en compétence :

1) **Choisis un path** (un seul).  
2) **Expose une preuve** (artefact / résultat).  
3) **Accepte l’épreuve** (score, rubriques).  
4) **Accepte le regard** (pair/mentor si requis). :contentReference[oaicite:22]{index=22}  
5) **Laisse le temps travailler** (cooldown = discipline, pas punition). :contentReference[oaicite:23]{index=23}  

> **Sceau de King Klown**  
> On ne devient pas capable en jurant qu’on l’est.  
> On devient capable en traversant.

---

## Vers la partie technique (Réjean)

Si tu veux les détails d’implémentation (services, modules Django, schéma, paramètres), la section technique correspondante est :  
↗︎ `/Konnaxion/KonnectED/CertifiKation.md` :contentReference[oaicite:24]{index=24}
