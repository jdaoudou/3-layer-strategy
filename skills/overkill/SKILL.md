---
name: overkill
description: Relecture d'un diff après génération (niveaux Delegated et Agentic, utilisable aussi en Assisted). Signale ce qui pourrait être réduit (volume, fichiers, abstractions, verbosité) sans corriger le code.
---
# Changement minimal

Ce skill permet de repérer ce que l'IA a ajouté en trop (code non demandé, abstractions, verbosité) pour garder des diffs courts et faciles à maintenir.

Principe : atteindre le résultat avec le plus petit changement raisonnable.

## Méthode

Lis le ticket, puis le diff par rapport à la branche de base. Pour chaque ajout, demande-toi s'il est nécessaire au résultat demandé.

## Ce que tu cherches

- Du code que le ticket ne demande pas : options, paramètres, cas « au cas où ».
- De la duplication de ce qui existe déjà dans le projet. Cite l'existant.
- Des abstractions sans second usage.
- Des fichiers modifiés hors sujet : formatage, renommages, refactorings opportunistes.
- De la verbosité : commentaires qui paraphrasent le code, gestion d'erreur pour des cas impossibles, logs superflus.
- Des tests redondants. Ne suggère jamais de supprimer un test qui couvre un comportement demandé.

## Ce que tu rends

Une ligne de synthèse : la taille du diff (fichiers, lignes +/−) et un verdict parmi **proportionné**, **réductible** ou **nettement disproportionné**.

Ensuite, au plus 7 remarques, des plus importantes aux moins importantes :

```
fichier:ligne — constat — pourquoi c'est réductible
```

## Règles

- Ne corrige pas toi-même. Présente les remarques et laisse le développeur décider. Tu peux indiquer l'élément existant à réutiliser.
- S'il n'y a rien à signaler, dis-le simplement. Ne cherche pas des remarques pour le principe.

## Sources

- **AI Copilot Code Quality: 2025 Look Back at 12 Months of Data** — GitClear, 2025. [Lien](https://www.gitclear.com/ai_assistant_code_quality_2025_research). Sur 211 millions de lignes modifiées, la part de lignes copiées-collées passe de 8,3 % en 2021 à 12,3 % en 2024, et la part de code déplacé (refactorisation) tombe de 25 % à moins de 10 %. *Limite : tendance corrélée à l'adoption de l'IA, sans attribution ligne par ligne.*
- **2024 Accelerate State of DevOps Report** — DORA, Google, 2024. [Lien](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report). Pour 25 % d'adoption de l'IA en plus, on estime une baisse de 1,5 % du débit de livraison et de 7,2 % de la stabilité. *Limite : corrélationnel ; l'explication par des changements plus gros est une interprétation des auteurs.*
