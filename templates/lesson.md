---
id: "[ID]"
title: "[Titre de la leçon]"
card: ".ai/project/spec/curriculum/[chemin de la fiche]"
track: "[core | engineering | product-experience | business-people | overlays]"
minutes: 0
status: draft
last_verified: "AAAA-MM-JJ"
native_review: pending
glossary: []
---

<!-- GUIDE
How to use this template (English guidance; delete every GUIDE comment once the lesson is written):

- Copy this file to lessons/<same relative path as the card under .ai/project/spec/curriculum/>. See .ai/project/spec/module-map.md.
- Front matter:
  - id: the module ID.
  - title: the French title, in sentence case, without the ID.
  - card: the path of the module card.
  - track: one of the listed values.
  - minutes: the card's "Time" line (OD-05).
  - status: draft | review | ready.
  - last_verified: the date the "re-verify" list was last checked.
  - native_review: pending until a native speaker has reviewed the lesson, then "done YYYY-MM-DD".
  - glossary: the terms this lesson introduces or relies on.
- A lesson has three layers:
  1. Learner text: plain paragraphs. It goes to the textbook.
  2. Slides: regions that open with an HTML comment reading "slide: TYPE" and close with one reading "/slide", as below. They go to the deck.
  3. Speaker notes: the <details> block inside each slide region. They go to the notes pane, never to the textbook.
- Slide types: title, section, concept, example, checkpoint, exercise, recap. Layouts and word limits are in DESIGN.md, section 4.2. One idea per slide.
- The slide heading is a statement, in sentence case, with no final period (DESIGN.md, section 9).
- Speaker notes:
  - full sentences the presenter can say, at about 110 words per planned minute;
  - a timing mark at the start, such as [3 min];
  - stage directions in square brackets;
  - the transition into each checkpoint written out word for word;
  - "Si vous êtes en retard" where a cut is allowed.
- Teach every required topic of the card. Recommended and optional topics go only in "Pour aller plus loin".
- Each idea opens with a concrete example, then names the concept (DESIGN.md, section 8). Use the session's running example where it fits.
- Version numbers and dated product behaviour go only in "À revérifier avant chaque prestation", or in C-02.
- French typography follows DESIGN.md, section 9: non-breaking spaces before ":" and inside « », no space before ; ! ?, and ’ as the apostrophe.
-->

# [Titre de la leçon]

[Une ou deux phrases pour le manuel : ce que ce module change pour la personne qui travaille avec un assistant.]

<!-- slide: section -->
### [Titre de la leçon]

<details><summary>Notes de présentation</summary>

[1 min] [Phrase d’ouverture qui relie ce module au précédent et à l’exemple fil rouge de la séance.]

</details>
<!-- /slide -->

## Objectifs

À la fin de ce module, vous serez en mesure :

- de [verbe d’action et résultat observable, repris de la fiche];
- de [verbe d’action et résultat observable, repris de la fiche].

<!-- GUIDE List exactly the outcomes of the card, no more and no fewer. Each item continues the introductory sentence, starts in lowercase and ends with a semicolon; the last one ends with a period. -->

## Déroulement

| Étape | Minutes | Diapositives |
|---|---|---|
| [Première idée] | [n] | [n à n] |
| [Deuxième idée] | [n] | [n à n] |
| Point de contrôle | [n] | [n] |
| Pratique | [n] | [n] |
| Récapitulatif | [n] | [n] |
| **Total** | [n] | |

Si vous êtes en retard : [ce qui peut être coupé, selon la fiche et le déroulement de la séance].

<!-- GUIDE The checkpoint always gets its own row (OD-05). The total equals the front matter "minutes". -->

## [Première idée]

[Texte pour le manuel : l’exemple concret, présenté en quelques phrases.]

<!-- slide: example -->
### [Affirmation qui annonce ce que l’exemple montre]

[Extrait de l’exemple : un courriel, un échange avec l’assistant, un tableau ou un extrait de code.]

<details><summary>Notes de présentation</summary>

[2 min] [Ce que vous dites en montrant l’exemple, en phrases complètes.] [Pause] [La question que vous posez à la salle, si elle a lieu.]

</details>
<!-- /slide -->

[Texte pour le manuel : l’idée nommée après l’exemple, en une ou deux phrases.]

<!-- slide: concept -->
### [L’idée, formulée comme une affirmation]

[Au plus quatre lignes courtes, ou un seul schéma.]

<details><summary>Notes de présentation</summary>

[2 min] [L’explication en phrases complètes, qui complète la diapositive sans la lire.]

</details>
<!-- /slide -->

<!-- GUIDE Repeat this unit (example, then concept) for each idea of the card's required topics, one idea per unit. -->

## Point de contrôle

[La question de la fiche, telle qu’on la pose à la salle.]

<!-- slide: checkpoint -->
### [La question de la fiche]

<details><summary>Notes de présentation</summary>

[3 min] Transition : « [la phrase exacte qui introduit la question] »

[Lisez la question.] [Pause : comptez lentement jusqu’à sept avant de parler.] [Attendez deux ou trois réponses.]

[Résumé en une phrase : la réponse attendue.]

</details>
<!-- /slide -->

## Pratique

[La tâche, sa durée et le résultat attendu, sur du matériel synthétique.]

<!-- slide: exercise -->
### [Ce que les personnes participantes font maintenant]

1. [Étape] ([n] min)
2. [Étape] ([n] min)

<details><summary>Notes de présentation</summary>

[n min] [Les consignes à dire, le signal de départ, ce que vous observez pendant l’exercice, le signal de fin.]

</details>
<!-- /slide -->

## Récapitulatif

[Pour le manuel : les points à retenir, reformulés et rattachés à l’exemple fil rouge.]

<!-- slide: recap -->
### [Ce que vous retenez de ce module]

- [Énoncé rattaché à une étape du module]
- [Énoncé rattaché à une étape du module]

<details><summary>Notes de présentation</summary>

[2 min] [Demandez d’abord à la salle de nommer ce qu’elle retient, puis montrez les énoncés pour confirmer.]

</details>
<!-- /slide -->

## Pour aller plus loin

[Les sujets recommandés et facultatifs de la fiche, en texte de référence, avec des liens vers les lectures complémentaires.]

## À revérifier avant chaque prestation

- [Élément à revérifier, repris de la fiche, avec sa date de vérification]
