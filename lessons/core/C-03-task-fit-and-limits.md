---
id: C-03
title: "Où l’assistant aide, et où il échoue"
card: .ai/project/spec/curriculum/core/C-03-task-fit-and-limits.md
track: core
minutes: 9
status: review
last_verified: "2026-11-11"
native_review: done 2026-11-11
glossary:
  - assistant
  - agent
  - application
  - révision humaine
  - revue de code
  - demande de fusion
  - dépôt
  - demande d’offres de services
  - offre de services
  - mandat
---

# Où l’assistant aide, et où il échoue

Savoir quoi confier à un assistant virtuel est la compétence la plus utile du début. Les personnes qui commencent par une tâche mal choisie concluent que l’assistant ne sert à rien, ou pire, lui font confiance là où il ne le faut pas.

<!-- slide: section -->
### Où l’assistant aide, et où il échoue

<details><summary>Notes de présentation</summary>

[0,5 min] Vous savez maintenant ce qu’est un assistant. Reste une question plus utile : quoi lui confier? Les personnes qui commencent par une tâche mal choisie en tirent souvent une mauvaise conclusion. Certaines décident que l’assistant ne sert à rien. D’autres lui font confiance là où elles ne devraient pas. Dans ce module, vous apprenez à trier les tâches avant de les confier.

</details>
<!-- /slide -->

## Objectifs

À la fin de ce module, vous serez en mesure :

- de classer une tâche comme bonne candidate, mauvaise candidate ou à enjeux élevés;
- d’appliquer un test en cinq questions avant de confier une tâche;
- d’expliquer pourquoi l’expertise compte davantage avec l’intelligence artificielle (IA), et non moins.

## Déroulement

| Étape | Minutes | Diapositives |
|---|---|---|
| Ouverture | 0,5 | 1 |
| Trois zones | 2 | 2 et 3 |
| Cinq questions | 1 | 4 |
| Aider n’est pas décider | 1 | 5 |
| Point de contrôle | 3 | 6 |
| Pratique | 1 | 7 |
| Récapitulatif | 0,5 | 8 |
| **Total** | 9 | |

Si vous êtes en retard, ou dans la version de 90 minutes de la séance : au point de contrôle, faites voter sur deux tâches seulement, dont la troisième tâche. La pratique devient un exercice à faire après la séance.

## Trois zones

Pendant le mandat de Location Pavois, trois personnes de l’équipe font chacune une demande à un assistant. Léa, analyste d’affaires, lui demande de mettre au propre ses notes d’entrevue, sans rien ajouter. Elle lui demande aussi combien de réservations Location Pavois reçoit chaque mois, sans lui fournir aucun document. Julien, développeur, demande à un agent de programmation de modifier le code du portail dans le dépôt (*repository*) de Location Pavois.

<!-- slide: example -->
### Trois demandes qui ne se valent pas

> **Léa :** Mets au propre mes notes d’entrevue, sans rien ajouter.
>
> **Léa :** Combien de réservations Location Pavois reçoit-elle chaque mois?
>
> **Julien :** Modifie le code du portail dans le dépôt du client.

<details><summary>Notes de présentation</summary>

[1 min] Voici trois demandes, faites pendant notre mandat fictif. [Montrez la première ligne.] Léa a mené des entrevues avec le personnel des comptoirs. Elle demande à l’assistant de mettre ses notes au propre, sans rien ajouter. Elle lui donne la matière, et elle pourra tout vérifier. [Montrez la deuxième ligne.] Ensuite, elle demande combien de réservations le client reçoit par mois. Elle ne fournit aucun document. L’assistant répondra quand même, avec un chiffre plausible. Personne ne pourra le vérifier. [Montrez la troisième ligne.] Enfin, Julien confie à un agent une modification du portail du client. La tâche convient à un agent, mais une erreur toucherait les réservations réelles. [Pause] Trois demandes, donc trois traitements différents.

</details>
<!-- /slide -->

Ces trois demandes tombent dans trois zones.

Les bonnes candidates sont les tâches où vous fournissez la matière et pouvez juger le résultat : rédiger une ébauche, reformuler, résumer un document que vous donnez, changer de format, dégager une structure, expliquer, proposer des options, faire une première analyse, aider à programmer. Les notes de Léa en font partie.

Les mauvaises candidates sont les tâches où le résultat ne peut pas être vérifié ou ne devrait pas venir d’un assistant : un fait sans source à comparer, un résultat qui doit être juste sans relecture, un résultat que vous ne savez pas juger, une décision qui revient à une personne. Le nombre de réservations demandé sans document en fait partie.

Les tâches à enjeux élevés touchent les personnes (l’embauche, l’évaluation), l’argent, les engagements juridiques, les systèmes en production ou les livrables remis au client. L’assistant peut y aider, mais seulement avec une application approuvée par votre organisation et une révision humaine (*human review*) plus serrée. La modification de Julien en fait partie : elle passe par une demande de fusion (*pull request*), et Kevin, chez le client, en fait la revue de code (*code review*) avant de l’accepter.

<!-- slide: concept -->
### Chaque tâche tombe dans l’une de trois zones

- Vert : matière fournie, résultat que vous savez juger
- Jaune : personnes, argent, engagements, production, livrables
- Rouge : fait sans source, résultat impossible à juger

<details><summary>Notes de présentation</summary>

[1 min] Nommons maintenant ces trois zones, avec trois couleurs. Le vert, ce sont les bonnes candidates. Vous donnez la matière, et vous savez juger le résultat. C’est le cas des notes de Léa. Le rouge, ce sont les mauvaises candidates. Un fait sans source, ou un résultat que personne ne peut juger. C’est le nombre de réservations. Le jaune, ce sont les enjeux élevés : les personnes, l’argent, les engagements, les systèmes en production, ce qu’on remet au client. L’assistant peut aider, mais avec une application approuvée et une révision plus serrée. C’est la modification de Julien, que Kevin relit avant de l’accepter. [Pause] Gardez ces couleurs en tête : vous allez voter avec elles dans quelques minutes.

</details>
<!-- /slide -->

## Cinq questions

Avant de confier ses notes d’entrevue, Léa se pose cinq questions. Est-ce que ça vaut la peine? Oui, la mise au propre lui prend du temps. Que se passe-t-il si c’est faux? Un besoin du personnel pourrait disparaître ou changer de sens. Peut-elle revenir en arrière? Oui, c’est une ébauche, et elle garde ses notes d’origine. Quelles données faut-il? Les propos de personnes du client : ils ne vont que dans l’application approuvée par son organisation. Peut-elle vérifier le résultat? Oui, en le comparant ligne par ligne avec ses notes.

<!-- slide: concept -->
### Cinq questions avant de confier une tâche

- Valeur : que gagne-t-on?
- Risque, réversibilité : si c’est faux, peut-on défaire?
- Sensibilité : quelles données fournir?
- Vérifiabilité : vérifier comment, et en combien de temps?

<details><summary>Notes de présentation</summary>

[1 min] Avant de confier une tâche, posez cinq questions. Reprenons les notes de Léa. Est-ce que ça vaut la peine? Oui, la mise au propre lui prend du temps. Et si c’est faux? Un besoin pourrait disparaître. Peut-elle défaire? Oui, elle garde ses notes d’origine. Quelles données faut-il? Les propos du personnel du client, donc seulement dans l’application approuvée. Peut-elle vérifier? Oui, ligne par ligne. [Pause] Regardez la dernière question. Elle compte deux choses : savoir vérifier, et le temps que ça prend. Si vérifier prend plus de temps que faire la tâche vous-même, gardez-la.

</details>
<!-- /slide -->

Le test tient en cinq mots. La valeur : est-ce que ça vaut la peine? Le risque : que se passe-t-il si le résultat est faux? La réversibilité : peut-on revenir en arrière? La sensibilité : quelles données la tâche demande-t-elle? La vérifiabilité : pouvez-vous vérifier le résultat, et combien de temps cela prendra-t-il? Une tâche qui échoue à l’une de ces questions passe au jaune ou au rouge.

## Aider n’est pas décider

Avant de rédiger l’offre de services, Isabelle compare trois options : un développement sur mesure et deux logiciels de location. Elle peut demander à l’assistant un tableau qui compare les trois options, à partir de la demande d’offres de services et de ses notes de découverte. Elle ne lui demande pas de choisir. Le choix revient à Isabelle, et l’offre est approuvée par la direction de son organisation. Isabelle peut juger le tableau, parce qu’elle a rencontré le client et connaît ses besoins. Une personne qui n’a pas assisté aux rencontres ne verrait pas ce que le tableau oublie.

<!-- slide: concept -->
### Aider à décider n’est pas décider

- L’assistant peut vous aider à décider.
- La décision revient à une personne.
- Vous ne confiez que ce que vous savez juger.

<details><summary>Notes de présentation</summary>

[1 min] Dernière idée de ce module. Isabelle doit choisir entre trois options pour l’offre. Elle demande à l’assistant de les comparer dans un tableau. C’est de l’aide. Elle ne lui demande pas de choisir. Le choix lui revient, et la direction de son organisation approuve l’offre. [Pause] Pourquoi Isabelle peut-elle se fier à ce tableau? Parce qu’elle a rencontré le client. Elle voit tout de suite ce qui manque. Une personne qui n’y était pas ne le verrait pas. Vous ne pouvez confier que ce que vous savez juger. C’est pourquoi votre expertise compte davantage avec l’IA, et non moins.

</details>
<!-- /slide -->

« L’IA peut aider à faire ceci » et « l’IA devrait décider ceci » sont deux énoncés différents. Le premier décrit une aide; le second retire la décision à la personne qui en rend compte. Pour juger un résultat, il faut savoir à quoi ressemble un bon résultat. C’est votre expertise qui repère l’erreur avant l’envoi, et l’assistant ne la remplace pas.

## Point de contrôle

Trois tâches. Pour chacune, votez : vert, jaune ou rouge? Ensuite, une personne volontaire explique son vote pour la tâche jaune.

1. Dresser la liste des exigences de la demande d’offres de services de Location Pavois.
2. Décider si votre organisation répond à la demande d’offres de services.
3. Rédiger, pour le personnel des succursales, un résumé du projet d’une page.

Réponses attendues : la première tâche est verte, car la demande est fournie et chaque exigence se vérifie; la deuxième est rouge, car la décision revient à une personne, ici la direction de votre organisation; la troisième est jaune, car c’est un document remis au client, qui demande une révision attentive. La troisième divise souvent la salle, et c’est voulu.

<!-- slide: checkpoint -->
### Trois tâches : vert, jaune ou rouge?

1. Lister les exigences de la demande
2. Décider si l’on répond à la demande
3. Résumer le projet pour le personnel

<details><summary>Notes de présentation</summary>

[3 min] Transition : « Vous avez trois couleurs et cinq questions. Essayons-les sur trois tâches de notre mandat. »

[Lisez la question, puis chaque tâche.] [Pause : comptez lentement jusqu’à sept avant de parler.] [Pour chaque tâche, dites « vert », puis « jaune », puis « rouge », et demandez de lever la main à la couleur choisie.] [Demandez à une personne qui a voté jaune pour la troisième tâche d’expliquer son vote.] [Si personne ne se porte volontaire, proposez une raison : c’est un document remis au client. Demandez si la salle est d’accord.] [Corrigé : 1, vert; 2, rouge; 3, jaune. Ne tranchez pas trop vite la troisième : le désaccord sur cette tâche est le cœur de l’exercice.]

Résumé : « La même tâche peut sembler verte à l’une et jaune à l’autre; les cinq questions servent à trancher. »

</details>
<!-- /slide -->

## Pratique

Notez trois tâches de votre propre semaine : une verte, une jaune et une rouge. Durée : 1 minute en séance, en silence; seul ou seule avec le manuel.

Résultat attendu : trois tâches réelles, chacune avec sa couleur et, pour la jaune, ce qui la rend sensible (des personnes, de l’argent, un engagement, un système en production ou un livrable). Gardez la tâche verte : vous l’essaierez avec la boucle de travail après la séance, ou dans l’atelier de votre parcours.

<!-- slide: exercise -->
### Notez une tâche de votre semaine pour chaque couleur

1. Une tâche verte (0,5 min)
2. Une jaune, puis une rouge (0,5 min)

<details><summary>Notes de présentation</summary>

[1 min] À vous, maintenant, en silence. Notez trois tâches de votre propre semaine : une verte, une jaune, une rouge. Gardez la verte : vous l’essaierez après la séance. [Lancez la minuterie pour une minute. Ne demandez pas de partager les réponses.]

</details>
<!-- /slide -->

## Récapitulatif

Avant de confier une tâche, placez-la dans l’une de trois zones : les notes de Léa sont vertes, la modification de Julien est jaune, le nombre de réservations demandé sans document est rouge. Cinq questions aident à trancher : la valeur, le risque, la réversibilité, la sensibilité et la vérifiabilité. Enfin, l’assistant peut aider à décider, mais ne décide pas, et vous ne confiez que ce que vous savez juger.

<!-- slide: recap -->
### Ce que vous retenez de ce module

- Vert, jaune, rouge : trier avant de confier
- Cinq questions pour trancher les cas douteux
- On ne confie que ce qu’on sait juger

<details><summary>Notes de présentation</summary>

[0,5 min] Qu’est-ce que vous retenez? [Attendez deux réponses, puis montrez les énoncés.] Trois zones, cinq questions, et une règle : on ne confie que ce qu’on sait juger. Voyons maintenant quelles applications existent aujourd’hui.

</details>
<!-- /slide -->

## Pour aller plus loin

Ces sujets ne sont pas présentés en séance. Ils servent de référence.

- La frontière est inégale : l’assistant réussit très bien certaines tâches qui semblent difficiles et échoue à d’autres qui semblent faciles. Testez-le sur un exemple réel au lieu de le supposer.
- Comptez le temps honnêtement : le temps gagné, moins le temps passé à relire et à corriger.
- Pour commencer, choisissez des tâches fréquentes, à faible risque et faciles à vérifier.

Sujets facultatifs :

- un inventaire des tâches de l’équipe, avec un atelier pour classer les occasions;
- le choix d’un premier projet pilote.

Le sens de chaque terme est dans le [glossaire](../../resources/R-02-glossary.md). Les lectures complémentaires (R-01) donnent les sources, section « Fondements ».

## À revérifier avant chaque prestation

- Rien de daté : ce module ne nomme aucun produit et ne décrit aucune fonction datée. Dernière vérification : le 11 novembre 2026.
