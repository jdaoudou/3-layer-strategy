---
name: align
description: Relecture d'un diff après génération. Vérifie qu'il respecte l'architecture, les conventions et les patterns déjà en place dans le projet, et signale les écarts sans corriger le code.
---
# Cohérence avec la codebase

Ce skill permet de vérifier que le code généré suit l'architecture et les conventions du projet, pour éviter qu'une deuxième manière de faire s'installe en silence.

## Méthode

1. Lis les patterns de référence d'`AGENTS.md` et, s'il existe, le dossier de décisions d'architecture.
2. Pour chaque nouvel élément du diff (fichier, classe, fonction, dépendance, manière de faire), cherche dans le projet comment la même chose est déjà faite.

## Ce que tu cherches

- Une deuxième manière de faire quelque chose qui en a déjà une : accès aux données, gestion d'erreur, configuration, logs, appels HTTP, validation.
- Une nouvelle dépendance alors qu'un équivalent est déjà utilisé.
- Un placement incohérent (couche, dossier).
- Un nommage qui s'écarte des conventions.
- Des tests écrits dans un style différent de l'existant.

## Ce que tu rends

Une ligne de synthèse avec un verdict parmi **cohérent**, **écarts mineurs** ou **écart structurant**.

Ensuite, au plus 7 remarques :

```
fichier:ligne — écart — pattern existant (fichier de référence)
```

## Règles

- Ne corrige pas toi-même. Présente les écarts et laisse le développeur décider.
- Un écart n'est pas forcément une erreur. Si l'existant te paraît lui-même discutable, dis-le. Mais une nouvelle manière de faire mérite une décision d'équipe : elle ne doit pas s'installer en silence.
- S'il n'y a rien à signaler, dis-le simplement.

## Sources

- **Speed at the Cost of Quality: How Cursor AI Increases Short-Term Velocity and Long-Term Complexity in Open-Source Projects** — He, Miller, Agarwal, Kästner et Vasilescu, Carnegie Mellon, MSR 2026. [Lien](https://arxiv.org/abs/2511.04427). Sur environ 800 dépôts, l'adoption de Cursor s'accompagne d'une hausse durable des avertissements d'analyse statique (+30 %) et de la complexité du code (+41 %), alors que le gain de vitesse disparaît après deux mois. *Chiffres de la deuxième version de l'article, à revérifier dans la dernière.*
- **State of AI vs Human Code Generation Report** — CodeRabbit, 2025. [Lien](https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report). Sur 470 PR, celles co-écrites avec l'IA comptent 1,7 fois plus de problèmes que les PR humaines (10,83 contre 6,45), dont plus de 3 fois plus de problèmes de lisibilité. *Limite : rapport d'un éditeur d'outil de revue.*
