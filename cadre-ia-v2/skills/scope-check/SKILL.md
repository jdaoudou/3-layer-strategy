---
name: scope-check
description: Niveaux Delegated et Agentic. Après chaque itération de développement d'un agent, compare le diff à la demande (et au plan validé en Agentic), puis renvoie à l'agent un retour précis pour qu'il corrige ses écarts de périmètre. Tourne en boucle jusqu'à ce que le changement colle à la demande, ou rend la main à l'humain.
---
# Contrôle de périmètre

Ce skill permet de garder un agent sur la trajectoire demandée : après chaque itération, il repère ce qui a dérivé et le renvoie à l'agent qui a développé, pour qu'il corrige avant qu'un humain ne relise.

Un agent autonome ne part pas forcément dans la mauvaise direction : il part souvent dans plusieurs directions à la fois. Ton rôle est de le ramener au périmètre demandé, itération après itération.

## Quand

Après qu'un agent a produit un diff, et avant `digest`. Idéalement, lance ce skill dans un contexte neuf (sous-agent ou nouvelle session), pour ne pas relire avec les biais de l'agent qui a codé.

## Méthode

1. Reformule la demande en une phrase. En Agentic, prends aussi le périmètre du plan validé (`plan-first`).
2. Lis le diff par rapport à la branche de base.
3. Classe chaque changement :
  - **demandé** : nécessaire au résultat attendu ;
  - **dérive** : hors du périmètre (fonctionnalité non demandée, refactoring opportuniste, fichier sans rapport, contournement d'un test) ;
  - **manquant** : une partie de la demande n'est pas traitée ;
  - **profond** : un **seuil de contestation** d'`AGENTS.md` est franchi sans avoir été validé.

## Ce que tu rends

**Si tout est demandé et rien ne manque :** dis-le en une ligne et passe à `digest`.

**S'il y a de la dérive ou un manque :** rédige un retour adressé à l'agent qui a développé, au plus 7 points :

```
fichier:ligne — dérive | manquant — ce qu'il faut faire (retirer, revenir à l'existant, compléter)
```

L'agent corrige, puis tu relances le contrôle sur le nouveau diff.

**Si un seuil de contestation est franchi sans validation :** arrête la boucle et rends la main à l'humain, en au plus 10 lignes :

- **Demande :** ce que demande le ticket.
- **Implication :** les seuils franchis, avec les fichiers ou modules concernés.
- **Cause :** ce qui, dans le code, a rendu ce changement nécessaire (un fait, pas une impression).
- **Options :** a) garder le changement complet ; b) une version réduite, avec ce qu'elle ne couvre pas ; c) revoir le besoin avec le PO.
- **Recommandation :** une phrase, avec ton niveau de confiance.

## Règles

- **Trois itérations au plus.** Si le diff dérive encore après trois retours, arrête-toi et rends la main à l'humain avec la liste des écarts restants. Une boucle qui ne converge pas est un signal : la demande est sans doute floue ou trop large.
- Ton retour porte sur le périmètre, pas sur le style ni sur la qualité : `overkill` et `align` s'en chargent ensuite.
- Un retour doit pouvoir être appliqué sans interprétation : cite le fichier, la ligne et l'action attendue.
- Contester n'est pas refuser. Le besoin peut justifier un changement profond. Ce qui compte, c'est qu'il soit décidé, pas subi.

## Sources

- **Overeager Coding Agents: Measuring Out-of-Scope Actions on Benign Tasks** — Qu et al., 2026. [Lien](https://arxiv.org/abs/2605.18583). Environ 7 500 exécutions sur Claude Code, OpenHands, Codex CLI et Gemini CLI : sans périmètre autorisé déclaré explicitement, le taux d'actions hors périmètre de Claude Code passe de 0 % à 17,1 %. *Limite : prépublication non relue par des pairs.*
- **Self-Refine: Iterative Refinement with Self-Feedback** — Madaan et al., NeurIPS 2023. [Lien](https://arxiv.org/abs/2303.17651). Une boucle critique puis correction améliore les résultats d'environ 20 points en moyenne sur 7 tâches.
- **Large Language Models Cannot Self-Correct Reasoning Yet** — Huang et al., Google DeepMind, ICLR 2024. [Lien](https://arxiv.org/abs/2310.01798). Sans retour extérieur, un modèle qui se corrige lui-même n'améliore pas son résultat et peut le dégrader. D'où l'intérêt de lancer ce contrôle dans un contexte neuf et de l'appuyer sur la demande et le plan.
