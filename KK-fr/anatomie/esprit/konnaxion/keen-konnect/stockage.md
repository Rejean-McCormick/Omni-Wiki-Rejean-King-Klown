---
title: Stockage
description: Dépôt sécurisé et versionné — la mémoire solide de Kréature. Rétention, intégrité, restauration, continuité d’équipe.
---

[English version](../../../../../KK-en/anatomy/mind/konnaxion/keen-konnect/stockage.md)

# Stockage — la Mémoire solide

Il existe une mémoire qui rêve.  
Et une mémoire qui **tient**.

La première est souple : elle reconstruit, elle réinterprète.  
La seconde est dure : elle protège l’intégrité du réel.

**Stockage** est cette seconde mémoire.

Dans Kréature, Stockage est le dépôt sûr et versionné :  
l’endroit où l’on garde ce qui ne doit pas se perdre, ce qui ne doit pas être écrasé, ce qui doit pouvoir être restauré.

> **Sceau de King Klown**  
> Les équipes oublient vite.  
> Les fichiers aussi, d’une autre manière.  
> Stockage est le rempart contre l’oubli qui détruit.

---

## Le parallèle humain (fortement corrélé)

Dans l’humain :

- l’esprit pense en mesh,
- la mémoire reconstruit,
- l’identité se maintient malgré les changements.

Mais le corps a aussi un autre type de mémoire :
- **os / tendons / cicatrices** : des structures stables, qui ne se réécrivent pas à chaque souvenir.

Stockage correspond à cette stabilité.

Si **Konstruct** est l’atelier où l’on bâtit,  
Stockage est l’armoire forte où l’on garde :
- plans,
- versions,
- preuves,
- archives,
- pièces maîtresses.

→ [keenKonnect](../keen-konnect.md)  
→ [Konstruct](konstruct.md)

---

## Ce que Stockage est (définition)

Stockage est le second sous-module de **keenKonnect**, décrit comme **Secure Repository & Versioned Storage**. 

Son rôle : fournir un dépôt souverain où le contenu est :
- protégé,
- versionné,
- récupérable,
- et gouverné par des règles de sécurité.

---

## Les 5 fonctions (services) — les cinq “verrous” du dépôt

Stockage expose cinq services nommés : 

1) **Secure Repository Management** — `secure_repository_management` : création/gestion de dépôts, politiques, permissions.   
2) **Version Control & Rollback** — `version_control_and_rollback` : versioning, diff, restauration.   
3) **Access Control & Encryption** — `access_control_and_encryption` : contrôle d’accès, chiffrement, clés.   
4) **Audit Trail & Compliance** — `audit_trail_and_compliance` : logs, traçabilité, conformité.   
5) **Backup & Recovery Automation** — `backup_and_recovery_automation` : sauvegardes, rotation, recovery tests.   

Dans l’analogie humaine :
- repository = squelette de la mémoire
- versioning = cicatrisation contrôlée (on peut revenir)
- encryption = peau + secret interne
- audit = “mémoire des actes” (responsabilité)
- backup = réserve vitale (survie)

---

## L’ossature (modèles) — ce qui rend la mémoire vérifiable

Stockage repose sur des modèles concrets : 

- **Repository** : dépôt, propriétaire, paramètres de sécurité.   
- **StoredAsset** : fichier/artefact stocké (type, hash, métadonnées).   
- **AssetVersion** : versions successives (lien vers asset, numéro, timestamp).   
- **EncryptionKey** : clés/chiffrement, rotation, scope.   
- **RepositoryAccessGrant** : permissions (user/role/scope).   
- **AuditLog** : logs d’accès / modification / restauration.   
- **BackupJob** : jobs de backup, statut, exécutions.   

Deux éléments méritent d’être “mis en avant” pour la mythologie Kréature :
- **hash** : l’intégrité (la preuve que le contenu n’a pas été altéré)
- **rollback** : la capacité de revenir sans mentir

---

## Les portes (routes UI)

Stockage expose des routes simples et auditables : 

- **/repos** — Repository Hub  
- **/repos/{id}** — vue d’un repo (assets, versions)  
- **/repos/{id}/audit** — audit log  
- **/repos/{id}/backup** — backups & restore operations  

---

## Ce que Stockage protège réellement

### 1) Contre l’écrasement (l’erreur banale)
Un fichier remplacé sans retour possible est une amputation.

Stockage propose versioning + rollback : le passé reste accessible. 

### 2) Contre la fuite (la perforation)
Accès et chiffrement protègent l’intérieur. 

### 3) Contre l’invisibilité (l’irresponsabilité)
Audit trail rend les actes visibles. 

### 4) Contre la catastrophe (la perte)
Backups & recovery existent comme automatisme, pas comme promesse vague. 

> **Sceau de King Klown**  
> La sécurité n’est pas un cadenas.  
> C’est une chaîne : intégrité, contrôle, trace, restauration.

---

## Stockage et le reste de Kréature

### Avec Konstruct : chantier + coffre
Konstruct produit des artefacts ; Stockage garantit qu’ils survivent.

→ [Konstruct](konstruct.md)

### Avec Orgo : souveraineté interne
Orgo maintient la bulle hermétique ; Stockage assure la mémoire dans cette bulle.

→ [Orgo](../../../corps/orgo.md)

### Avec KonnectED / CertifiKation : preuves et portfolios
Les preuves de compétence ont besoin d’un dépôt sûr (assets versionnés, audités).

→ [CertifiKation](../konnected/certifikation.md)

---

## Mini-rituel : “Sceller ce qui compte”

Quand un artefact devient “important” :

1) **Stocker** comme asset (hash + metadata).   
2) **Versionner** chaque mutation significative.   
3) **Chiffrer** et limiter les grants.   
4) **Auditer** les accès.   
5) **Backup** et tester un restore.   

> **Sceau de King Klown**  
> Une mémoire qui ne peut pas être restaurée  
> n’est pas une mémoire :  
> c’est un pari.

---

## Continuer

- ← [keenKonnect](../keen-konnect.md)  
- ← [Konstruct](konstruct.md)  
- → [Konnaxion](../README.md)
