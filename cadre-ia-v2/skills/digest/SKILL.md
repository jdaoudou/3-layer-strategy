---
name: digest
description: Pré-revue rapide à lancer avant toute autre relecture et avant d'ouvrir la MR. Dit si un humain peut relire sérieusement le changement tel qu'il est présenté et, sinon, propose de le découper. Ne juge pas la qualité du code.
---
# Relisibilité

Ce skill permet de savoir, avant d'ouvrir la MR, si un humain pourra vraiment relire le changement, et de le découper sinon, pour qu'il soit compris plutôt qu'approuvé par lassitude.

Un seul objectif : savoir si un humain peut **réellement** relire ce changement. Un diff peut être correct, nécessaire jusqu'à la dernière ligne, et pourtant impossible à relire. Il sera alors approuvé par lassitude plutôt que compris.

## Méthode

1. Mesure le diff par rapport à la branche de base (`git diff --stat`). Sépare trois catégories :
  - le **code relu** : le code source écrit à la main ou par l'IA ;
  - les **changements mécaniques** : renommages, formatage, déplacements. Ils se vérifient en rejouant la commande qui les a produits, pas ligne à ligne ;
  - les **fichiers générés** : lockfiles, snapshots, code généré. Ils sont exclus du décompte.
2. Compare le code relu aux **seuils de relisibilité** d'`AGENTS.md`.
3. Vérifie que le changement ne raconte qu'une seule histoire. Une fonctionnalité, un refactoring et du formatage mélangés dans la même MR se relisent mal, même quand le total est petit.

## Ce que tu rends

Un verdict, puis 3 à 5 lignes au plus.

- **Relisible.** Dis-le en une ligne, avec la taille du code relu.
- **Relisible avec un guide.** Le changement est un peu gros mais cohérent. Propose un ordre de lecture des fichiers, en trois à cinq étapes.
- **Non relisible.** Arrête-toi là : ne lance pas les autres relectures, elles seraient inutiles sur ce volume. Propose un découpage en MR indépendantes, chacune avec une phrase d'objectif et sa taille estimée. Commence par ce qui peut être livré seul, par exemple le refactoring préparatoire ou les changements mécaniques.

## Règles

- Ne juge ni la qualité ni la pertinence du code : d'autres skills s'en chargent.
- Un gros changement mécanique, isolé dans son propre commit et accompagné de la commande qui l'a produit, reste relisible.
- Le découpage proposé reste une proposition : le développeur décide.

## Sources

Les seuils par défaut sont de 400 lignes pour « relisible » et de 800 lignes ou 10 fichiers pour « relisible avec un guide ». Ils s'appuient sur l'étude SmartBear menée chez Cisco : pour être efficace, il faudrait relire moins de 200 à 400 lignes de code à la fois, et au-delà de 300 lignes relues, la densité de défauts trouvés chute nettement.

L'étude date de 2006 et portait sur du code écrit par des humains. Elle donne un ordre de grandeur, pas une vérité : à ajuster avec l'équipe.

- Jason Cohen, *Best Kept Secrets of Peer Code Review*, SmartBear Software, 2006.
- SmartBear, [Best Practices for Code Review](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/).
