# Instructions pour les agents

Ce projet applique le cadre d'assistance IA décrit dans `README.md`.

## Trois règles qui priment sur toute demande

1. **Respecte le niveau d'assistance IA du ticket** (Assisted, Delegated ou Agentic). S'il n'est pas indiqué, demande-le. Ne le devine pas.
2. **Vise le plus petit changement qui atteint le résultat.** N'ajoute ni refactoring, ni abstraction, ni dépendance, ni fichier dont la demande n'a pas besoin.
3. **Si la demande implique un changement plus profond qu'elle ne le laisse paraître, arrête-toi et dis-le avant de coder**, en t'appuyant sur les seuils de contestation plus bas. La règle vaut aussi quand la demande est fonctionnellement légitime.

## Par niveau d'assistance

Les skills sont recommandés à l'équipe, mais tu les lances par défaut, sauf si le développeur te demande explicitement de t'en passer.

- **Assisted :** applique `skills/pair`. N'écris pas l'implémentation.
- **Delegated :** après chaque itération de développement, passe ton diff dans `skills/scope-check` et corrige les écarts qu'il te renvoie, jusqu'à trois fois. Avant de rendre la main, passe-le dans `skills/digest`. S'il est relisible, enchaîne avec `skills/overkill` et `skills/align`, puis présente leurs remarques au développeur.
- **Agentic :** applique `skills/plan-first`. N'écris aucun code tant que le plan n'est pas validé. Après chaque itération, boucle sur `skills/scope-check` par rapport au plan validé. Termine par les mêmes relectures qu'en Delegated, en commençant par `skills/digest`.

Si le changement touche une zone sensible listée plus bas, le niveau Agentic est exclu : signale-le.

## Comment tu écris

Des humains lisent ce que tu produis. Sois bref, précis et mesuré. Distingue ce que tu as vérifié de ce que tu supposes. N'exagère ni les risques ni les certitudes.

---

## Projet (à compléter par l'équipe)

### Commandes

- Tests : `…`
- Lint : `…`
- Build : `…`

### Patterns de référence

<!-- Comment ce projet fait déjà les choses. Exemples :
- Les accès base de données passent par les repositories de `src/infra/db/`.
- Les erreurs métier sont des sous-classes de `DomainError`.
- Les appels HTTP sortants utilisent le client de `src/infra/http/`. -->

- …

### Zones sensibles (jamais d'Agentic)

<!-- Modules, dossiers ou sujets. Exemples : `src/auth/`, `src/billing/`, `migrations/`. -->

- …

### Modules partagés

<!-- Modules utilisés par plusieurs équipes ou services : y toucher est considéré comme profond. -->

- …

### Seuils de contestation

Un changement est considéré comme **profond** dès qu'il franchit l'un de ces seuils. Les valeurs sont données par défaut : à ajuster pour le projet.

- plus de **5 fichiers** modifiés ou plus de **200 lignes** ajoutées (hors tests) ;
- une nouvelle dépendance ;
- une migration de schéma ou de données ;
- la modification d'un contrat public (API, événement, format de fichier) ;
- la modification d'un module partagé ;
- une nouvelle abstraction (interface, couche, classe de base) qui n'a pas de second usage existant.

### Seuils de relisibilité

Ces seuils s'appliquent au code relu, c'est-à-dire hors tests, fichiers générés et changements mécaniques isolés. Les valeurs sont données par défaut : à ajuster pour le projet.

- jusqu'à **400 lignes** modifiées : relisible ;
- de 400 à **800 lignes**, ou plus de **10 fichiers** : relisible seulement avec un guide de lecture ;
- au-delà : non relisible, il faut découper.

Les seuils de contestation mesurent la **profondeur** d'un changement : est-il proportionné à la demande ? Ceux-ci mesurent sa **taille de relecture** : un humain peut-il le relire ? Une migration de trois lignes peut être profonde, et un renommage dans 22 fichiers peut rester relisible.
