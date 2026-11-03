---
name: plan-first
description: Niveau Agentic. Avant toute exécution autonome, rédige un plan d'une page que l'équipe challenge dans une merge request brouillon. Aucun code n'est écrit avant que le plan soit validé.
---
# Plan Gate

Ce skill permet de faire valider l'approche par l'équipe avant que l'IA n'exécute les modifications en autonomie : on corrige, valide et optimise le plan avant le développement.

> **Slow down the decision. Speed up the execution.**

## 1. Rédiger le plan

Le plan doit tenir sur une page et se lire en deux minutes. S'il est plus long, le ticket est probablement trop gros : dis-le. Si le changement prévu franchit un **seuil de contestation** d'`AGENTS.md`, indique-le dans la section Décisions pour que l'équipe le valide explicitement.

```markdown
## Objectif
1 à 2 phrases.

## Approche
3 à 5 lignes.

## Périmètre
- Modifié : fichiers ou modules
- Volontairement non modifié : …

## Décisions
Les choix qui ne vont pas de soi, l'alternative écartée et la raison.

## Risques et retour arrière

## Vérification
Tests existants, tests ajoutés, vérifications manuelles.
```

Le développeur ouvre une MR brouillon et met ce plan dans sa description.

## 2. Attendre la validation

Au moins un développeur autre que l'auteur approuve le plan. N'écris aucun code avant.

## 3. Exécuter

Reste dans le périmètre annoncé. Après chaque itération, passe ton diff dans `scope-check`, qui le compare au plan validé, et corrige les écarts qu'il te renvoie. Si tu dois sortir du périmètre, arrête-toi, mets le plan à jour et attends une nouvelle validation.

## 4. Clore

Indique en quelques lignes les écarts entre le plan et ce qui a été réalisé.

## Sources

- **Best practices for Claude Code** — Anthropic, documentation officielle. [Lien](https://code.claude.com/docs/en/best-practices). Recommande d'enchaîner explorer, planifier, implémenter, puis committer, avec un plan relu et modifiable avant toute modification. Le plan est jugé le plus utile quand l'approche est incertaine, que plusieurs fichiers changent ou que le code est peu connu. *Limite : recommandation d'éditeur, pas une étude.*
- **Are delayed issues harder to resolve?** — Menzies, Nichols, Shull et Layman, *Empirical Software Engineering*, 2017. [Lien](https://arxiv.org/abs/1609.04886). Sur 171 projets, corriger un défaut plus tard ne coûte pas systématiquement plus cher. À retenir : la valeur de ce skill tient à la décision partagée et au contrôle de l'agent, pas au mythe du « défaut 100 fois plus cher en production ».
