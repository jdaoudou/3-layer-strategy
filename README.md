# Framework 3SL

## Le cadre en bref

Ce cadre repose sur deux idées :

1. Au cadrage technique, chaque ticket reçoit un **niveau d'assistance IA**.
2. Ce niveau fixe la place de l'IA et les contrôles à faire.

---

## Les skills

| Skill | Quand | Ce qu'il fait |
| --- | --- | --- |
| `pair` | Assisted, pendant le développement | L'IA reste partenaire de réflexion et de relecture. |
| `plan-first` | Agentic, avant de coder | Rédige un plan d'une page à faire valider avant toute exécution. |
| `scope-check` | Après chaque itération de l'agent | Renvoie à l'agent ses écarts de périmètre jusqu'à ce que le diff colle à la demande. Rend la main à l'humain si un seuil est franchi. |
| `digest` | Après le code, en premier | Dit si un humain peut relire le diff et, sinon, propose un découpage. |
| `overkill` | Après le code | Signale ce qui peut être réduit : volume, fichiers, abstractions. |
| `align` | Après le code | Signale les écarts avec les patterns et conventions déjà en place. |

Les skills de relecture (`digest`, `overkill`, `align`) **évaluent le code, signalent et donnent des pistes d'amélioration, mais ne proposent en aucun cas de solution**. C'est le développeur qui décide de ce qu'il change. `scope-check` est différent : il s'adresse à l'agent qui a développé, pour qu'il corrige lui-même avant la relecture humaine.

---

## Installer dans un projet (10 minutes)

1. Copier `AGENTS.md`, `CLAUDE.md`, `skills/` et `.gitlab/` à la racine du projet.
2. Remplir la section **Projet** d'`AGENTS.md` : commandes, patterns de référence, zones sensibles et seuils.
3. Pour Claude Code : `mkdir -p .claude && ln -s ../skills .claude/skills`. Les autres agents (Codex, Cursor, Copilot…) lisent `AGENTS.md` directement.
4. Ajouter la ligne « Niveau d'assistance IA » au modèle de ticket.

---

## Mise en application

Chaque ticket de développement se voit attribuer, lors du cadrage technique, un **niveau d'assistance IA**.
Ce niveau définit :

- la place respective du développeur et de l'IA ;
- les skills recommandés ;
- le niveau de validation collective attendu avant et après le développement.

L'objectif n'est pas de limiter l'usage de l'IA, mais d'adapter son niveau d'autonomie au risque, à la complexité et au niveau de compréhension nécessaire.

---

## Les 3 niveaux d'assistance

### 1. Assisted : **Human leads. AI advises.**

Le développeur conserve entièrement la réalisation du code.
L'IA peut :

- challenger une approche ;
- répondre à des questions ;
- analyser du code existant ;
- proposer des pistes ;
- relire et commenter une implémentation.

Elle ne génère pas directement la solution à la place du développeur.

**Skills recommandés :**

- **Pendant le développement :** `pair`
- **Pour relire, si on le souhaite :** `digest`, puis `overkill` et `align`

**Typical use:**
`Architecture` · `Core domain` · `New domain` · `Unclear requirements`

### 2. Delegated : **Human specifies. AI implements. Human controls.**

Le développeur peut librement utiliser son agent pour analyser l'US, construire un plan et produire tout ou partie du développement.
L'autonomie accordée à l'IA est compensée par des contrôles systématiques après génération.

**Skills recommandés :**

- **Après chaque itération de l'agent :** `scope-check`, en boucle, jusqu'à ce que le diff colle à la demande
- **Puis :** `digest`, puis `overkill` et `align`
- Le développeur relit l'intégralité du diff.

**Typical use:**
`Well-scoped feature` · `Refactoring` · `Tests` · `Known patterns`

### 3. Agentic : **Human decides. Agent executes. Team validates.**

L'agent peut prendre en charge une part importante du cycle de développement. En revanche, l'autonomie d'exécution implique une **validation humaine plus forte avant la génération du code.**

La vitesse apportée par l'agent ne doit pas accélérer la prise de décision technique. Au contraire, plus l'exécution devient autonome, plus l'intention et la stratégie doivent être explicites et partagées.

L'objectif est volontairement de déplacer le ralentissement :

> **Slow down the decision. Speed up the execution.**

**Skills recommandés :**

- **Avant de coder :** `plan-first`. Le plan est proposé dans une MR brouillon et validé par un autre développeur.
- **Après chaque itération de l'agent :** `scope-check`, en boucle, par rapport au plan validé
- **Puis :** `digest`, puis `overkill` et `align`

**Typical use:**
`Bulk migrations` · `Dependency upgrades` · `Test coverage` · `Repetitive changes`

---

## Faire évoluer le cadre

- Les skills sont **mutualisés dans le repository**, accessibles à toute l'équipe et versionnés comme du code.
- Toute évolution significative d'un skill passe donc par une Merge Request.

---

## Manifeste

La généralisation de l'IA change profondément le métier de développeur : écrire du code n'est plus la seule manière de produire une solution. Il faut désormais choisir consciemment qui doit la produire : l'humain ou la machine.

Nous refusons donc un usage automatique de l'IA, tout comme nous refusons de sanctuariser le développement manuel. Chaque tâche doit commencer par une question : est-il plus pertinent que je le fasse moi-même ou que je le confie à l'IA ?

Il n'existe pas de réponse universelle. Une tâche complexe peut justifier l'usage intensif d'un agent comme elle peut nécessiter une maîtrise humaine complète. Une tâche simple peut être automatisée en quelques secondes ou réalisée plus efficacement directement par un développeur. Le bon choix dépend du contexte, du risque, du besoin de compréhension, du coût de contrôle et de la valeur réelle apportée par l'automatisation.

Cette décision doit également intégrer le coût de l'IA. Les tokens, les calculs et les boucles agentiques ne sont pas gratuits, ni économiquement ni environnementalement. Utiliser l'IA doit donc être un choix, pas un réflexe.

Nous mettons en place ce framework pour rendre ce choix explicite, partagé et maîtrisé. Il ne définit pas ce que l'humain doit systématiquement faire ni ce que la machine doit systématiquement prendre en charge. Il crée les conditions pour décider, à chaque développement, quel niveau d'assistance est réellement pertinent.

L'objectif n'est pas d'utiliser plus ou moins d'IA. Il est de l'utiliser là où elle a du sens.

---
