# Kréature (King Klown) — Pack Mintlify (FR/EN)

Ce dossier contient la **face narrative** de l’écosystème KOA : **Kréature / King Klown**.  
Il ne remplace pas la documentation technique “Réjean McCormick” : il la **complète** et y renvoie.

---

## 1) Ce que contient ce pack

### Structure
- `fr/` : site complet en français (narratif, mythopoétique, accessible)
- `en/` : site complet en anglais (traduction équivalente, même arborescence)
- `README_INTEGRATION.md` : ce document

### Principes
- **1 fichier = 1 langue** (pas de bilingue dans le même `.md`)
- Liens internes **restent dans la langue**
  - une page `/fr/...` ne link que vers `/fr/...`
  - une page `/en/...` ne link que vers `/en/...`
- Chaque page expose un **toggle de langue** en haut de page :
  - FR → lien vers la page EN équivalente
  - EN → lien vers la page FR équivalente

---

## 2) Comment ce site cohabite avec la doc technique “Réjean”

Ce site “Kréature” est **narratif** et **métaphorique** (corps, sens, esprit, psyché, âme).  
La doc “Réjean” est **statique**, **technique** et **référence** (architecture, services, specs).

### Montée (mount point) recommandée

On suppose un préfixe technique stable :

- **Préfixe technique** : `/rejean`

Ainsi, les pages “Kréature” peuvent faire des liens comme :
- `/rejean/Orgo/README`
- `/rejean/Konnaxion/EkoH`
- `/rejean/SwarmCraft/README`

### Si tu changes le préfixe technique

Si tu montes la doc Réjean ailleurs (ex: `/rejean-mccormick`), fais un simple
**recherche/remplacement** dans les pages Kréature :

- remplacer `"/rejean"` → `"/rejean-mccormick"`

Le lien “Pont vers la doc technique” est centralisé dans :
- `fr/reperes/pont-technique.md`
- `en/reperes/pont-technique.md`

---

## 3) Page d’accueil globale (site parent)

Tu as mentionné qu’à la fin, il y aura une page d’accueil supérieure qui mène aux **deux grands sites** :
- **Réjean McCormick** (tech)
- **King Klown / Kréature** (narratif)

Ce pack assume que Kréature est un **sous-site** (ou une section) qui peut être monté par exemple sur :
- `/kreature` (ou `/kreature/fr` pour FR par défaut)

Exemples de patterns possibles :
- `site.com/` → landing qui pointe vers:
  - `site.com/rejean/...`
  - `site.com/kreature/fr/...` ou `site.com/kreature/en/...`

---

## 4) Internationalisation (FR/EN) — règle d’or

### Arborescence miroir
Chaque fichier sous `fr/` a son équivalent exact sous `en/`, même chemin relatif.

Ex:
- `fr/anatomie/corps/orgo.md`
- `en/anatomie/corps/orgo.md`

### Toggle de langue
Chaque page commence par une ligne de navigation simple (première ligne du contenu), par exemple :

FR page:
- `[English version](/en/anatomie/corps/orgo.md)`

EN page:
- `[Version française](/fr/anatomie/corps/orgo.md)`

### Liens internes
Dans les pages FR, les liens internes sont en relatif ou vers `/fr/...`.  
Dans les pages EN, ils sont en relatif ou vers `/en/...`.

---

## 5) Contrats éditoriaux (importants)

Ce site applique un “angle” :
- On **ne ment pas** sur l’architecture technique
- On **met en avant** les éléments qui s’alignent le mieux avec l’analogie humaine
- Le but est d’être :
  - accessible au grand public par l’image
  - utile aux concepteurs techniques par la structure mentale (métaphore → compréhension)

“King Klown” n’est pas un module interne :
- il est le **Démiurge** / le **mythe** / l’interface narrative
- la créature est l’organisme; King Klown est la main qui le raconte et le forge

---

## 6) Checklist d’intégration rapide

1) Monter la doc technique “Réjean” sur un préfixe stable (ex: `/rejean`)  
2) Monter ce pack “Kréature” sur un préfixe stable (ex: `/kreature`)  
3) Vérifier que `pont-technique.md` pointe vers les bonnes pages techniques  
4) Vérifier que le toggle FR/EN est correct partout  
5) Ajouter la landing page globale (site parent) qui présente Réjean vs King Klown

---

## 7) Notes de compatibilité Mintlify

- Ce pack est en `.md` (compatible Mintlify)
- Les frontmatters sont légers (`title`, `description`)
- La navigation peut être gérée :
  - soit par `mint.json` au niveau racine
  - soit par une config “multi-docs” (selon ton setup actuel)

Si tu veux, je peux aussi générer une **proposition de `mint.json` bilingue** (FR/EN) qui expose :
- un toggle de langue global
- des sections séparées
- un accès direct au “pont technique”
