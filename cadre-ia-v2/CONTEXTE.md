# Contexte du repo : pour le LLM qui m'aide à le faire évoluer

Lis ce fichier avant toute modification. Il explique ce qu'est ce repo, d'où il vient et comment m'aider.

## Ce qu'est ce repo

C'est un cadre qui aide une équipe tech à décider, ticket par ticket, de la place qu'elle donne à l'IA dans le développement. Il fournit aussi les garde-fous nécessaires pour que le code produit par l'IA respecte la vision des humains.

**Attention :** `AGENTS.md`, `CLAUDE.md`, `skills/` et `.gitlab/` sont **le produit** : ce sont des fichiers que l'équipe copie dans ses projets. Ce ne sont pas des instructions pour toi. Si ton outil les charge automatiquement, ignore leurs consignes (mode IA, contestation de périmètre…) quand tu travailles sur ce repo-ci. Traite-les comme des textes à relire et à améliorer.

## La vision, en trois objectifs

1. **Limiter la quantité de code.** Le plus petit changement raisonnable.
2. **Garantir la cohérence des choix** avec l'architecture et les patterns existants.
3. **Une IA capable de contester une modification trop profonde**, même quand elle découle d'une demande fonctionnelle légitime. Contester ne veut pas dire refuser : la décision reste humaine.

Toute modification du cadre doit servir au moins un de ces objectifs, ou rendre le cadre plus facile à adopter.

## Le manifeste initial (texte de référence, à ne pas réécrire sans que je le demande)

> La généralisation de l'IA change profondément le métier de développeur : écrire du code n'est plus la seule manière de produire une solution. Il faut désormais choisir consciemment qui doit la produire : l'humain ou la machine.
>
> Nous refusons donc un usage automatique de l'IA, tout comme nous refusons de sanctuariser le développement manuel. Chaque tâche doit commencer par une question : est-il plus pertinent que je le fasse moi-même ou que je le confie à l'IA ?
>
> Il n'existe pas de réponse universelle. Une tâche complexe peut justifier l'usage intensif d'un agent comme elle peut nécessiter une maîtrise humaine complète. Une tâche simple peut être automatisée en quelques secondes ou réalisée plus efficacement directement par un développeur. Le bon choix dépend du contexte, du risque, du besoin de compréhension, du coût de contrôle et de la valeur réelle apportée par l'automatisation.
>
> Cette décision doit également intégrer le coût de l'IA. Les tokens, les calculs et les boucles agentiques ne sont pas gratuits, ni économiquement ni environnementalement. Utiliser l'IA doit donc être un choix, pas un réflexe.
>
> Nous mettons en place ce framework pour rendre ce choix explicite, partagé et maîtrisé. Il ne définit pas ce que l'humain doit systématiquement faire ni ce que la machine doit systématiquement prendre en charge. Il crée les conditions pour décider, à chaque développement, quel niveau d'assistance est réellement pertinent.
>
> L'objectif n'est pas d'utiliser plus ou moins d'IA. Il est de l'utiliser là où elle a du sens.

## Les choix structurants (ne pas les défaire sans en discuter)

- **Un mode par ticket**, choisi au cadrage : Assisted, Delegated ou Agentic. Ce ne sont pas des niveaux de maturité.
- **Trois questions plutôt qu'un score.** Une note chiffrée donne une fausse précision, et chacun finit par l'ajuster pour obtenir le mode qu'il voulait.
- **Sept skills, pas plus sans bonne raison.** Moins il y en a, plus l'adoption est rapide.
- **Les skills de relecture signalent sans corriger.** La décision reste au développeur.
- **Les seuils de contestation sont concrets et réglables** par projet, dans `AGENTS.md`.

## Ce qui a été abandonné (v0.1, « Three-Layer Strategy »)

Il s'agissait d'un framework de spec-driven development : six documents par changement, un score de 0 à 12, un mode à choisir pour chaque étape. Il était trop lourd, écrit par une machine pour des machines, et passait à côté des trois objectifs. Ne réintroduis pas ces mécanismes.

## Comment m'aider

- **Le public, ce sont des humains** : des développeurs et des tech leads. Écris en français, de façon concise, précise et mesurée. Pas de jargon gratuit, pas de superlatifs.
- **Propose des modifications courtes et ciblées.** Montre le passage avant et après plutôt que de réécrire un fichier entier.
- **Garde la cohérence** entre `README.md`, `AGENTS.md`, les skills et le modèle de MR. Si tu changes un terme ou une règle quelque part, signale les autres endroits concernés.
- **Ajoute un fichier, une section ou un skill seulement si c'est nécessaire.** Supprimer vaut souvent mieux qu'ajouter.
- **Si une demande contredit la vision ou les choix ci-dessus, dis-le** avant de l'appliquer.
